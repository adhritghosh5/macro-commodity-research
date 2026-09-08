"""
Commodity Scarcity Multi-Layer Factor Backtest
Author: Adhrit Ghosh

Simulates a long/short macro commodity allocation based on the 5-layer composite signal:
- Long high-scarcity industrial metals (Cu, Zn, Sn) & Uranium / Power equipment equities when S_t > 1.0
- Neutral / Cash when S_t is between 0 and 1.0
- Short / Underweight upstream commodities when S_t < 0
"""

import pandas as pd
import numpy as np

class CommodityScarcityBacktester:
    def __init__(self, initial_capital: float = 1000000.0, transaction_cost_bps: float = 10.0):
        self.initial_capital = initial_capital
        self.transaction_cost = transaction_cost_bps / 10000.0

    def run_backtest(self, price_df: pd.DataFrame, signal_series: pd.Series) -> pd.DataFrame:
        """
        Executes vectorized signal-based portfolio allocation.
        """
        results = pd.DataFrame(index=price_df.index)
        results["Signal"] = signal_series
        results["Position"] = np.where(signal_series > 1.0, 1.0, np.where(signal_series < -0.5, -0.5, 0.0))
        
        # Benchmark return (e.g. equal weight commodity basket)
        benchmark_returns = price_df.pct_change().mean(axis=1)
        results["Benchmark_Returns"] = benchmark_returns
        results["Strategy_Returns"] = results["Position"].shift(1) * benchmark_returns - (
            results["Position"].diff().abs() * self.transaction_cost
        )
        
        results["Cumulative_Benchmark"] = (1 + results["Benchmark_Returns"]).cumprod()
        results["Cumulative_Strategy"] = (1 + results["Strategy_Returns"].fillna(0)).cumprod()
        
        return results

    def performance_summary(self, results: pd.DataFrame) -> dict:
        """Computes annualized Sharpe ratio, max drawdown, and total return."""
        strat_returns = results["Strategy_Returns"].dropna()
        ann_return = strat_returns.mean() * 252
        ann_vol = strat_returns.std() * np.sqrt(252)
        sharpe = ann_return / ann_vol if ann_vol > 0 else 0.0
        
        cum_ret = results["Cumulative_Strategy"]
        drawdown = (cum_ret - cum_ret.cummax()) / cum_ret.cummax()
        max_dd = drawdown.min()
        
        return {
            "Annualized Return": f"{ann_return * 100:.2f}%",
            "Annualized Volatility": f"{ann_vol * 100:.2f}%",
            "Sharpe Ratio": f"{sharpe:.2f}",
            "Max Drawdown": f"{max_dd * 100:.2f}%"
        }

if __name__ == "__main__":
    print("CommodityScarcityBacktester initialized.")
