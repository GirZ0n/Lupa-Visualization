from typing import Dict

import streamlit as st

from src.common.fragments import show_bar_plot_with_config


def show_page(
    *,
    title: str,
    description: str,
    import_stats: Dict[str, int],
    import_stats_by_package: Dict[str, int],
    key: str,
):
    st.title(title)

    st.markdown(description)

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names',
        description='The occurrence of the mined import directives / fully qualified names from projects.',
        df=import_stats,
        x_axis='import name',
        y_axis='count',
        key=f'{key}_import_stats',
    )

    show_bar_plot_with_config(
        header='The occurrence of imports FQ names grouped by the package name',
        description=(
            'To get packages, we built a tree of FQ names and detected package names based on several configurable '
            'heuristics (number of child nodes, number of leaves, occurrence, depth, size of the subtree).'
        ),
        df=import_stats_by_package,
        x_axis='package name',
        y_axis='count',
        key=f'{key}_import_stats_by_package',
    )
