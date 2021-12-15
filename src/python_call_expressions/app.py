import sys

import streamlit as st

sys.path.append('')
sys.path.append('../..')

from src.python_call_expressions.pages import PAGE_MAP


def main():
    st.set_page_config(page_title='Python Call Expressions', layout='wide')

    with st.sidebar:
        st.title('Python Call Expressions')
        page_name = st.radio('Select page', PAGE_MAP.keys())

        with st.expander('Glossary'):
            st.markdown('`np.zeros()` - *call expression*')
            st.markdown('`"numpy.core._multiarray_umath.zeros"` - *call expression fully qualified name*')

    PAGE_MAP[page_name].show()


if __name__ == '__main__':
    main()
