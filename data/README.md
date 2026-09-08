# Data Architecture & Schemas

This directory maintains the quantitative time-series datasets, macro indicators, and corporate financial data backing all research notes.

## Directory Structure
```
data/
├── raw/                      # Unaltered raw API/manual export files (.csv, .json)
│   ├── brent_crude_daily.csv
│   ├── lme_metals_daily.csv
│   ├── india_omc_financials.csv
│   ├── india_banking_metrics.csv
│   └── nqh2o_water_index.csv
└── processed/                # Normalized, aligned, and cleaned datasets (.parquet, .csv)
    ├── macro_scarcity_features.parquet
    └── policy_equity_returns.parquet
```

## Data Feeds & Provenance
* **Energy & Commodities:** FRED (St. Louis Fed), EIA, LME, COMEX, CME Group.
* **Indian Financials & Equities:** NSE India, BSE, RBI DBIE (Database on Indian Economy).
* **Policy & Macro:** Press Information Bureau (PIB), Ministry of Finance, Ministry of Power.
