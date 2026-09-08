"""
Data Loader Module for Macro & Commodity Time Series
Author: Adhrit Ghosh
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional

class DataLoader:
    """
    Handles ingestion, normalization, and time alignment for commodities,
    equities, and macroeconomic indicators.
    """
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_commodity_series(self, symbols: List[str], start_date: str, end_date: str) -> pd.DataFrame:
        """
        Loads daily closing prices for designated commodities (Brent, Copper, Zinc, Tin, Silver, NQH2O).
        """
        # Scaffold implementation for multi-asset alignment
        date_range = pd.date_range(start=start_date, end=end_date, freq='B')
        df = pd.DataFrame(index=date_range)
        df.index.name = 'Date'
        return df

    def load_indian_equities(self, tickers: List[str], start_date: str, end_date: str) -> pd.DataFrame:
        """
        Loads daily OHLCV series for Indian upstream, downstream OMCs, and banking champions.
        """
        date_range = pd.date_range(start=start_date, end=end_date, freq='B')
        df = pd.DataFrame(index=date_range)
        df.index.name = 'Date'
        return df

    def get_omc_financial_metrics(self) -> pd.DataFrame:
        """
        Returns structured financial snapshot for IOC, BPCL, and HPCL.
        """
        data = {
            "Company": ["Indian Oil Corporation (IOC)", "Bharat Petroleum (BPCL)", "Hindustan Petroleum (HPCL)"],
            "Operating Cash Flow Status": ["Strained / Volatile", "Robust Positive", "Positive & Growing"],
            "Capex Focus": ["Maintenance", "₹95k Cr AP Greenfield Refinery", "Refinery Modernization"],
            "Investment Stance": ["Underweight", "Overweight", "Overweight"]
        }
        return pd.DataFrame(data)
