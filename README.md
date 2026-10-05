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

## Quick Start

```bash
git clone [https://github.com/sidrashake789/demand-forecasting-research.git](https://github.com/sidrashake789/demand-forecasting-research.git)
cd demand-forecasting-research

pip install -r requirements.txt

python src/models/train_baseline.py   # Prints 43.51%
python src/models/train_hybrid.py     # Prints 39.37%
