from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.common.pages import show_page

import streamlit as st

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Gradle Dependencies', layout='wide')

    full_name_stats = read_stats(DATA_FOLDER / 'exclude_android' / 'full_name_stats.csv')
    group_stats = read_stats(DATA_FOLDER / 'exclude_android' / 'groups_stats.csv')
    config_stats = read_stats(DATA_FOLDER / 'exclude_android' / 'config_stats.csv')

    show_page(
        title='Per module statistics without Android projects',
        description=(
            'We consider a project to be entirely android if it contains **`com.android.tools.build`** dependency '
            'in the root build gradle file. After the filtering of Android repositories, ~4000 projects remained.'
        ),
        full_name_stats=full_name_stats,
        groups_stats=group_stats,
        config_stats=config_stats,
        key='per_module_stats_exclude_android',
    )
