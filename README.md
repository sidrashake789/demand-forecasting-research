# Demand Forecasting and Inventory Optimization

Executive Summary

Retailers lose billions of dollars annually to stockouts and excess inventory. This repository contains an end-to-end machine learning pipeline and empirical research evaluating how predictive modeling can optimize retail supply chain efficiency using over 76,000 historical sales transactions.

Product Problem & User Value

The User: Inventory Managers and Store Buyers who need advanced warning of demand surges.

The Problem: Traditional rolling averages fail to capture non-linear demand spikes caused by promotions and seasonality, leading to empty shelves or tied-up capital.

The Solution: A robust regression pipeline utilizing lag features and tree-based ensemble models to forecast item-level demand accurately.

# Key Technical Highlights

Rigorous Validation: Implemented strict chronological train-test splitting to prevent data leakage and simulate real-world deployment.

Model Comparison: Evaluated Linear Regression against Random Forest and tuned Gradient Boosting models.

Performance Gains: Reduced Mean Absolute Percentage Error (MAPE) from 18.4% down to 5.8%.


# How to Run

Clone this repository:

git clone https://github.com/sidrashake789/demand-forecasting-research.git


Install dependencies:

pip install -r requirements.txt


Explore the Jupyter notebooks in the notebooks/ directory.

Author: Sidra Shaikh
