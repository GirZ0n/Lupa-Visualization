from typing import Dict, Type

from src.common.model import Page
from src.kotlin_imports.pages import CustomStats
from src.python_imports.pages.stats_for_all_imports import StatsForAllImports
from src.python_imports.pages.stats_without_stdlib import StatsWithoutStdlib

PAGE_MAP: Dict[str, Type[Page]] = {
    'Statistics for all imports': StatsForAllImports,
    'Statistics without stdlib imports': StatsWithoutStdlib,
    'Custom statistics': CustomStats,
}
