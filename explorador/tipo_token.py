"""tipo_token.py es un modulo usado para representar los tipos de tokens
encontrados en el código fuente."""
from enum import Enum, auto


class TipoToken(Enum):
    """Clase usada para representar los tipos de tokens encontrados en el código
    fuente."""

    COMENTARIO = auto()

    PALABRAS_RESERVADAS = auto()
    # ESCUDERIA = auto()
    # PILOTO = auto()
    # DIRECTOR = auto()
    # INGENIERO = auto()
    # AERODINAMICA = auto()
    # MECANICA = auto()
    # PRESUPUESTO = auto()
    # CAPITAL = auto()
    # AUTO = auto()
    # ORDEN = auto()
    # CONFIRMACION = auto()
    # CIRCUITO = auto()
    # BOX = auto()
    # OUT = auto()

    TIPO_DATO = auto()
    # TIPO_ENTERO = auto()
    # TIPO_FLOTANTE = auto()
    # TIPO_BOOLEANO = auto()
    # TIPO_CADENA = auto()

    ENTERO = auto()
    FLOTANTE = auto()
    BOOLEANO = auto()
    CADENA = auto()

    OPERADORES_ARITMETICOS = auto()
    # SUMA = auto()
    # RESTA = auto()
    # MULTIPLICACION = auto()
    # DIVISION = auto()
    # POTENCIA = auto()
    # MODULO = auto()

    OPERADORES_ASIGNACION = auto()
    # IGUAL = auto()
    # SUMA_IGUAL = auto()
    # RESTA_IGUAL = auto()
    # MULTIPLICACION_IGUAL = auto()
    # DIVISION_IGUAL = auto()
    # POTENCIA_IGUAL = auto()
    # MODULO_IGUAL = auto()

    OPERADORES_LOGICOS = auto()
    # AND = auto()
    # OR = auto()
    # NOT = auto()

    OPERADORES_COMPARACION = auto()
    # IGUALDAD = auto()
    # DESIGUALDAD = auto()
    # MENOR_QUE = auto()
    # MAYOR_QUE = auto()
    # MENOR_IGUAL_QUE = auto()
    # MAYOR_IGUAL_QUE = auto()

    OPERADORES_PUNTUACION = auto()
    # PARENTESIS_IZQ = auto()
    # PARENTESIS_DER = auto()
    # PARENTESIS_CUADRADO_IZQ = auto()
    # PARENTESIS_CUADRADO_DER = auto()
    # CORCHETE_IZQ = auto()
    # CORCHETE_DER = auto()
    # PUNTO = auto()
    # COMA = auto()
    # PUNTO_Y_COMA = auto()
    # DOS_PUNTOS = auto()

    IDENTIFICADOR = auto()

    NO_RECONOCIDO = auto()
