import os
import sys
from more_itertools import peekable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorador.explorador import Explorador


class Analizador:
    """Clase que representa un analizador léxico y sintáctico."""
    def __init__(self, tokens):
        self.tokens = peekable(tokens)

    # TODO: Declare return types for all methods
    def analizar(self):
        """Genera un árbol sintáctico abstracto."""
        self.tokens = iter(self.tokens)
        return self.campeonato()

    def campeonato(self):
        """Punto de entrada de la gramática."""
        nodo = None
        ...

    def declaraciones(self):
        """Analiza las declaraciones."""
        ...

    def escuderia(self):
        ...

    def miembros(self):
        # NOTE: This can be deleted if not needed
        ...

    def piloto(self):
        ...

    def director(self):
        ...
    
    def ingeniero(self):
        ...

    def recursos(self):
        # NOTE: This can be deleted if not needed
        ...

    def presupuesto(self):
        ...

    def capital(self):
        ...

    def auto(self):
        ...

    def funcion(self):
        ...

    def parametros(self):
        ...

    def retorno(self):
        ...

    def instrucciones(self):
        ...

    def condiciones(self):
        ...

    def ciclos(self):
        ...

    def instruccion(self):
        ...

    def declaracion_variable(self):
        ...

    def asignacion(self):
        ...

    def expresion(self):
        ...

    def llamada_funcion(self):
        ...


def test():
    with open("./gramatica/ejercicio1.fia", "r") as file:
        codigo_fuente = file.read()
    explorador = Explorador(codigo_fuente)
    tokens = explorador.tokenizar()
    analizador = Analizador(tokens)
    arbol = analizador.analizar()
    # arbol.imprimir()


if __name__ == '__main__':
    test()