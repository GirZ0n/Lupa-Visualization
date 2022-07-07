from src.common.fragments import show_bar_plot_with_config
from src.kotlin_imports.common.column_name import ColumnName
from src.kotlin_imports.common.utils import get_fq_names_stats

import streamlit as st

_KEY = 'custom_stats'

if __name__ == '__main__':
    st.set_page_config(page_title='Kotlin Imports', layout='wide')

    st.title('Custom statistics')

    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        fq_name_file = st.file_uploader(
            label='fq_names:',
            help='Path to a CSV file which contains column `import` with import directives fully qualified name',
            type=['csv'],
            key=f'{_KEY}_fq_name',
        )

    with middle_column:
        filter_packages_file = st.file_uploader(
            label='filter_packages:',
            help='Path to a CSV file which contains column `package_name` with package names to filter packages by',
            type=['csv'],
            key=f'{_KEY}_filter_packages',
        )

    with right_column:
        group_by_packages_file = st.file_uploader(
            label='group_by_packages:',
            help='Path to a CSV file which contains column `package_name` with package names to group imports by',
            type=['csv'],
            key=f'{_KEY}_group_by_packages',
        )

    if fq_name_file is not None:
        stats = get_fq_names_stats(
            fq_names_path=fq_name_file,
            filter_packages_path=filter_packages_file,
            group_by_packages_path=group_by_packages_file,
        )

        show_bar_plot_with_config(
            header='',
            description='',
            df=stats,
            x_axis=ColumnName.FQ_NAME.value,
            x_title='Package name',
            y_axis=ColumnName.COUNT.value,
            y_title='Count',
            key=_KEY,
        )

        st.download_button(
            label='Download statistics',
            data=stats.to_csv(index=False),
            file_name='stats.csv',
            mime='text/csv',
            key=f'{_KEY}_download_button',
        )
