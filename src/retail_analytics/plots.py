"""Plotting helpers to keep notebooks focused on analysis narrative."""

import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def barplot(
    dataframe: DataFrame,
    x: str,
    y: str,
    title: str,
    figsize: tuple[int, int] = (12, 6),
    rotate_x: int = 0,
) -> plt.Axes:
    """Create a standard bar plot used across analysis notebooks."""
    _, axis = plt.subplots(figsize=figsize)
    sns.barplot(data=dataframe, x=x, y=y, ax=axis)
    axis.set_title(title)
    if rotate_x:
        axis.tick_params(axis="x", rotation=rotate_x)
    return axis
