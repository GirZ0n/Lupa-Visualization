from src.common.utils import get_stats_by_name
from src.python_imports import DATA_FOLDER
from src.python_imports.common.pages import show_page

import streamlit as st


if __name__ == '__main__':
    st.set_page_config(page_title='Python Imports', layout='wide')

    show_page(
        title='Statistics without Python Standard Library',
        description=(
            "We mined all *imports' fully qualified names* from each Python file "
            'in the dataset using PSI (see `/resources/python_imports/data/import_data.csv`).'
        ),
        import_stats_by_version=get_stats_by_name(DATA_FOLDER / 'exclude_stdlib' / 'import_stats'),
        package_stats_by_version=get_stats_by_name(DATA_FOLDER / 'exclude_stdlib' / 'import_stats_by_package'),
        key='exclude_stdlib',
    )
