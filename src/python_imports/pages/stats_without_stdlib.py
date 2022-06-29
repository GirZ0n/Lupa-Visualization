from src.common.model import Page
from src.common.utils import get_stats_by_name
from src.python_imports import DATA_FOLDER
from src.python_imports.common.pages import show_page


class StatsWithoutStdlib(Page):
    title = 'Statistics without Python Standard Library'
    description = (
        "We mined all *imports' fully qualified names* from each Python file "
        'in the dataset using PSI (see `/resources/python_imports/data/import_data.csv`).'
    )
    import_stats_df_path = DATA_FOLDER / 'exclude_stdlib' / 'import_stats'
    import_stats_by_package_df_path = DATA_FOLDER / 'exclude_stdlib' / 'import_stats_by_package'
    key = 'exclude_stdlib'

    @classmethod
    def show(cls):
        show_page(
            title=cls.title,
            description=cls.description,
            import_stats_by_version=get_stats_by_name(cls.import_stats_df_path),
            package_stats_by_version=get_stats_by_name(cls.import_stats_by_package_df_path),
            key=cls.key,
        )
