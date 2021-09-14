import pandas as pd
import streamlit as st

from src.common.fragments import show_bar_plot_with_config
from src.kotlin_imports.common.column_name import ColumnName


def show_page(
    *,
    title: str,
    description: str,
    import_stats: pd.DataFrame,
    import_stats_by_package: pd.DataFrame,
    key: str,
):
    st.title(title)

    st.markdown(description)

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names',
        description='The occurrence of the mined import directives / fully qualified names from projects.',
        df=import_stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Import name',
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{key}_import_stats',
    )

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names grouped by the package name',
        description=(
            'To get packages, we built a tree of FQ names and detected package names based on several configurable '
            'heuristics (number of child nodes, number of leaves, occurrence, depth, size of the subtree).'
        ),
        df=import_stats_by_package,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Package name',
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{key}_import_stats_by_package',
    )
