from src.common.utils import get_stats_by_name
from src.python_call_expressions import DATA_FOLDER
from src.python_call_expressions.common.pages import show_page

import streamlit as st


if __name__ == '__main__':
    st.set_page_config(page_title='Python Call Expressions', layout='wide')

    show_page(
        title='Statistics without Python Standard Library and Python builtins',
        description=(
            "We mined all *call expressions' fully qualified names* from each Python file "
            'in the dataset using PSI (see `/resources/python_call_expressions/data/call_expressions_data.csv`).'
        ),
        stats_by_version=get_stats_by_name(DATA_FOLDER / 'exclude_stdlib_and_builtins'),
        key='exclude_stdlib_and_builtins',
    )
