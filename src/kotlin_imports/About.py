import sys
from pathlib import Path

sys.path.append('')
sys.path.append('../..')

from src.common.utils import read_content

import streamlit as st

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Imports', layout='wide')
    st.markdown(read_content(Path(__file__).parent / 'README.md'))
