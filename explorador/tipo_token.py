from enum import Enum, auto

class tipo_Token(Enum):
    # Palabras reservadas

    CAMPEONATO = auto()
    ESCUDERIA = auto()
    PILOTO = auto()
    DIRECTOR = auto()
    INGENIERO = auto()
    AERODINAMICA = auto()
    MECANICA = auto()
    PRESUPUESTO = auto()
    CAPITAL = auto()
    AUTO = auto()
    ORDEN = auto()
    CONFIRMACION = auto()
    RADIO = auto()
    COMENTARIO = auto()
    CIRCUITO = auto()
    BOX = auto()
    OUT = auto()

    ENTERO = auto()
    FLOTANTE = auto()
    BOOLEANO = auto()
    CADENA = auto()

    IDENTIFICADOR = auto()

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
    #AND = auto()
    #OR = auto()
    #NOT = auto()

    OPERADORES_COMPARACION = auto()
    #IGUALDAD = auto()
    #DESIGUALDAD = auto()
    #MENOR_QUE = auto()
    #MAYOR_QUE = auto()
    #MENOR_IGUAL_QUE = auto()
    #MAYOR_IGUAL_QUE = auto()

    OPERADORES_PUNTUACION = auto()
    #PARENTESIS_IZQ = auto()
    #PARENTESIS_DER = auto()
    #PARENTESIS_CUADRADO_IZQ = auto()
    #PARENTESIS_CUADRADO_DER = auto()
    #CORCHETE_IZQ = auto()
    #CORCHETE_DER = auto()
    #PUNTO = auto()
    #COMA = auto()
    #PUNTO_Y_COMA = auto()
    #DOS_PUNTOS = auto()



