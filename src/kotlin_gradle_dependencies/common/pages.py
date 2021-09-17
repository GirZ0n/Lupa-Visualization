import pandas as pd
import streamlit as st

from src.common.fragments import show_bar_plot_with_config
from src.kotlin_gradle_dependencies.common.column_name import ColumnName


def show_page(
    *,
    title: str,
    description: str,
    full_name_stats: pd.DataFrame,
    groups_stats: pd.DataFrame,
    config_stats: pd.DataFrame,
    key: str,
):
    st.title(title)

    st.markdown(description)

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies *groupId:artifactId*',
        df=full_name_stats,
        x_axis=ColumnName.GROUP_ID_ARTIFACT_ID.value,
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{key}_full_name_stats',
    )

    columns_to_show = full_name_stats.columns.to_list()
    columns_to_show.remove(ColumnName.GROUP_ID_ARTIFACT_ID.value)
    columns_to_show.remove(ColumnName.COUNT.value)

    show_bar_plot_with_config(
        header='The occurrence of gradle dependencies *groupId:artifactId* with configuration',
        df=full_name_stats,
        x_axis=ColumnName.GROUP_ID_ARTIFACT_ID.value,
        y_axis=columns_to_show,
        y_title='Count',
        sort_by=ColumnName.COUNT.value,
        key=f'{key}_full_name_multi_stats',
    )

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies *groupId*',
        df=groups_stats,
        x_axis=ColumnName.GROUP_ID.value,
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{key}_group_stats',
    )

    columns_to_show = groups_stats.columns.to_list()
    columns_to_show.remove(ColumnName.GROUP_ID.value)
    columns_to_show.remove(ColumnName.COUNT.value)

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies *groupId* with configuration',
        df=groups_stats,
        x_axis=ColumnName.GROUP_ID.value,
        y_axis=columns_to_show,
        y_title='Count',
        sort_by=ColumnName.COUNT.value,
        key=f'{key}_group_multi_stats',
    )

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies configuration',
        df=config_stats,
        x_axis=ColumnName.CONFIG_NAME.value,
        x_title='Configuration',
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{key}_config_stats',
    )
