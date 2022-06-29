from typing import Dict, Type

from src.common.model import Page
from src.kotlin_imports.pages.custom_stats import CustomStats
from src.kotlin_imports.pages.stats_for_all_projects import StatsForAllProject
from src.kotlin_imports.pages.stats_without_android_projects import StatsWithoutAndroidProjects

PAGE_MAP: Dict[str, Type[Page]] = {
    'Statistics for all projects': StatsForAllProject,
    'Statistics without Android projects': StatsWithoutAndroidProjects,
    'Custom statistics': CustomStats,
}
