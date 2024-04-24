"""token.py es un modulo usado para representar los tokens encontrados en el
código fuente."""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorador.tipo_token import TipoToken


class Token:
    """Clase usada para representar los tokens encontrados en el código
    fuente."""

    def __init__(
        self, tipo: TipoToken, lexema: str, linea: int, columna: int
    ) -> None:
        """Constructor para la clase Token.

        Args:
            tipo (TipoToken): El tipo de token.
            lexema (str): El lexema del token.
            linea (int): La linea en la que se encuentra el token.
            columna (int): La columna en la que se encuentra el token.
        """
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    def __str__(self) -> str:
        """Representación en string de la clase Token."""
        return f"token: <{self.tipo}, lexema:{self.lexema}, linea:{self.linea}, columna:{self.columna}>"

    def __repr__(self) -> str:
        """Representación en string de la clase Token."""
        return self.__str__()
