# A Hybrid Framework for Demand Forecasting

## Executive Summary
Predicting retail demand accurately is a major challenge for supply chain planning. Traditional forecasting models rely strictly on historical sales transactions and pricing, often failing during unexpected real-world disruptions such as severe weather storms or public health crises.

This repository contains a machine learning framework evaluated on **76,000 retail transaction records** across 5 stores and 20 products from January 1, 2022, to January 30,2024. We compare a standard **Baseline Random Forest** against a **Context-Aware Hybrid Random Forest** that incorporates custom numeric scores for weather conditions and epidemic statuses.

## Key Performance Results
Evaluated using a modified Mean Absolute Percentage Error (MAPE) with epsilon smoothing ($\epsilon = 1.0$) to cleanly handle zero-sales days:

| Forecasting Model | Features Included | Modified MAPE ($\epsilon = 1.0$) |
| :--- | :--- | :---: |
| **Baseline Random Forest** | Inventory Level, Units Ordered, Price, Discount, Competitor Pricing | **43.51%** |
| **Hybrid Context Random Forest** | Inventory Level, Units Ordered, Price, Weather_Score, Epidemic_Score | **39.37%** |

* **Absolute Error Reduction:** **4.14 percentage points** (~9.5% relative error reduction).
* **Key Finding:** Adding structured domain context helps lower overprediction errors during bad weather or public health disruptions.

## Repository Structure
```text
demand-forecasting-research/
├── data/
│   ├── raw/
│   │   └── demand_forecasting.csv
│   └── processed/
│       └── demand_forecasting_hybrid.csv
├── experiments/
│   ├── analyze.py
│   └── train_simple.py
├── src/
│   ├── features/
│   │   └── create_hybrid_features.py
│   ├── models/
│   │   ├── train_baseline.py
│   │   └── train_hybrid.py
│   └── utils/
│       ├── check_context.py
│       ├── check_data.py
│       └── check_zeros.py
├── .gitignore
├── generate_paper.py
├── paper.tex
├── README.md
└── requirements.txt
