"""Reusable transformations used across business-question analyses."""

import pandas as pd


TOTAL_SALES_COLUMN = "TotalOrderValue"


def total_sales_by_order_date(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by date in ascending time order."""
    result = (
        dataframe.groupby("OrderDate", as_index=False)[TOTAL_SALES_COLUMN]
        .sum()
        .sort_values("OrderDate")
    )
    return result.reset_index(drop=True)


def total_sales_by_state(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales per state in descending sales order."""
    result = (
        dataframe.groupby("State", as_index=False)[TOTAL_SALES_COLUMN]
        .sum()
        .sort_values(TOTAL_SALES_COLUMN, ascending=False)
    )
    return result.reset_index(drop=True)


def top_cities_by_sales(dataframe: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Return the top cities by total sales."""
    if top_n <= 0:
        raise ValueError("top_n must be greater than zero")

    result = (
        dataframe.groupby("City", as_index=False)[TOTAL_SALES_COLUMN]
        .sum()
        .sort_values(TOTAL_SALES_COLUMN, ascending=False)
        .head(top_n)
    )
    return result.reset_index(drop=True)


def total_sales_by_segment(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales per customer segment."""
    result = (
        dataframe.groupby("Segment", as_index=False)[TOTAL_SALES_COLUMN]
        .sum()
        .sort_values(TOTAL_SALES_COLUMN, ascending=False)
    )
    return result.reset_index(drop=True)


def total_sales_by_segment_year(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by year and segment."""
    working = dataframe.copy()
    if "Year" not in working.columns:
        working["Year"] = pd.to_datetime(working["OrderDate"], dayfirst=True, errors="raise").dt.year

    result = (
        working.groupby(["Year", "Segment"], as_index=False)[TOTAL_SALES_COLUMN]
        .sum()
        .sort_values(["Year", "Segment"])
    )
    return result.reset_index(drop=True)
