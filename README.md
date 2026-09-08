# Macro & Commodity Research Repository

[![Research Period](https://img.shields.io/badge/Research%20Period-2014%20--%202026-blue.svg)](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/)
[![Focus Area](https://img.shields.io/badge/Focus-Macro%20%7C%20Commodities%20%7C%20Equities%20%7C%20Energy%20Transition-brightgreen.svg)](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/)
[![Author](https://img.shields.io/badge/Author-Adhrit%20Ghosh-purple.svg)](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/)

A structured institutional-grade repository housing macroeconomic research notes, commodity transmission frameworks, policy impact studies, quantitative signal architectures, and backtesting harnesses.

---

## 🏛️ Repository Architecture

```
macro-commodity-research/
│
├── README.md                                    # Main repository documentation & research synthesis
│
├── reports/                                     # Publication-ready research notes & executive summaries
│   ├── 01-crude-oil-indian-equities/            # Crude oil price shocks, OMCs, refiners & EV hedge
│   │   ├── report.pdf                           # Complete publication PDF
│   │   └── README.md                            # Executive summary & key data tables
│   │
│   ├── 02-dark-gold-digital-gold/               # AI compute, grid bottlenecks, metals & nuclear SMRs
│   │   ├── report.pdf                           # Complete publication PDF
│   │   └── README.md                            # The 5-layer commodity transition framework
│   │
│   └── 03-modi-era-policies/                    # 2014–2025 structural reforms & banking recapitalization
│       ├── report.pdf                           # Complete publication PDF
│       └── README.md                            # Policy timeline & banking equity performance
│
├── charts/                                      # Chart generation scripts & visual exhibits
│   ├── crude-oil/                               # Brent/WTI, crack spreads, OMC cash flows
│   ├── commodities/                             # Indexed metals (Cu, Zn, Sn, Ag) relative to crude
│   ├── equities/                                # PSU vs private banks, OMC vs EV manufacturers
│   ├── nuclear/                                 # India 100 GW 2047 roadmap & SMR pipeline
│   └── ai-energy/                               # Data centre power curves & water cooling stress
│
├── data/                                        # Raw time-series, processed metrics & metadata
│   ├── raw/                                     # Raw market feeds (EIA, CME, RBI, LME, MOSPI)
│   ├── processed/                               # Cleaned, standardized and indexed time-series
│   └── README.md                                # Data dictionary & provenance
│
├── notebooks/                                   # Interactive research & exploratory analyses
│   ├── 01_crude_equities_analysis.ipynb         # Upstream vs downstream OMC financial models
│   ├── 02_ai_energy_commodity_stack.ipynb       # 5-factor commodity scarcity signal implementation
│   ├── 03_modi_policy_regime_shifts.ipynb       # Policy event-study & banking asset quality trends
│   └── README.md
│
├── src/                                         # Core Python analytical library
│   ├── __init__.py
│   ├── data_loader.py                           # Automated data ingestion & FRED/Yahoo Finance pipelines
│   ├── indicators.py                            # Custom Z-score standardizers & crack-spread calculators
│   ├── signal_engine.py                         # Multi-layer macro-commodity scoring model
│   ├── visualizer.py                            # Publication-standard plotting routines
│   └── README.md
│
└── backtests/                                   # Quantitative backtesting harnesses & return attribution
    ├── commodity_scarcity_backtest.py           # Long/short commodity & equity factor backtest
    ├── policy_momentum_backtest.py              # Event-driven policy sector allocation strategy
    └── README.md
```

---

## 📚 Cornerstone Research Reports

### 1. [Crude Oil & Indian Equities: Report on the Price Action of Crude Oil](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/reports/01-crude-oil-indian-equities/README.md)
* **Author:** Adhrit Ghosh | **Research Period:** September 2025
* **Core Question:** How do changing global crude dynamics, OPEC+ supply quotas, and geopolitical tensions transmit into the financial health of Indian upstream and downstream equity markets?
* **Key Findings:**
  * **Upstream vs. Downstream Divergence:** Rising crude prices deliver operating leverage to upstream producers (ONGC, OIL) while compressing gross refining margins (GRMs) and marketing margins for downstream Oil Marketing Companies (OMCs).
  * **OMC Cash Flow Polarization:** Detailed financial breakdown of IOC, BPCL, and HPCL. While IOC encountered negative operating cash flow pressures due to elevated operating cost runs, BPCL and HPCL demonstrated superior cash generation and resilient balance sheets, backed by strategic capex (e.g., BPCL's ₹95,000 Cr Andhra Pradesh refinery).
  * **Macro De-dollarization & Settlement Channels:** Evaluation of currency risks (USD/INR depreciation) and non-traditional bilateral energy settlements (e.g., UAE-India settlement frameworks bypassing traditional FX rails).
  * **Long-Term Structural Hedge:** Growing consumer and fleet adoption of Two-Wheeler / Commercial EVs (Ather Energy, Ola Electric) acts as an asymmetric hedge against perpetual crude price volatility and domestic oil production decline (-3% YoY).

---

### 2. [From Dark Gold to Digital Gold: The Commodities Behind the AI–Energy Transition](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/reports/02-dark-gold-digital-gold/README.md)
* **Author:** Adhrit Ghosh | **Research Period:** September 2026
* **Core Question:** Where does economic scarcity migrate when modern technological demand shifts from hydrocarbons to high-density compute and power infrastructure?
* **Transmission Architecture:**
  $$\text{AI Demand} \longrightarrow \text{Data Centres} \longrightarrow \text{Electricity Demand} \longrightarrow \text{Grid \& Firm Power} \longrightarrow \begin{cases} \text{Metals (Cu, Zn, Sn, Ag)} \\ \text{Nuclear \& SMRs} \\ \text{Cooling \& Water Infrastructure} \end{cases}$$
* **Key Insights:**
  * **Industrial Metals Basket:** Copper (grid transmission, transformer windings), Zinc (galvanizing & structural steel corrosion resistance), Tin (electronics packaging & solder), and Silver (photovoltaics & high-conductivity contacts).
  * **India Nuclear Renaissance:** Analyzing India's strategic roadmap targeting **100 GW of nuclear capacity by 2047** (from ~8.78 GW baseline), with indigenous Small Modular Reactor (SMR) development: **BSMR-200** (220 MWe), **SMR-55** (55 MWe), and **HTGCR** (5 MWth heat applications).
  * **The Water Bottleneck:** Water is a physical cooling constraint. Evaluation of water-stress pricing, cooling architectures (immersion vs. closed-loop), and the CME Nasdaq Veles California Water Index (**NQH2O**).
* **Quantitative Signal Model:**
  $$S_t = w_1 Z(\Delta \text{AI}_t) + w_2 Z(\Delta \text{Power}_t) + w_3 Z(\text{MetalTightness}_t) + w_4 Z(\text{NuclearPipeline}_t) + w_5 Z(\text{WaterStress}_t)$$
  $$\text{where } \sum_{i=1}^5 w_i = 1$$

---

### 3. [Impact on the Market due to Modi-Era Government Policies (2014–2025)](file:///c:/Users/adhri/Downloads/Research%20Portfolio/macro-commodity-research/reports/03-modi-era-policies/README.md)
* **Author:** Adhrit Ghosh | **Research Period:** September 2025
* **Core Question:** How did the sequential policy architecture of the Modi administration transform India's financial sector and equity market leadership over a decade?
* **Policy Chronology & Structural Phases:**
  1. **2014–2016 (Inclusion & Manufacturing):** *Make in India*, *Pradhan Mantri Jan Dhan Yojana* (500M+ zero-balance accounts), *Digital India*.
  2. **2016–2017 (Structural Cleansing & Formalization):** *Demonetization*, *Insolvency & Bankruptcy Code (IBC)*, *Goods & Services Tax (GST)*, *RERA*.
  3. **2018–2020 (Social Safety & Shock Absorption):** *Ayushman Bharat*, *Corporate Tax Rate Cuts (to 22%/15%)*, *Aatmanirbhar Bharat COVID stimulus*.
  4. **2020–2025 (Capital Investment & Scale):** *Production-Linked Incentive (PLI) Schemes*, *FDI Liberalization*, *Massive Infra Capex*, *GST 2.0 Rationalization*.
* **The Banking System as the Primary Engine:**
  * Resolution of the "Twin Balance Sheet" crisis through IBC and multi-year PSU bank recapitalizations (₹3.1+ Lakh Cr).
  * Evolution of banking leaders: **HDFC Bank** (retail scale and HDFC Ltd mega-merger), **ICICI Bank** (post-2018 governance overhaul and RoA expansion), **SBI** (associate bank consolidation and balance sheet strength), and **Axis Bank** (corporate book turnaround).

---

## 📊 Analytical Dimensions & Modules

| Module | Core Variables & Datasets | Primary Tools / Scripts | Output Artifacts |
| :--- | :--- | :--- | :--- |
| **`charts/`** | Brent/WTI, LME Copper/Zinc/Tin/Silver, Nifty 50, Bank Nifty, NQH2O | Matplotlib, Seaborn, Plotly | High-resolution SVG/PNG charts |
| **`data/`** | Historical daily OHLCV, macro indicators, government capex series | CSV, Parquet, JSON schemas | Normalized multi-asset data feeds |
| **`notebooks/`** | Interactive Jupyter notebooks for regression, Granger causality & event studies | Pandas, NumPy, Statsmodels | Reproducible research notebooks |
| **`src/`** | Modular library for signal generation, factor normalization, and API ingestion | Python 3.10+ package | Reusable analytical modules |
| **`backtests/`** | Vectorized and event-driven backtesting engines with Sharpe/Sortino metrics | Custom Backtester, Vectorbt | Trade logs, equity curves & tear sheets |

---

---
*Repository maintained by **Adhrit Ghosh**. For analytical queries and dataset access, refer to the respective report directories.*
