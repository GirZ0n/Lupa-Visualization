from typing import Dict

import pandas as pd
import streamlit as st

from src.common.fragments import choose_values, show_bar_plot_with_config
from src.common.utils import merge_stats
from src.python_call_expressions.common.column_name import ColumnName


def show_page(
    *,
    title: str,
    description: str,
    stats_by_version: Dict[str, pd.DataFrame],
    key: str,
):
    st.title(title)

    st.markdown(description)

    chosen_versions = choose_values(
        set(stats_by_version.keys()),
        multiselect_label='Python versions:',
        nothing_selected_error='You must select at least one version of the language.',
        key=f'{key}_python_versions',
    )

    stats = [stats for version, stats in stats_by_version.items() if version in chosen_versions]

    values = stats[0].columns.tolist()
    values.remove(ColumnName.FQ_NAME.value)
    stats = merge_stats(stats, index=ColumnName.FQ_NAME.value, values=values)

    categories = stats.columns.tolist()
    categories.remove(ColumnName.FQ_NAME.value)
    categories.remove(ColumnName.TOTAL.value)

    fq_name = st.text_input('Fully qualified name:', key=f'{key}_fq_name_input')
    if fq_name != '':
        stats = stats[stats[ColumnName.FQ_NAME.value].str.startswith(fq_name)]

    show_bar_plot_with_config(
        header='The occurrence of call expressions FQ names',
        description='The occurrence of the mined call expressions / fully qualified names from projects.',
        df=stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Expression name',
        y_axis=ColumnName.TOTAL.value,
        y_title='Number of projects',
        key=f'{key}_call_expressions_total_stats',
    )

    show_bar_plot_with_config(
        header='The occurrence of call expressions FQ names by category',
        description='The occurrence of the mined call expressions / fully qualified names from projects.',
        df=stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Expression name',
        y_axis=categories,
        y_title='Number of projects',
        barmode='group',
        sort_by=ColumnName.TOTAL.value,
        key=f'{key}_call_expressions_stats_by_category',
    )
