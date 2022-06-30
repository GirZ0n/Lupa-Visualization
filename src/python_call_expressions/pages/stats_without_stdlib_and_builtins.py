from src.common.model import Page
from src.common.utils import get_stats_by_name
from src.python_call_expressions import DATA_FOLDER
from src.python_call_expressions.common.pages import show_page


class StatsWithoutStdlibAndBuiltins(Page):
    title = 'Statistics without Python Standard Library and Python builtins'
    description = (
        "We mined all *call expressions' fully qualified names* from each Python file "
        'in the dataset using PSI (see `/resources/python_call_expressions/data/call_expressions_data.csv`).'
    )
    call_expressions_stats_df_path = DATA_FOLDER / 'exclude_stdlib_and_builtins'
    key = 'exclude_stdlib_and_builtins'

    @classmethod
    def show(cls):
        show_page(
            title=cls.title,
            description=cls.description,
            stats_by_version=get_stats_by_name(cls.call_expressions_stats_df_path),
            key=cls.key,
        )
