# Hybrid Demand Forecasting

**Does adding weather and epidemic information make a retail demand forecast more accurate?**

This project compares two Random Forest models that predict how many units a store sells. One uses only sales and pricing data. The other also gets a weather score and an epidemic score.

## Results at a glance

| Model | Inputs | Error (MAPE) |
| --- | --- | --- |
| Baseline | Inventory Level, Units Ordered, Price, Discount, Competitor Pricing | 43.51% |
| Hybrid | Inventory Level, Units Ordered, Price, **Weather Score, Epidemic Score** | **39.37%** |

The hybrid model's error is **4.14 percentage points lower** (a 9.5% relative reduction).

**Read this with caution.** This is preliminary evidence, not a controlled test:
- The hybrid model also drops Discount and Competitor Pricing, so the gain can't be credited to the context scores alone.
- The train/test split is random, not by date.
- Results come from a single run.

The full discussion is in the paper's Limitations section.

## Quick start

```bash
git clone https://github.com/sidrashake789/demand-forecasting-research.git
cd demand-forecasting-research
pip install -r requirements.txt

python src/models/train_baseline.py   # prints 43.51%
python src/models/train_hybrid.py     # prints 39.37%
```

Scripts can be run from any folder.

## How it works

1. **Build the context scores** (`src/features/create_hybrid_features.py`). Weather and epidemic labels are turned into numbers using a hand-written lookup. This step is optional, because the processed file is already included.
2. **Train the baseline** (`src/models/train_baseline.py`) on the raw data.
3. **Train the hybrid** (`src/models/train_hybrid.py`) on the data with the scores.

**The scores**

| Field | Value | Score |
| --- | --- | --- |
| Weather | Sunny / Cloudy / Rainy / Snowy | 1.2 / 1.0 / 0.9 / 0.8 |
| Epidemic | 0 (none) / 1 (flagged) | 1.0 / 0.6 |

**Shared settings**
- Random Forest Regressor, 100 trees, `random_state=42`
- 80/20 train/test split (60,800 / 15,200 rows), identical for both models
- Error is a modified MAPE that adds 1 to the denominator, so rows with zero sales don't break the metric

## Repository structure

```
.
├── data/
│   ├── raw/                  original Kaggle dataset
│   └── processed/            dataset with the context scores added
├── src/
│   ├── features/             builds the weather and epidemic scores
│   └── models/               baseline and hybrid training scripts
├── experiments/              early exploratory scripts, kept for reference
├── scripts/                  data checks and dataset statistics
├── paper/                    LaTeX paper, references, summary-PDF script
├── requirements
│   ├── requirements/
└── README.md
```

## Data

The raw dataset was downloaded from Kaggle. It has **76,000 rows**: 5 stores × 20 products × 760 days (1 Jan 2022 to 30 Jan 2024), with no missing values.

| Group | Columns |
| --- | --- |
| Identifiers | Date, Store ID, Product ID |
| Descriptors | Category, Region |
| Sales and stock | Units Sold (the target), Inventory Level, Units Ordered |
| Pricing | Price, Discount, Competitor Pricing, Promotion |
| Context | Weather Condition, Epidemic, Seasonality |
| Other | Demand |

Only the columns named in the results table above are used by the models. To print dataset statistics, run `python scripts/describe_data.py`.

## Paper

The paper's LaTeX source is in `paper/`. To build it:

```bash
cd paper
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

This produces `paper/main.pdf`. Separately, `python paper/generate_paper.py` builds a short summary PDF.
