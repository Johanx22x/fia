"""explorador.py es un modulo usado para parsear el código fuente y
tokenizarlo."""
import re
import sys
import os
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorador.token import Token, TipoToken
from utilidades.error import ErrorParseo


TOKENS: List[Tuple[TipoToken, str]] = [
    (TipoToken.COMENTARIO, r"^(//.*)|(\/\*(.|\n)*?\*\/)"),
    (
        TipoToken.PALABRAS_RESERVADAS,
        r"^(escuderia|piloto|director|aerodinamica|mecanica|presupuesto|capital|auto|orden|confirmacion|circuito|box|out|break|continue)",
    ),
    (TipoToken.TIPO_DATO, r"^(entero|flotante|booleano|cadena)"),
    (TipoToken.BOOLEANO, r"^(verdadero|falso)"),
    (TipoToken.FLOTANTE, r"^(-?[0-9]+\.[0-9]+)"),
    (TipoToken.ENTERO, r"^[0-9]+"),
    (TipoToken.CADENA, r'^["\'](.+)*["\']'),
    (TipoToken.OPERADORES_ARITMETICOS, r"^(\+|\-|\*|\/|\%|\^)"),
    (TipoToken.OPERADORES_COMPARACION, r"^(\<\=|\>\=|\=\=|\!\=|\<|\>|)"),
    (TipoToken.OPERADORES_ASIGNACION, r"^(\=|\+\=|\-\=|\*\=|\/\=|\^\=|\%\=)"),
    (TipoToken.OPERADORES_LOGICOS, r"^(\&\&|\|\|)"),
    (TipoToken.PARENTESIS_IZQ, r"^\("),
    (TipoToken.PARENTESIS_DER, r"^\)"),
    (TipoToken.PARENTESIS_CUADRADO_IZQ, r"^\["),
    (TipoToken.PARENTESIS_CUADRADO_DER, r"^\]"),
    (TipoToken.CORCHETE_IZQ, r"^\{"),
    (TipoToken.CORCHETE_DER, r"^\}"),
    (TipoToken.COMA, r"^\,"),
    (TipoToken.PUNTO, r"^\."),
    (TipoToken.PUNTO_Y_COMA, r"^\;"),
    (TipoToken.DOS_PUNTOS, r"^\:"),
    (TipoToken.IDENTIFICADOR, r"^[a-zA-Z][a-zA-Z0-9_]*"),
    (TipoToken.NO_RECONOCIDO, r"^\S+"),
]


class Explorador:
    """Clase usada para parsear el código fuente y tokenizarlo."""

    def __init__(self, codigo_fuente: str) -> None:
        """Constructor para la clase Explorador.

        Args:
            codigo_fuente (str): El código fuente a explorar.
        """
        self.codigo_fuente = codigo_fuente
        self.posicion = 0
        self.linea = 1
        self.columna = 1

    def tokenizar(self) -> List[Token]:
        """Función usada para tokenizar el código fuente.

        Returns:
            List[Token]: La lista de tokens encontrados en el código fuente.
        """
        try:
            tokens = []
            while self.posicion < len(self.codigo_fuente):
                token = self.encontrar_token()
                if token is None:
                    continue
                if token.tipo == TipoToken.NO_RECONOCIDO:
                    raise ErrorParseo(
                        f"No se reconoce el token {token.lexema}",
                        token.linea,
                        token.columna,
                        len(token.lexema),
                        self.codigo_fuente,
                    )
                if token.tipo != TipoToken.COMENTARIO:
                    tokens.append(token)
            return tokens
        except ErrorParseo as error:
            print(error)
            sys.exit(1)

    def encontrar_token(self) -> Token:
        """Función usada para encontrar un token en el código fuente.

        Returns:
            Token: El token encontrado en el código fuente.
        """
        for tipo, patron in TOKENS:
            lexema = self.encontrar_lexema(patron)
            if lexema:
                token = Token(tipo, lexema, self.linea, self.columna)
                self.avanzar(len(lexema))
                return token
        self.avanzar(1)
        return None

    def encontrar_lexema(self, patron: str) -> str:
        """Función usada para encontrar un lexema en el código fuente.

        Args:
            patron (str): El patrón a buscar en el código fuente.

        Returns:
            str: El lexema encontrado en el código fuente.
        """
        match = re.match(patron, self.codigo_fuente[self.posicion :])
        if match:
            return match.group()
        return None

    def avanzar(self, cantidad: int) -> None:
        """Función usada para avanzar la posición en el código fuente.

        Args:
            cantidad (int): La cantidad de caracteres a avanzar.
        """
        for caracter in self.codigo_fuente[self.posicion : self.posicion + cantidad]:
            if caracter == "\n":
                self.linea += 1
                self.columna = 1
            else:
                self.columna += 1
        self.posicion += cantidad
