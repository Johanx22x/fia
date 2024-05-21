
from generador.patronGenerador import Visitante

class Generador:

    visitador  : Visitante

    """Generador de codigo Python"""
    def __init__(self, arbol: Visitante) -> None:
        """Inicializa el generador"""
        self.arbol = arbol
        self.visitador = Visitante()
        ##self.visitador = Nodo('tipo', 'contenidobuenas')

    def imprimir(self, nivel=0):
        self.arbol.imprimir(nivel)

    def generar(self) -> str:
        """Genera codigo Python"""
        self.imprimir()
        resultado = self.visitador.visitar(self.arbol)
        print()
        print(resultado)
        return resultado
 