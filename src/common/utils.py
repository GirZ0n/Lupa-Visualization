from pathlib import Path
from typing import Dict, Set, Union

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


@st.cache
def read_stats(csv_path: Union[Path, str], *, x_label: str, y_label: str) -> Dict[str, int]:
    df = pd.read_csv(csv_path)
    return {row[x_label]: row[y_label] for _, row in df.iterrows()}


def get_bar_plot(
    stats: Dict[str, int],
    x: str,
    y: str,
    bars_count: int = None,
    bars_ignore: Set[str] = None,
    bars_select: Set[str] = None,
) -> go.Figure:
    """
    Method for statistics visualization as a bar chart
    :param stats: dict which for string value name stores it's statistics int or float value
    :param x: axis label with value names
    :param y: axis label for with values
    :param bars_count: number of bars to show from start in sorted by count order
    :param bars_ignore: ignore bars with names start with one from this set
    :param bars_select: select bars with names start with one from this set
    """

    df = pd.DataFrame.from_dict({x: stats.keys(), y: stats.values()})
    df = df.sort_values(by=[y], ascending=False)

    if bars_ignore is not None:
        df = df[df[x].apply(lambda x_value: not any(x_value.startswith(bar_ignore) for bar_ignore in bars_ignore))]

    if bars_select is not None:
        df = df[df[x].apply(lambda x_value: any(x_value.startswith(bar_select) for bar_select in bars_select))]

    if bars_count is not None:
        df = df[:bars_count]

    stats_df = pd.DataFrame({x: df[x].values, y: df[y].values})
    return px.bar(stats_df, x=x, y=y)

