from enum import Enum, auto

class TipoNodo(Enum):
    """Tipos de nodos de un árbol sintáctico abstracto."""
    CAMPEONATO = auto()
    ESCUDERIA = auto()
    MIEMBROS = auto()
    PILOTO = auto()
    DIRECTOR = auto()
    INGENIERO = auto()
    RECURSOS = auto()
    PRESUPUESTO = auto()
    CAPITAL = auto()
    AUTO = auto()
    FUNCION = auto()
    LLAMADA_FUNCION = auto()
    PARAMETROS = auto()
    PARAMETRO = auto()
    TIPO_DATO = auto()
    VARIABLE = auto()
    RETORNO = auto()
    INSTRUCCIONES = auto()
    CONDICIONES = auto()
    CICLOS = auto()
    INSTRUCCION = auto()
    DECLARACION_VARIABLE = auto()
    ASIGNACION = auto()
    EXPRESION = auto()
    OPERADOR = auto()
    ARGUMENTOS = auto()
    AGRUPACION = auto()
    ACCESO_LISTA = auto()
    VALOR = auto()
    TIPO_INGENIERO = auto()
    CONDICIONES_OUT = auto()

class Nodo:

    tipo : TipoNodo
    contenido : str
    atributos : dict


    """Nodo de un árbol sintáctico abstracto."""
    def __init__(self, tipo, lexema, *args):
        self.tipo = tipo
        self.lexema = lexema
        self.hijos = list(args)

    def imprimir(self, nivel=0):
        """Imprime el árbol en preorden."""
        print('  ' * nivel + str(self))
        for hijo in self.hijos:
            hijo.imprimir(nivel + 1)

    def __str__(self):
        """Representación en cadena del nodo."""
        return f"{self.tipo.name}: {self.lexema}"

    def __repr__(self):
        """Representación en cadena del nodo."""
        return str(self)
