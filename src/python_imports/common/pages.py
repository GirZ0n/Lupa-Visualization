from typing import Dict

import pandas as pd
import streamlit as st

from src.common.fragments import choose_values, show_bar_plot_with_config
from src.common.utils import merge_stats
from src.python_imports.common.column_name import ColumnName


def show_page(
    *,
    title: str,
    description: str,
    import_stats_by_version: Dict[str, pd.DataFrame],
    package_stats_by_version: Dict[str, pd.DataFrame],
    key: str,
):
    st.title(title)

    st.markdown(description)

    versions = set(import_stats_by_version.keys())
    versions |= package_stats_by_version.keys()

    chosen_versions = choose_values(
        versions,
        multiselect_label='Python versions:',
        nothing_selected_error='You must select at least one version of the language.',
        key=f'{key}_python_versions',
    )

    import_stats = [stats for version, stats in import_stats_by_version.items() if version in chosen_versions]
    import_stats = merge_stats(import_stats, index=ColumnName.FQ_NAME.value, values=[ColumnName.COUNT.value])

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names',
        description='The occurrence of the mined import directives / fully qualified names from projects.',
        df=import_stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Import name',
        y_axis=ColumnName.COUNT.value,
        y_title='Number of projects',
        key=f'{key}_import_stats',
    )

    package_stats = [stats for version, stats in package_stats_by_version.items() if version in chosen_versions]
    package_stats = merge_stats(package_stats, index=ColumnName.FQ_NAME.value, values=[ColumnName.COUNT.value])

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names grouped by the package name',
        description=(
            'To get packages, we built a tree of FQ names and detected package names based on several configurable '
            'heuristics (number of child nodes, number of leaves, occurrence, depth, size of the subtree).'
        ),
        df=package_stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Package name',
        y_axis=ColumnName.COUNT.value,
        y_title='Number of imports',
        key=f'{key}_import_stats_by_package',
    )
