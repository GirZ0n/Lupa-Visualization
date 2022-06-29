from src.common.utils import read_stats
from src.kotlin_gradle_dependencies import DATA_FOLDER
from src.kotlin_gradle_dependencies.common.pages import show_page
from src.kotlin_gradle_dependencies.pages import Page


class PerModuleStatsWithoutAndroidProjects(Page):
    title = 'Per module statistics without Android projects'
    description = (
        'We consider a project to be entirely android if it contains **`com.android.tools.build`** dependency '
        'in the root build gradle file. After the filtering of Android repositories, ~4000 projects remained.'
    )
    full_name_stats_df_path = DATA_FOLDER / 'exclude_android' / 'full_name_stats.csv'
    group_stats_df_path = DATA_FOLDER / 'exclude_android' / 'groups_stats.csv'
    config_stats_df_path = DATA_FOLDER / 'exclude_android' / 'config_stats.csv'
    key = 'per_module_stats_exclude_android'

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
