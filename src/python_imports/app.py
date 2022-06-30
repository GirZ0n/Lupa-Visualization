import sys

sys.path.append('')
sys.path.append('../..')

from src.python_imports.pages import PAGE_MAP

import streamlit as st


def main():
    st.set_page_config(page_title='Python Imports', layout='wide')

    with st.sidebar:
        st.title('Python Imports')
        page_name = st.radio('Select page', PAGE_MAP.keys())

        with st.expander('Glossary'):
            st.markdown('`import typing.List` - *import directive*')
            st.markdown('`"typing.List"` - *import fully qualified name*')

    PAGE_MAP[page_name].show()


if __name__ == '__main__':
    main()
