import sys

import streamlit as st

sys.path.append('')
sys.path.append('../..')

from src.kotlin_imports.pages import PAGE_MAP


def main():
    st.set_page_config(page_title='Kotlin Imports', layout='wide')

    with st.sidebar:
        st.title('Kotlin Imports')
        page_name = st.radio('Select page', PAGE_MAP.keys())

        with st.expander('Glossary'):
            st.markdown('`import com.google.gson.Gson` - *import directive*')
            st.markdown('`"com.google.gson.Gson"` - *import fully qualified name*')

    PAGE_MAP[page_name].show()


if __name__ == "__main__":
    main()
