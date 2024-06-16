from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: int
    worth: int
    volume: int
