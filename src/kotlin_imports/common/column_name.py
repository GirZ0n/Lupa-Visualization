from enum import Enum, unique


@unique
class ColumnName(Enum):
    FQ_NAME = 'fq_name'
    COUNT = 'count'
