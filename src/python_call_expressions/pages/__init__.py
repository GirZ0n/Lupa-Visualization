from typing import Dict, Type

from src.common.model import Page
from src.python_call_expressions.pages.stats_for_all_call_expressions import StatsForAllCallExpressions

PAGE_MAP: Dict[str, Type[Page]] = {
    'Statistics for all imports': StatsForAllCallExpressions,
    'Statistics without stdlib': StatsForAllCallExpressions,  # TODO
}
