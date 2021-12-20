from typing import Dict, Type

from src.common.model import Page
from src.python_call_expressions.pages.stats_for_all_call_expressions import StatsForAllCallExpressions
from src.python_call_expressions.pages.stats_without_stdlib_and_builtins import StatsWithoutStdlibAndBuiltins

PAGE_MAP: Dict[str, Type[Page]] = {
    'Statistics for all expressions': StatsForAllCallExpressions,
    'Statistics without stdlib and builtins': StatsWithoutStdlibAndBuiltins,
}
