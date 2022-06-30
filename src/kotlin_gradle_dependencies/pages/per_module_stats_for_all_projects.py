from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.common.pages import show_page
from src.kotlin_gradle_dependencies.pages import Page


class PerModuleStatsForAllProject(Page):
    title = 'Per module statistics for all projects'
    description = (
        'We mined all gradle dependencies from build.gradle/build.gradle.kts files '
        'from project modules in the dataset using PSI.'
    )
    full_name_stats_df_path = DATA_FOLDER / 'all' / 'full_name_stats.csv'
    group_stats_df_path = DATA_FOLDER / 'all' / 'groups_stats.csv'
    config_stats_df_path = DATA_FOLDER / 'all' / 'config_stats.csv'
    key = 'per_module_stats_all'

    @classmethod
    def show(cls):
        full_name_stats = read_stats(cls.full_name_stats_df_path)
        group_stats = read_stats(cls.group_stats_df_path)
        config_stats = read_stats(cls.config_stats_df_path)

        show_page(
            title=cls.title,
            description=cls.description,
            full_name_stats=full_name_stats,
            groups_stats=group_stats,
            config_stats=config_stats,
            key=cls.key,
        )
