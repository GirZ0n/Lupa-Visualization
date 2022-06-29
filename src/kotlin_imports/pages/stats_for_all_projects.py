from src.common.utils import read_stats
from src.kotlin_imports import DATA_FOLDER
from src.kotlin_imports.common.pages import show_page
from src.kotlin_imports.pages import Page


class StatsForAllProject(Page):
    title = 'Statistics for all projects'
    description = (
        "We mined all *imports' fully qualified names* from each Kotlin file "
        'in the dataset using PSI (see `./data/all/import_data.csv`).'
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
