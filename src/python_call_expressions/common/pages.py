import pandas as pd
import streamlit as st

from src.common.fragments import show_bar_plot_with_config
from src.python_call_expressions.common.column_name import ColumnName


def show_page(
    *,
    title: str,
    description: str,
    stats: pd.DataFrame,
    key: str,
):
    st.title(title)

    st.markdown(description)

    category_options = stats[ColumnName.CATEGORY.value].unique()

    chosen_categories = st.session_state.get(f'{key}_chosen_categories')
    if chosen_categories is None:
        st.session_state[f'{key}_chosen_categories'] = category_options
        chosen_categories = category_options

    categories = st.multiselect(
        'Categories:',
        options=category_options,
        default=chosen_categories,
        key=f'{key}_categories_multiselect',
    )

    fq_name = st.text_input('Fully qualified name:', key=f'{key}_fq_name_input')
    if fq_name != '':
        stats = stats[stats[ColumnName.FQ_NAME.value].str.startswith(fq_name)]

    stats = stats[stats[ColumnName.CATEGORY.value].isin(categories)]

    show_bar_plot_with_config(
        header='The occurrence of call expressions FQ names',
        description='The occurrence of the mined call expressions / fully qualified names from projects.',
        df=stats,
        x_axis=ColumnName.FQ_NAME.value,
        x_title='Expression name',
        y_axis=ColumnName.COUNT.value,
        y_title='Number of projects',
        color=ColumnName.CATEGORY.value,
        key=f'{key}_call_expressions_stats',
    )
