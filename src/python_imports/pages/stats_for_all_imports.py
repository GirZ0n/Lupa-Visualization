from src.common.model import Page
from src.common.utils import read_stats
from src.kotlin_imports.common.pages import show_page
from src.python_imports import DATA_FOLDER


class StatsForAllImports(Page):
    title = 'Statistics for all imports'
    description = (
        'We mined all *imports\' fully qualified names* from each Python file '
        'in the dataset using PSI (see `/resources/python_imports/data/import_data.csv`).'
    )
    import_stats_df_path = DATA_FOLDER / 'all' / 'import_stats.csv'
    import_stats_by_package_df_path = DATA_FOLDER / 'all' / 'import_stats_by_package.csv'
    key = 'all'

    @classmethod
    def show(cls):
        import_stats = read_stats(cls.import_stats_df_path)
        import_stats_by_package = read_stats(cls.import_stats_by_package_df_path)

        show_page(
            title=cls.title,
            description=cls.description,
            import_stats=import_stats,
            import_stats_by_package=import_stats_by_package,
            key=cls.key,
        )
