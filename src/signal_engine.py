"""
Multi-Layer Quantitative Signal Engine
Author: Adhrit Ghosh

Implements the 5-layer Commodity Scarcity Scorecard:
S_t = w1*Z(Delta_AI) + w2*Z(Delta_Power) + w3*Z(MetalTightness) + w4*Z(NuclearPipeline) + w5*Z(WaterStress)
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional

class ScarcitySignalEngine:
    def __init__(self, weights: Optional[Dict[str, float]] = None):
        """
        Initializes signal engine with standardized layer weights summing to 1.0.
        """
        if weights is None:
            self.weights = {
                "ai_demand": 0.25,
                "power_demand": 0.25,
                "metal_tightness": 0.20,
                "nuclear_pipeline": 0.15,
                "water_stress": 0.15
            }
        else:
            total = sum(weights.values())
            self.weights = {k: v / total for k, v in weights.items()}

    def compute_composite_signal(self, features_df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates the weighted standardized multi-layer commodity scarcity signal.
        """
        out_df = pd.DataFrame(index=features_df.index)
        
        # Calculate individual standardized component contributions
        for component, weight in self.weights.items():
            if component in features_df.columns:
                out_df[f"{component}_z"] = features_df[component]
                out_df[f"{component}_weighted"] = features_df[component] * weight
            else:
                out_df[f"{component}_weighted"] = 0.0
                
        out_df["composite_scarcity_signal"] = out_df[[f"{c}_weighted" for c in self.weights.keys()]].sum(axis=1)
        
        # Trading regime indicators
        out_df["regime_extreme_scarcity"] = out_df["composite_scarcity_signal"] > 1.5
        out_df["regime_moderate_scarcity"] = (out_df["composite_scarcity_signal"] > 0.5) & (out_df["composite_scarcity_signal"] <= 1.5)
        out_df["regime_neutral_surplus"] = out_df["composite_scarcity_signal"] <= 0.5
        
        return out_df

if __name__ == "__main__":
    print("ScarcitySignalEngine initialized successfully.")
