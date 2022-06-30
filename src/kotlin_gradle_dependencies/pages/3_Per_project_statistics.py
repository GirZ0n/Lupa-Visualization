from src.common.fragments import show_bar_plot_with_config
from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.common.column_name import ColumnName

import streamlit as st

_KEY = 'per_project_stats'


if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Gradle Dependencies', layout='wide')

    unique_full_name_stats_all = read_stats(DATA_FOLDER / 'all' / 'unique_full_name_stats.csv')
    unique_full_name_stats_without_android = read_stats(DATA_FOLDER / 'exclude_android' / 'unique_full_name_stats.csv')

    st.title('Per project statistics')

    st.markdown(
        '"Per module" statistics can skew the rating of Gradle dependency due to the referencing '
        'in many modules in a project. So, the following plots show Gradle dependencies statistics '
        'for projects dependencies sets (unique in project).'
    )

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies *groupId:artifactId*',
        description='For all projects',
        df=unique_full_name_stats_all,
        x_axis=ColumnName.GROUP_ID_ARTIFACT_ID.value,
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{_KEY}_all',
    )

    show_bar_plot_with_config(
        header='The occurrence of Gradle dependencies *groupId:artifactId*',
        description='Without Android projects',
        df=unique_full_name_stats_without_android,
        x_axis=ColumnName.GROUP_ID_ARTIFACT_ID.value,
        y_axis=ColumnName.COUNT.value,
        y_title='Count',
        key=f'{_KEY}_without_android',
    )
