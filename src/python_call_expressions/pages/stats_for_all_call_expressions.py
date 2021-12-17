from src.common.model import Page
from src.common.utils import read_stats
from src.python_call_expressions import DATA_FOLDER

from src.python_call_expressions.common.pages import show_page


class StatsForAllCallExpressions(Page):
    title = 'Statistics for all call expressions'
    description = (
        'We mined all *call expressions\' fully qualified names* from each Python file '
        'in the dataset using PSI (see `/resources/python_call_expressions/data/call_expressions_data.csv`).'
    )
    call_expressions_stats_df_path = DATA_FOLDER / 'all' / 'call_expressions_stats.csv'
    key = 'all'

    @classmethod
    def show(cls):
        stats = read_stats(cls.call_expressions_stats_df_path)
        show_page(title=cls.title, description=cls.description, stats=stats, key=cls.key)
