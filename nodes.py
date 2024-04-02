from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f'{self.value}'


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"


@dataclass
class POWNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} ^ {self.node_b})"


@dataclass
class PositivoAntes:
    node_a: any

    def __repr__(self):
        return f"(+{self.node_a})"


@dataclass
class NegativoAntes:
    node_a: any

    def __repr__(self):
        return f"(-{self.node_a})"
