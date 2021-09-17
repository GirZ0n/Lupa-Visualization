from enum import Enum, unique


@unique
class ColumnName(Enum):
    GROUP_ID = 'groupId'
    ARTIFACT_ID = 'artifactId'
    COUNT = 'count'
    GROUP_ID_ARTIFACT_ID = 'groupId:artifactId'
    CONFIG_NAME = 'config_name'
