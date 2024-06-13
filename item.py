from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    worth: int
    volume: int
