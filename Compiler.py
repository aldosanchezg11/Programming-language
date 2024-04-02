from Lexer import lexer
from Parser import *
from interpreter import Interpreter

while True:
    try:
        text = input("Program > ")
        lexer = lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree:
            continue
        interpreter = Interpreter()
        valor = interpreter.visit(tree)
        print(valor)
    except Exception as e:
        print(e)
