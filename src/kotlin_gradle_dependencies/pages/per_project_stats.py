from src.common.fragments import show_bar_plot_with_config
from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.pages import Page

import streamlit as st


class PerProjectStats(Page):
    title = 'Per project statistics'
    description = (
        '"Per module" statistics can skew the rating of Gradle dependency due to the referencing '
        'in many modules in a project. So, the following plots show Gradle dependencies statistics '
        'for projects dependencies sets (unique in project).'
    )
    unique_full_name_stats_all_df_path = DATA_FOLDER / 'all' / 'unique_full_name_stats.csv'
    unique_full_name_stats_without_android_df_path = DATA_FOLDER / 'exclude_android' / 'unique_full_name_stats.csv'
    key = 'per_project_stats'

    @classmethod
    def show(cls):
        unique_full_name_stats_all = read_stats(cls.unique_full_name_stats_all_df_path)
        unique_full_name_stats_without_android = read_stats(cls.unique_full_name_stats_without_android_df_path)

        st.title(cls.title)

        st.markdown(cls.description)

        show_bar_plot_with_config(
            header='The occurrence of Gradle dependencies *groupId:artifactId*',
            description='For all projects',
            df=unique_full_name_stats_all,
            x_axis='groupId:artifactId',
            y_axis='count',
            y_title='Count',
            key=f'{cls.key}_all',
        )

        show_bar_plot_with_config(
            header='The occurrence of Gradle dependencies *groupId:artifactId*',
            description='Without Android projects',
            df=unique_full_name_stats_without_android,
            x_axis='groupId:artifactId',
            y_axis='count',
            y_title='Count',
            key=f'{cls.key}_without_android',
        )
