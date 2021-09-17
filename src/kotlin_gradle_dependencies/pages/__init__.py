from typing import Dict, Type

from src.common.model import Page
from src.kotlin_gradle_dependencies.pages.per_module_stats_for_all_projects import PerModuleStatsForAllProject
from src.kotlin_gradle_dependencies.pages.per_module_stats_without_android_projects import (
    PerModuleStatsWithoutAndroidProjects,
)
from src.kotlin_gradle_dependencies.pages.per_project_stats import PerProjectStats

PAGE_MAP: Dict[str, Type[Page]] = {
    'Per module statistics for all projects': PerModuleStatsForAllProject,
    'Per module statistics without Android projects': PerModuleStatsWithoutAndroidProjects,
    'Per project statistics': PerProjectStats,
}
