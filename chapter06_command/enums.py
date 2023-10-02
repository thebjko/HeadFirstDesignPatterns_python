from enum import Enum


class CeilingFanSpeed(int, Enum):
    OFF: int = 0
    LOW: int = 1
    MEDIUM: int = 2
    HIGH: int = 3
