# Hybrid Demand Forecasting

Does adding weather and epidemic information make a retail demand forecast more accurate?

This project compares two Random Forest models that predict retail unit sales. One uses only sales and pricing data, while the other incorporates weather and epidemic context scores.

---

## Results at a Glance

| Model | Inputs | Error (MAPE) |
| :--- | :--- | :--- |
| **Baseline** | Inventory Level, Units Ordered, Price, Discount, Competitor Pricing | 43.51% |
| **Hybrid** | Inventory Level, Units Ordered, Price, Weather Score, Epidemic Score | 39.37% |

* The hybrid model's error is **4.14 percentage points lower** (a **9.5% relative reduction**).
* **Important Caveat:** Read these findings with caution as preliminary evidence rather than a controlled test:
  * The hybrid model also drops *Discount* and *Competitor Pricing*, meaning performance gains cannot be exclusively attributed to the context scores alone.
  * The train/test split is random rather than chronological by date.
  * Results are derived from a single run.
  * A full discussion is available in the paper's **Limitations** section.

---

## Repository Structure

```text
├── data/
│   ├── raw/
│   │   └── demand_forecasting.csv       # Original dataset (76,000 records)[cite: 5]
│   └── processed/
│       └── demand_forecasting_hybrid.csv # Processed dataset with context score columns
├── src/
│   ├── features/
│   │   └── create_hybrid_features.py    # Maps weather/epidemic categories to numeric scores[cite: 9]
│   └── models/
│       ├── train_baseline.py            # Baseline Random Forest model trainer[cite: 11]
│       └── train_hybrid.py              # Hybrid Random Forest model trainer[cite: 10]
├── experiments/
│   ├── analyze.py                       # Early exploratory HistGradientBoosting script[cite: 8]
│   └── train_simple.py                  # Early 3-feature exploratory script[cite: 7]
├── paper/
│   └── main.tex                         # LaTeX source code for the research paper[cite: 6]
├── generate_paper.py                    # Script to compile project summary report PDF
├── requirements.txt                     # Python dependencies
└── README.md
