from src.common.utils import read_stats
from src.kotlin_imports import DATA_FOLDER
from src.kotlin_imports.common.pages import show_page

import streamlit as st

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Imports', layout='wide')

    import_stats = read_stats(DATA_FOLDER / 'exclude_android' / 'import_stats.csv')
    import_stats_by_package = read_stats(DATA_FOLDER / 'exclude_android' / 'import_stats_by_package.csv')

    show_page(
        title='Statistics without Android projects',
        description=(
            'We consider a project to be entirely android '
            'if it contains **`com.android.tools.build`** dependency in the root build gradle file. '
            'After the filtering of Android repositories, ~4000 projects remained.'
        ),
        import_stats=import_stats,
        import_stats_by_package=import_stats_by_package,
        key='exclude_android',
    )
