Hybrid Demand Forecasting Framework

This research project explores the integration of domain-specific contextual data (such as weather patterns and public health crises) into traditional statistical demand forecasting models. By moving from a purely transactional model to a context-aware hybrid framework, this study demonstrates a significant reduction in Mean Absolute Percentage Error (MAPE).

Key Findings
Baseline Performance: 43.51% MAPE (Statistical Model only)

Hybrid Framework Performance: 39.37% MAPE (Context-Aware)

Outcome: A 4.14 percentage point improvement in predictive accuracy.

Project Methodology
The model utilizes a Random Forest Regressor to analyze 76,000 transaction records. I implemented an epsilon-smoothing technique to ensure mathematical stability and engineered contextual modifiers to account for external environmental volatility.

Repository Contents
train_hybrid.py: The core Python implementation of the hybrid forecasting model.

Research_Paper.pdf: The full 5-page research report detailing our methodology, analysis, and future work.

How to Run
Clone this repository: git clone https://github.com/YOUR_USERNAME/demand-forecasting-research.git

Ensure you have the required libraries installed: pip install pandas scikit-learn

Execute the hybrid model: python train_hybrid.py
