import sys

sys.path.append('')
sys.path.append('../..')

from src.kotlin_gradle_dependencies.pages import PAGE_MAP

import streamlit as st


def main():
    st.set_page_config(page_title='Kotlin Gradle Dependencies', layout='wide')

    with st.sidebar:
        st.title('Kotlin Gradle Dependencies')
        page_name = st.radio('Select page', PAGE_MAP.keys())

        with st.expander('Glossary'):
            st.markdown('`implementation "org.jetbrains.kotlin:kotlin-reflect:1.5.10"` - *Gradle dependency* where:')
            st.markdown('* `implementation` - configuration')
            st.markdown('* `org.jetbrains.kotlin` - groupId')
            st.markdown('* `kotlin - reflect` - artifactId')
            st.markdown('`1.5.10` - version')

    PAGE_MAP[page_name].show()


if __name__ == '__main__':
    main()
