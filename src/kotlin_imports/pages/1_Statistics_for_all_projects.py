from src.common.utils import read_stats
from src.kotlin_imports import DATA_FOLDER
from src.kotlin_imports.common.pages import show_page

import streamlit as st

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Imports', layout='wide')

    import_stats = read_stats(DATA_FOLDER / 'all' / 'import_stats.csv')
    import_stats_by_package = read_stats(DATA_FOLDER / 'all' / 'import_stats_by_package.csv')

    show_page(
        title='Statistics for all projects',
        description=(
            "We mined all *imports' fully qualified names* from each Kotlin file "
            'in the dataset using PSI (see `./data/all/import_data.csv`).'
        ),
        import_stats=import_stats,
        import_stats_by_package=import_stats_by_package,
        key='all',
    )
