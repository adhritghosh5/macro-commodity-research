"""
Technical and Macroeconomic Indicators Module
Author: Adhrit Ghosh
"""

import pandas as pd
import numpy as np

def calculate_zscore(series: pd.Series, window: int = 252) -> pd.Series:
    """
    Computes rolling Z-score: Z(t) = (X(t) - mu(t)) / sigma(t)
    """
    rolling_mean = series.rolling(window=window, min_periods=max(1, window // 4)).mean()
    rolling_std = series.rolling(window=window, min_periods=max(1, window // 4)).std()
    rolling_std = rolling_std.replace(0, np.nan)
    return (series - rolling_mean) / rolling_std

def index_to_base(df: pd.DataFrame, base_date: str = "2025-04-01", base_val: float = 100.0) -> pd.DataFrame:
    """
    Re-bases all time-series in DataFrame to base_val at base_date.
    """
    if base_date in df.index:
        base_levels = df.loc[base_date]
    else:
        # Nearest available date
        idx = df.index.get_indexer([pd.to_datetime(base_date)], method='nearest')[0]
        base_levels = df.iloc[idx]
    
    return (df.divide(base_levels)) * base_val

def compute_crack_spread(brent_price: pd.Series, gasoline_price: pd.Series, diesel_price: pd.Series) -> pd.Series:
    """
    Calculates 3:2:1 refinery crack spread proxy ($/bbl).
    """
    return (2 * gasoline_price + 1 * diesel_price) / 3.0 - brent_price
