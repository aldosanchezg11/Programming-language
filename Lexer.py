from Tokens import Tokentype, Token
ESPACIO = ' \n\t'
DIGITOS = '0123456789'


class lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_character = next(self.text)
        except StopIteration:
            self.current_character = None

    def generate_tokens(self):
        while self.current_character is not None:
            if self.current_character in ESPACIO:
                self.advance()
            elif self.current_character == '.' or self.current_character in DIGITOS:
                yield self.generate_number()
            elif self.current_character == '*':
                self.advance()
                yield Token(Tokentype.Multiply)
            elif self.current_character == '/':
                self.advance()
                yield Token(Tokentype.Divide)
            elif self.current_character == '(':
                self.advance()
                yield Token(Tokentype.OParenthesis)
            elif self.current_character == ')':
                self.advance()
                yield Token(Tokentype.CParenthesis)
            elif self.current_character == '^':
                self.advance()
                yield Token(Tokentype.POW)
            else:
                raise Exception(f"Caracter no válido '{self.current_character}'")

    def generate_number(self):
        punto_decimal = 0
        number_s = self.current_character
        self.advance()
        while self.current_character is not None and (self.current_character == '.' or self.current_character):
            if self.current_character == '.':
                punto_decimal += 1
                if punto_decimal > 1:
                    break
            number_s += self.current_character
            self.advance()
        if number_s.startswith('.'):
            number_s = '0' + number_s
        if number_s.endswith('.'):
            number_s += '0'
        return Token(Tokentype.Number, float(number_s))