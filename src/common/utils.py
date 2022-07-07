import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Union

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import streamlit as st


@st.cache
def read_stats(csv_path: Union[Path, str]) -> pd.DataFrame:
    return pd.read_csv(csv_path, keep_default_na=False)


def read_content(file_path: Union[Path, str]) -> str:
    with open(file_path, 'r') as file:
        return file.read()


@st.cache
def merge_stats(stats: List[pd.DataFrame], *, index: str, values: List[str]) -> pd.DataFrame:
    """
    Merge tables with statistics, summarizing all values having the same index.

    :param stats: List of tables with statistics that need to be merged.
    :param index: Field for which the values are to be summed.
    :param values: Fields that need to be summed up.

    :return: Table with merged statistics.
    """
    merged_stats = pd.concat(stats)
    merged_stats = merged_stats.pivot_table(index=index, values=values, aggfunc='sum')
    merged_stats.reset_index(inplace=True)
    return merged_stats


@st.cache
def get_stats_by_name(stats_path: Union[Path, str]) -> Dict[str, pd.DataFrame]:
    """
    Get all tables with statistics by file name.

    :param stats_path: The path to the folder with the statistics files.

    :return: Dictionary with statistics by file name.
    """
    file_names = os.listdir(stats_path)

    stats_by_name = {}
    for name in file_names:
        stats_by_name[re.sub(r'\.csv$', '', name)] = read_stats(stats_path / name)

    return stats_by_name


def get_bar_plot(
    stats: pd.DataFrame,
    *,
    x: str,
    y: Union[str, List[str]],
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    sort_by: Optional[Union[str, List[str]]] = None,
    color: Optional[str] = None,
    barmode: str = 'stack',  # Literal['stack', 'group', 'overlay', 'relative']
    bars_count: Optional[int] = None,
    bars_ignore: Optional[Set[str]] = None,
    bars_select: Optional[Set[str]] = None,
) -> go.Figure:
    """
    Visualize statistics as a bar chart.

    :param stats: Dataframe with statistics that need to be visualized.
    :param x: Column name in 'stats'.
    :param y: Column name or list of column names in 'stats'.
    :param x_title: X-axis title.
    :param y_title: Y-axis title.
    :param sort_by: Name or list of names to sort by.
    :param barmode: One of 'stack', 'group', 'overlay' or 'relative'.
    :param color: The name of the column in 'stats' by which you want to group the statistics.
    :param bars_count: Number of bars to show from start in sorted by count order.
    :param bars_ignore: Ignore bars with names start with one from this set.
    :param bars_select: Select bars with names start with one from this set.

    :return: Bar chart plotted according to the passed parameters.
    """
    if sort_by is None:
        sort_by = y

    df = stats.sort_values(by=sort_by, ascending=False)

    if bars_ignore is not None:
        df = df[df[x].apply(lambda x_value: not any(x_value.startswith(bar_ignore) for bar_ignore in bars_ignore))]

    if bars_select is not None:
        df = df[df[x].apply(lambda x_value: any(x_value.startswith(bar_select) for bar_select in bars_select))]

    if bars_count is not None:
        df = df[:bars_count]

    fig = px.bar(df, x=x, y=y, color=color, barmode=barmode)
    fig.update_layout(xaxis_categoryorder='total descending')

    if x_title is not None:
        fig.update_xaxes(title=x_title)

    if y_title is not None:
        fig.update_yaxes(title=y_title)

    return fig
