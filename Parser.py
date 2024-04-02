from Tokens import Tokentype
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raiseError(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.cur_token = next(self.tokens)
        except StopIteration:
            self.cur_token = None

    def parse(self):
        if self.cur_token is None:
            return None
        result = self.expr()

        if self.cur_token is not None:
            self.raiseError()
        return result

    def expr(self):
        result = self.CON()
        while self.cur_token is not None and self.cur_token in (Tokentype.Multiply, Tokentype.POW):
            if self.cur_token.type == Tokentype.Multiply:
                self.advance()
                result = MultiplyNode(result, self.CON())
            elif self.cur_token.type == Tokentype.POW:
                self.advance()
                result = POWNode(result, self.CON())
        return result

    def CON(self):
        result = self.term()
        while self.cur_token is not None and self.cur_token in Tokentype.Divide:
            if self.cur_token.type == Tokentype.Divide:
                self.advance()
                result = DivideNode(result, self.term())
        return result

    def term(self):
        token = self.cur_token
        if token.type == Tokentype.OParenthesis:
            self.advance()
            result = self.expr()
            if self.cur_token.type is not Tokentype.CParenthesis:
                self.raiseError()
            self.advance()
            return result

        if token.type == Tokentype.Multiply:
            self.advance()
            return MultiplyNode(self.term(), token.value)

        if token.type == Tokentype.Number:
            self.advance()
            return NumberNode(token.value)
        self.raiseError()
