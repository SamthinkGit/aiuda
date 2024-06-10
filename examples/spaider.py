from dataclasses import dataclass
from typing import Hashable

from aiuda import aiuda
from aiuda.core.globals import Globals


@dataclass
class CatName:
    name: str
    alias: str
    hash: Hashable


@dataclass
class Cat:
    name: CatName
    age: int
    properties: dict


if __name__ == "__main__":

    name = CatName("Horus", "miwmiw", hash("Horus"))
    cat = Cat(name=name, age=6, properties={"type": "super_cat", "color": "orange"})
    Globals.globals = globals()
    aiuda.spaider(cat)
