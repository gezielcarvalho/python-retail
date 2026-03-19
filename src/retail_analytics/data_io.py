"""Data loading and dataset profiling helpers."""

from pathlib import Path

import pandas as pd

from .paths import DEFAULT_DATASET_PATH

REQUIRED_COLUMNS = (
    "OrderId",
    "OrderDate",
    "CustomerId",
    "Segment",
    "Country",
    "City",
    "State",
    "ProductId",
    "Category",
    "SubCategory",
    "TotalOrderValue",
)


def load_retail_dataset(csv_path: Path | str = DEFAULT_DATASET_PATH) -> pd.DataFrame:
    """Load the retail dataset and enforce the expected schema."""
    dataset_path = Path(csv_path)
    dataframe = pd.read_csv(dataset_path)

    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(dataframe.columns))
    if missing_columns:
        missing_text = ", ".join(missing_columns)
        raise ValueError(f"Missing required columns: {missing_text}")

    dataframe = dataframe.copy()
    dataframe["OrderDate"] = pd.to_datetime(dataframe["OrderDate"], dayfirst=True, errors="raise")

    return dataframe


def dataset_profile(dataframe: pd.DataFrame) -> dict[str, int | str]:
    """Return high-level metrics that describe the dataset."""
    if dataframe.empty:
        return {
            "records": 0,
            "columns": dataframe.shape[1],
            "segments": 0,
            "cities": 0,
            "states": 0,
            "categories": 0,
            "subcategories": 0,
            "date_start": "N/A",
            "date_end": "N/A",
        }

    order_dates = pd.to_datetime(dataframe["OrderDate"], dayfirst=True, errors="coerce")

    return {
        "records": int(dataframe.shape[0]),
        "columns": int(dataframe.shape[1]),
        "segments": int(dataframe["Segment"].nunique(dropna=True)),
        "cities": int(dataframe["City"].nunique(dropna=True)),
        "states": int(dataframe["State"].nunique(dropna=True)),
        "categories": int(dataframe["Category"].nunique(dropna=True)),
        "subcategories": int(dataframe["SubCategory"].nunique(dropna=True)),
        "date_start": order_dates.min().date().isoformat(),
        "date_end": order_dates.max().date().isoformat(),
    }
