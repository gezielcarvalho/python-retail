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


def lineplot(
    dataframe: DataFrame,
    x: str,
    y: str,
    title: str,
    figsize: tuple[int, int] = (12, 6),
    hue: str | None = None,
) -> plt.Axes:
    """Create a line plot for time series or trends."""
    _, axis = plt.subplots(figsize=figsize)
    sns.lineplot(data=dataframe, x=x, y=y, hue=hue, ax=axis)
    axis.set_title(title)
    return axis


def pie_chart(
    dataframe: DataFrame,
    values: str,
    labels: str,
    title: str,
    figsize: tuple[int, int] = (8, 6),
    autopct: str = "%1.1f%%",
) -> plt.Axes:
    """Create a pie chart for proportions."""
    _, axis = plt.subplots(figsize=figsize)
    axis.pie(
        dataframe[values],
        labels=dataframe[labels],
        autopct=autopct,
        startangle=140,
    )
    axis.set_title(title)
    axis.axis("equal")  # Equal aspect ratio
    return axis
