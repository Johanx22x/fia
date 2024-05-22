"""error.py es un modulo usado para representar los errores encontrados en el
código fuente."""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorador.token import Token

class ErrorParseo(Exception):
    """Clase usada para representar un error encontrado en el código fuente."""

    def __init__(self, descripcion: str, linea: int, columna: int, tamano_lexema: int,
                 codigo_fuente: str) -> None:
        """Inicializa un objeto de la clase Error.

        Args:
            tipo (str): El tipo de error encontrado en el código fuente.
            descripcion (str): La descripción del error encontrado en el código fuente.
            linea (int): La línea donde se encontró el error.
            columna (int): La columna donde se encontró el error.
        """
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.tamano_lexema = tamano_lexema
        self.codigo_fuente = codigo_fuente

    def obtener_linea(self) -> str:
        """Obtiene la línea donde se encontró el error.

        Returns:
            str: La línea donde se encontró el error.
        """
        return self.codigo_fuente.split("\n")[self.linea - 1]

    def colorear_lexema(self) -> str:
        """Colorea el lexema donde se encontró el error."""
        lexema = self.obtener_linea()[self.columna - 1:self.columna - 1 + self.tamano_lexema]
        return f"\u001b[31m{lexema}\u001b[0m"

    def reemplazar_lexema(self, reemplazo: str) -> str:
        """Reemplaza el lexema donde se encontró el error.

        Args:
            reemplazo (str): El reemplazo del lexema.

        Returns:
            str: La línea con el lexema reemplazado.
        """
        linea = self.obtener_linea()
        return linea[:self.columna - 1] + reemplazo + linea[self.columna - 1 + self.tamano_lexema:]

    def __str__(self) -> str:
        """Representa el objeto como un string.

        Returns:
            str: El objeto representado como un string.
        """
        error = f"Error de parseo: {self.descripcion}"
        error += f" en la línea {self.linea} y columna {self.columna}.\n"
        error += f"\n{self.reemplazar_lexema(self.colorear_lexema())}"
        error += f"\n{' ' * (self.columna - 1)}\u001b[31m{'^' * self.tamano_lexema}\u001b[0m"
        return error


# TODO: Implementar ErrorAnalisis
class ErrorAnalisis(Exception):
    """Clase usada para representar un error encontrado en el análisis del código fuente."""
    def __init__(self, descripcion: str, token: Token) -> None:
        """Inicializa un objeto de la clase Error.

        Args:
            descripcion (str): La descripción del error encontrado en el código fuente.
            token (Token): El token donde se encontró el error.
        """
        self.descripcion = descripcion
        self.token = token

    def __str__(self) -> str:
        """Representa el objeto como un string.

        Returns:
            str: El objeto representado como un string.
        """
        error = f"Error de análisis: {self.descripcion}"
        error += f" en la línea {self.token.linea} y columna {self.token.columna}.\n"
        return error


class ErrorSemantico(Exception):
    """Clase usada para representar un error semántico encontrado en el código fuente a traves del verificador."""
    def __init__(self, simbolo: str, descripcion: str) -> None:
        """Inicializa un objeto de la clase Error.

        Args:
            simbolo (str): El simbolo donde se encontró el error.
            descripcion (str): La descripción del error encontrado en el código fuente.
        """
        self.simbolo = simbolo
        self.descripcion = descripcion

    def __str__(self) -> str:
        """Representa el objeto como un string.

        Returns:
            str: El objeto representado como un string.
        """
        error = f"Error semántico: {self.simbolo} {self.descripcion}"
        return error
