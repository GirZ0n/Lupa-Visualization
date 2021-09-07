from src.common.utils import read_stats
from src.kotlin_imports import DATA_FOLDER
from src.kotlin_imports.pages import Page
from src.kotlin_imports.common.pages import show_page


class StatsWithoutAndroidProjects(Page):
    title = 'Statistics without Android projects'
    description = (
        'We consider a project to be entirely android '
        'if it contains **`com.android.tools.build`** dependency in the root build gradle file. '
        'After the filtering of Android repositories, ~4000 projects remained.'
    )
    import_stats_df_path = DATA_FOLDER / 'exclude_android' / 'import_stats.csv'
    import_stats_by_package_df_path = DATA_FOLDER / 'exclude_android' / 'import_stats_by_package.csv'
    key = 'exclude_android'

    @classmethod
    def show(cls):
        import_stats = read_stats(cls.import_stats_df_path, x_label='fq_name', y_label='count')
        import_stats_by_package = read_stats(cls.import_stats_by_package_df_path, x_label='fq_name', y_label='count')

        show_page(
            title=cls.title,
            description=cls.description,
            import_stats=import_stats,
            import_stats_by_package=import_stats_by_package,
            key=cls.key,
        )
