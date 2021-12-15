from src.common.fragments import show_bar_plot_with_config
from src.common.model import Page
from src.common.utils import read_stats
from src.python_call_expressions import DATA_FOLDER

import streamlit as st

from src.python_call_expressions.common.column_name import ColumnName


class StatsForAllCallExpressions(Page):
    title = 'Statistics for all call expressions'
    description = (
        'We mined all *call expressions\' fully qualified names* from each Python file '
        'in the dataset using PSI (see `/resources/python_imports/data/import_data.csv`).'  # TODO: path
    )
    import_stats_df_path = DATA_FOLDER / 'all' / 'call_expressions_stats.csv'
    key = 'all'

    @classmethod
    def show(cls):
        import_stats = read_stats(cls.import_stats_df_path)

        st.title(cls.title)

        st.markdown(cls.description)

        fq_name = st.text_input('Fully qualified name:')
        if fq_name != '':
            import_stats = import_stats[import_stats[ColumnName.FQ_NAME.value].str.startswith(fq_name)]

        categories = st.multiselect(
            'Categories:',
            options=import_stats[ColumnName.CATEGORY.value].unique(),
            default=import_stats[ColumnName.CATEGORY.value].unique(),
        )

        import_stats = import_stats[import_stats[ColumnName.CATEGORY.value].isin(categories)]

        show_bar_plot_with_config(
            header='The occurrence of call expressions FQ names',
            description='The occurrence of the mined call expressions / fully qualified names from projects.',
            df=import_stats,
            x_axis=ColumnName.FQ_NAME.value,
            x_title='Expression name',
            y_axis=ColumnName.COUNT.value,
            y_title='Number of projects',
            key=f'{cls.key}_call_expressions_stats',
        )
