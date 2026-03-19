from retail_analytics.data_io import REQUIRED_COLUMNS, dataset_profile, load_retail_dataset


def test_load_retail_dataset_has_expected_columns() -> None:
    dataframe = load_retail_dataset()

    assert list(dataframe.columns) == list(REQUIRED_COLUMNS)
    assert dataframe["OrderDate"].dtype.kind == "M"


def test_dataset_profile_has_basic_metrics() -> None:
    dataframe = load_retail_dataset()
    profile = dataset_profile(dataframe)

    assert profile["records"] == 9700
    assert profile["columns"] == len(REQUIRED_COLUMNS)
    assert profile["segments"] >= 1
    assert profile["categories"] >= 1
