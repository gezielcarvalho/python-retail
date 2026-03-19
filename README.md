# Python Retail Analytics

Notebook-based retail analysis project focused on business questions and visual storytelling with Python.

The repository contains exploratory data analysis (EDA) notebooks that answer 10 business questions on a US retail dataset, using pandas for data manipulation and matplotlib/seaborn for visualizations.

## Current Project Snapshot

What this project already demonstrates:

- Problem framing around business questions
- Practical use of pandas groupby and aggregations
- Chart building with matplotlib and seaborn
- Organized notebook-per-question workflow
- Exported visual artifacts in the images folder

## Dataset Profile

Source file: data/dataset.csv

- Records: 9700
- Columns: 11
- Date range: 03/01/2015 to 30/12/2018
- Segments: 3
- Cities: 528
- States: 49
- Categories: 3
- Subcategories: 17

Columns:

- OrderId
- OrderDate
- CustomerId
- Segment
- Country
- City
- State
- ProductId
- Category
- SubCategory
- TotalOrderValue

## Business Questions and Notebooks

| Question | Notebook | Visualization Output |
| --- | --- | --- |
| Q01. City with highest Office Supplies sales | Q01_HighestSalesValue.ipynb | - |
| Q02. Total sales by order date | Q02_TotalSalesByOrderDate.ipynb | images/q2_total_sales_per_date.png |
| Q03. Total sales by state | Q03_TotalSalesByState.ipynb | images/q3_total_sales_per_state.png |
| Q04. Top 10 cities by total sales | Q04_HighestSalesCities.ipynb | images/q4_top10_cities.png |
| Q05. Segment with highest total sales | Q05_SegmentHighestTotalSales.ipynb | images/q5_sales_per_segment.png |
| Q06. Total sales by segment and year | Q06_SegmentTotalPerYear.ipynb | images/q6_sales_per_segment_year.png |
| Q07. Sales eligible for 15% discount | Q07_Q08_CalculateDiscount.ipynb | images/q7_discounts.png |
| Q08. Average order value before and after discount | Q07_Q08_CalculateDiscount.ipynb | images/q8_discounts.png |
| Q09. Average sales by segment, year and month | Q09_AverageSalesSegment.ipynb | images/q9_AverageSales.png |
| Q10. Total sales by category/subcategory (Top 12) | Q10_TotalSalesByCategory.ipynb | images/q10_TotalSalesTop12.png |

## Repository Structure

```text
.
|-- data/
|   `-- dataset.csv
|-- images/
|   `-- *.png
|-- Q01_HighestSalesValue.ipynb
|-- Q02_TotalSalesByOrderDate.ipynb
|-- Q03_TotalSalesByState.ipynb
|-- Q04_HighestSalesCities.ipynb
|-- Q05_SegmentHighestTotalSales.ipynb
|-- Q06_SegmentTotalPerYear.ipynb
|-- Q07_Q08_CalculateDiscount.ipynb
|-- Q09_AverageSalesSegment.ipynb
|-- Q10_TotalSalesByCategory.ipynb
|-- README.md
`-- ROADMAP.md
```

## How to Run

1. Create and activate a virtual environment.
2. Install dependencies.
3. Start Jupyter Lab (or Jupyter Notebook).
4. Open the notebooks and run cells in order.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn jupyterlab
jupyter lab
```

## Analysis Notes

- Notebooks are readable and objective, but there is repeated setup logic across files (imports, loading, basic checks).
- Most analysis is concentrated in notebook code; there is no reusable Python package yet.
- There are no automated tests, formatting/linting, or CI checks in the current version.

These points are normal for an EDA-first project, and they are exactly where the next evolution can strongly highlight Python engineering skills.

## Evolution Plan

The detailed step-by-step evolution plan is in ROADMAP.md.

High-level direction:

1. Refactor repeated notebook logic into reusable Python modules.
2. Add tests, linting, type hints, and CI automation.
3. Expand analytics with more advanced techniques (RFM, cohort, forecasting).
4. Productize outcomes with a CLI and an interactive dashboard.

Following this path turns the project from notebook-only analysis into a portfolio-grade Python analytics application.
