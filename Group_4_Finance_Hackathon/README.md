# World Happiness Report Analysis
### Solavise Women in Data (SWID) Programme — Week 8 Hackathon
**Group 4 | Finance & Economics**

---

## Project Overview

Every year, the World Happiness Report asks hundreds of thousands of people
around the world how satisfied they are with their lives. The answers reveal
a striking divide — some countries consistently score near 8 out of 10,
while others barely reach 3.

This project analyses **9 years of World Happiness Report data (2015–2023)**
across **171 countries and 11 regions** to answer one central question:

> **What makes a country happy — and can we predict it from economic and social data?**

---

## Repository Contents

| File | Description |
|---|---|
| `Group_4_Finance_Hackathon.ipynb` | Main Jupyter Notebook — full analysis |
| `WHR_15_23.csv` | Raw dataset (World Happiness Report 2015–2023) |
| `clean_WHR_15_23.csv` | Cleaned dataset after preprocessing |
| `MultiYear_Trend_Visualization.png` | Happiness trends over time (top 5 vs bottom 5) |
| `chart5_feature_importance.png` | Random Forest feature importance chart |

---

## Dataset

- **Source:** World Happiness Report (Kaggle)
- **File:** `WHR_15_23.csv`
- **Rows:** 1,367 (before cleaning) → 1,363 (after removing duplicates)
- **Years covered:** 2015 – 2023
- **Countries:** 171
- **Regions:** 11

### Columns

| Column | Description |
|---|---|
| `country` | Country name |
| `region` | World region |
| `year` | Survey year |
| `happiness_score` | National happiness score (0–10) |
| `gdp_per_capita` | Log GDP per capita (economic output per person) |
| `social_support` | Perceived social support score |
| `healthy_life_expectancy` | Healthy life expectancy at birth |
| `freedom_to_make_life_choices` | Freedom to make life decisions score |
| `generosity` | National generosity score |

---

## Skills Demonstrated

| Skill | What We Did |
|---|---|
| **Data Cleaning** | Handled 1 missing value, converted 9 zeros to NaN, fixed country name inconsistency, removed 4 duplicate rows, rounded to 3 decimal places, sorted alphabetically |
| **NumPy** | Used `np.diff()` for year-on-year change, `np.mean()`, `np.median()`, `np.std()`, `np.max()`, `np.min()` for statistical summaries |
| **Pandas** | `groupby`, `agg`, filtering, merging, `sort_values`, `drop_duplicates`, `fillna`, `replace` |
| **Visualisation** | 6 charts — bar charts, line chart, heatmap, scatter plot using Matplotlib & Seaborn |
| **Machine Learning** | Linear Regression (baseline) → Random Forest (improvement), evaluated with RMSE and R² |
| **Storytelling** | Clear narrative with beginning, middle, end, key findings, and actionable recommendations |

---

## Data Cleaning Summary

| Issue Found | Fix Applied |
|---|---|
| 1 missing value (`healthy_life_expectancy` — State of Palestine 2023) | Filled with column mean |
| 9 zeros across 5 numeric columns (not valid values) | Converted to NaN, filled with column mean |
| Country name inconsistency (`Somaliland region` vs `Somaliland Region`) | Standardised capitalisation |
| 4 duplicate rows (Cyprus appeared twice in 2018 and 2019) | Kept first occurrence |
| Long decimal places | Rounded all numeric values to 3 decimal places |
| Unsorted data | Sorted alphabetically by country |

---

## Key Findings

**1. The happiness divide is wide and consistent**
Finland ranked happiest (avg score: **7.663**) across all 9 years.
Afghanistan ranked least happy (avg score: **2.991**).
The gap between them is nearly 5 points on a 10-point scale.

**2. Region matters enormously**
North America & ANZ led all regions (**7.176**).
Sub-Saharan Africa scored lowest (**4.289**).
Every indicator — GDP, life expectancy, social support — was dramatically
higher in the top region than the bottom.

**3. GDP is the strongest predictor**
Correlation with happiness: GDP **(0.72)**, Life Expectancy **(0.68)**,
Social Support **(0.62)**, Freedom **(0.55)**, Generosity **(0.08)**.
Generosity showed almost no relationship with national happiness.

**4. The world is slowly getting happier**
Global average rose from **5.376** in 2015 to **5.554** in 2022,
though it dipped slightly in 2023. Progress is real but uneven.

**5. Romania improved most, Lebanon declined most**
Romania gained **+0.183 points per year** on average.
Lebanon fell **−0.306 points per year**, reflecting its ongoing crisis.

---

## Machine Learning Results

We built two models to predict happiness score from the 5 indicators.

| Model | RMSE | R² | Notes |
|---|---|---|---|
| Linear Regression | 0.590 | 0.718 | Baseline — simple, interpretable |
| Random Forest | 0.521 | 0.780 | Improvement — 8.4% better RMSE |

**Selected model: Random Forest**
It explains **78% of the variation** in happiness scores using just 5 indicators,
with an average prediction error of only **0.521 points**.

### Feature Importance (Random Forest)

| Factor | Importance |
|---|---|
| GDP per Capita | 52.5% |
| Life Expectancy | 18.9% |
| Freedom | 12.7% |
| Social Support | 9.2% |
| Generosity | 6.7% |

**GDP per capita accounts for over half of what predicts happiness.**

---

## Recommendations

**1. Invest in economic development and health together**
Sub-Saharan Africa and South Asia score lowest on both GDP and life
expectancy. These regions need policies that treat economic growth and
healthcare as a single package — because the data shows they reinforce
each other in building national happiness.

**2. Protect personal freedoms, especially during crises**
Freedom is the third most important predictor at 12.7%. Lebanon's
sharp decline (−0.306/yr) coincided with restricted freedoms during
its economic collapse. Governments that limit personal autonomy during
hard times compound the happiness cost of the crisis itself.

---

## How to Run This Notebook

### Option A — Google Colab (Recommended)
1. Open [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Open notebook → GitHub**
3. Paste this repository URL and open `Group_4_Finance_Hackathon.ipynb`
4. Click **Runtime → Run All**
5. Upload `WHR_15_23.csv` when prompted

### Option B — Run Locally
```bash
# Clone the repository
git clone https://github.com/YourUsername/SWID-Week8-Group4-Hackathon.git
cd SWID-Week8-Group4-Hackathon

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl

# Launch Jupyter
jupyter notebook Group_4_Finance_Hackathon.ipynb
```

---

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

All libraries are pre-installed in Google Colab — no setup needed.

---

## Group 4 Members

| Name | Role |
|---|---|
| *Vivian Ndung'u* | *Visualization* |
| *Faith Odhe* | *Machine learning* |
| *Beryl Akinyi* | *Storytelling* |
| *Ranila Liisone* | *Presentation slides* |

---

*Solavise Women in Data (SWID) Programme | Week 8 Hackathon | Group 4:)*
