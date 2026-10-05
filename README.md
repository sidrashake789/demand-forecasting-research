# A Hybrid Framework for Demand Forecasting

This repository contains the code and data pipeline for my undergraduate MIS project exploring how external context factors (like weather conditions and health outbreaks) affect retail demand forecasting. 

## Project Overview
Most standard retail forecasting models rely strictly on past sales history and pricing data. When sudden external disruptions occur,such as severe weather or public health crises, these historical models often struggle because they assume past sales patterns will simply repeat. 

In this project, I built a hybrid demand forecasting pipeline using a Random Forest regressor on 76,000 retail transaction records. By mapping categorical weather and epidemic indicators into custom numerical scoring weights, the hybrid model achieves a lower prediction error compared to a standard baseline model.

## Key Performance Results
* **Baseline Model MAPE:** 43.51% (Trained on transactional and pricing features only)
* **Hybrid Model MAPE:** 39.37% (Trained with engineered `Weather_Score` and `Epidemic_Score` features)
* **Improvement:** 4.14 absolute percentage point reduction in error (approx. 9.5% relative decrease).

---

## Repository Structure

```text
├── data/
│   ├── raw/
│   │   └── demand_forecasting.csv       # Original dataset (76,000 records)
│   └── processed/
│       └── demand_forecasting_hybrid.csv # Processed dataset with context score columns
├── src/
│   ├── features/
│   │   └── create_hybrid_features.py    # Maps weather/epidemic categories to numeric scores
│   └── models/
│       ├── train_baseline.py            # Baseline Random Forest model trainer
│       └── train_hybrid.py              # Hybrid Random Forest model trainer
├── experiments/
│   ├── analyze.py                       # Early exploratory HistGradientBoosting script
│   └── train_simple.py                  # Early 3-feature exploratory script
├── paper/
│   └── main.tex                         # LaTeX source code for the research paper
├── generate_paper.py                    # Script to compile project summary report
├── requirements.txt                     # Python dependencies
└── README.md
