from nodes import *
from valores import Numero


class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        assert isinstance(node, NumberNode)
        assert isinstance(node, MultiplyNode)
        assert isinstance(node, POWNode)
        assert isinstance(node, DivideNode)
        assert isinstance(node, PositivoAntes)
        assert isinstance(node, NegativoAntes)
        return method(node)

    def visit_NumberNode(self, node):
        return Numero(node.value)

    def visit_MultiplyNode(self, node):
        return Numero(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_POWNode(self, node):
        try:
            return Numero(self.visit(node.node_a).value ^ self.visit(node.node_b).value)
        except:
            raise Exception("Error Matemático en elevar número")

    def visit_DivideNode(self, node):
        try:
            return Numero(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Error Matemático en división")

    def visit_PositivoAntes(self, node):
        return self.visit(node.node)

    def visit_NegativoAntes(self, node):
        return self.visit(node.node)
