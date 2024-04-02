from enum import Enum
from dataclasses import dataclass


class Tokentype(Enum):
    Number = 0
    Multiply = 1
    Divide = 2
    OParenthesis = 3
    CParenthesis = 4
    POW = 5


@dataclass
class Token:
    type: Tokentype
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
