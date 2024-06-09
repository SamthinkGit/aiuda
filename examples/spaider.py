from dataclasses import dataclass

from aiuda import aiuda
from aiuda.core.globals import Globals


@dataclass
class Cat:
    name: str
    age: int
    properties: dict


if __name__ == "__main__":

    cat = Cat("Horus", 6, {"type": "super_cat", "color": "orange"})
    Globals.globals = globals()
    aiuda.spaider(cat)
