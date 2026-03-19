"""Core package for the Python Retail analytics project."""

from .data_io import REQUIRED_COLUMNS, dataset_profile, load_retail_dataset
from .plots import barplot, lineplot, pie_chart
from .transforms import (
    top_cities_by_sales,
    total_sales_by_order_date,
    total_sales_by_segment,
    total_sales_by_segment_year,
    total_sales_by_state,
)

__all__ = [
    "REQUIRED_COLUMNS",
    "barplot",
    "dataset_profile",
    "lineplot",
    "load_retail_dataset",
    "pie_chart",
    "top_cities_by_sales",
    "total_sales_by_order_date",
    "total_sales_by_segment",
    "total_sales_by_segment_year",
    "total_sales_by_state",
]
