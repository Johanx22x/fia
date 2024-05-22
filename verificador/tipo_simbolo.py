"""tipo_simbolo.py es un modulo usado para definir el tipo de simbolo en la
tabla de simbolos."""
from enum import Enum, auto

class TipoSimbolo(Enum):
    """Enum usado para definir el tipo de simbolo en la tabla de simbolos."""
    ENTERO = auto()
    FLOTANTE = auto()
    BOOLEANO = auto()
    CADENA = auto()
    NINGUNO = auto()
    ESCUDERIA = auto()
    PILOTO = auto()
    DIRECTOR = auto()
    INGENIERO = auto()
    AUTO = auto()
