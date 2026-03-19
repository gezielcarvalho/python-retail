"""Core package for the Python Retail analytics project."""

from .data_io import REQUIRED_COLUMNS, dataset_profile, load_retail_dataset
from .transforms import (
    total_sales_by_order_date,
    total_sales_by_segment,
    total_sales_by_segment_year,
    total_sales_by_state,
    top_cities_by_sales,
)

__all__ = [
    "REQUIRED_COLUMNS",
    "dataset_profile",
    "load_retail_dataset",
    "total_sales_by_order_date",
    "total_sales_by_segment",
    "total_sales_by_segment_year",
    "total_sales_by_state",
    "top_cities_by_sales",
]
