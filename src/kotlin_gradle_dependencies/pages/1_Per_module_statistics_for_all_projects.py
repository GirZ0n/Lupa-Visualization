from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.common.pages import show_page

import streamlit as st

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Gradle Dependencies', layout='wide')

    full_name_stats = read_stats(DATA_FOLDER / 'all' / 'full_name_stats.csv')
    group_stats = read_stats(DATA_FOLDER / 'all' / 'groups_stats.csv')
    config_stats = read_stats(DATA_FOLDER / 'all' / 'config_stats.csv')

    show_page(
        title='Per module statistics for all projects',
        description=(
            'We mined all gradle dependencies from build.gradle/build.gradle.kts files '
            'from project modules in the dataset using PSI.'
        ),
        full_name_stats=full_name_stats,
        groups_stats=group_stats,
        config_stats=config_stats,
        key='per_module_stats_all',
    )
