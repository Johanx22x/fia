
from tipo_token import tipo_Token

class Token:

    def __init__(self, tipo: tipo_Token, lexema: str, literal, linea: int, columna: int) -> None:
        self.tipo = tipo
        self.lexema = lexema
        self.literal = literal
        self.linea = linea
        self.columna = columna 

    def __str__(self) -> str:
        return f"token: <{self.tipo}, lexema:{self.lexema}, literal:{self.literal}, linea:{self.linea}, columna:{self.columna}>"


