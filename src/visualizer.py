"""
Publication-Quality Visualizer for Commodity & Macro Charts
Author: Adhrit Ghosh
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

def set_institutional_style():
    """Applies clean, institutional formatting parameters."""
    plt.rcParams.update({
        'figure.facecolor': '#FFFFFF',
        'axes.facecolor': '#FAFAFA',
        'axes.edgecolor': '#D0D7DE',
        'axes.grid': True,
        'grid.color': '#E1E4E8',
        'grid.linestyle': '--',
        'grid.alpha': 0.7,
        'font.family': 'sans-serif',
        'font.size': 10,
        'axes.titlesize': 12,
        'axes.titleweight': 'bold',
        'lines.linewidth': 1.75
    })

def plot_indexed_commodity_basket(df: pd.DataFrame, output_path: str = "charts/commodities/indexed_metal_basket.png"):
    """Plots indexed commodity price series (Base = 100)."""
    set_institutional_style()
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    for col in df.columns:
        ax.plot(df.index, df[col], label=col)
        
    ax.axhline(100, color='gray', linestyle=':', alpha=0.8)
    ax.set_title("Indexed Commodity & Metals Performance (Base = 100)")
    ax.set_ylabel("Index Level")
    ax.legend(frameon=True, facecolor='white', framealpha=0.9)
    plt.tight_layout()
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()
