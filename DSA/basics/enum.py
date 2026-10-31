"""Enum examples for common Python patterns."""

import importlib.util
import sysconfig
from pathlib import Path

_stdlib_enum_path = Path(sysconfig.get_paths()["stdlib"]) / "enum.py"
_stdlib_enum_spec = importlib.util.spec_from_file_location("_stdlib_enum", _stdlib_enum_path)
_stdlib_enum_module = importlib.util.module_from_spec(_stdlib_enum_spec)
_stdlib_enum_spec.loader.exec_module(_stdlib_enum_module)

Enum = _stdlib_enum_module.Enum
IntEnum = _stdlib_enum_module.IntEnum
auto = _stdlib_enum_module.auto


class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


class Status(IntEnum):
    PENDING = 0
    IN_PROGRESS = 1
    DONE = 2


class DemoEnum(Enum):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


def describe_enum(value):
    """Return a simple description for enum values."""
    return f"{value.name}: {value.value}"


if __name__ == "__main__":
    print(describe_enum(TrafficLight.RED))
    print(list(Status))
    print(list(DemoEnum))
