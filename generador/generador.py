
from generador.patronGenerador import Visitante

class Generador:
    """Generador de codigo Python"""

    def __init__(self, arbol: Visitante) -> None:
        """Inicializa el generador"""
        self.arbol = arbol
        self.visitador = Visitante()

    def imprimir(self, nivel=0):
        """Imprime el arbol"""
        self.arbol.imprimir(nivel)

    def generar(self) -> str:
        """Genera codigo Python"""
        self.imprimir()
        resultado = self.visitador.visitar(self.arbol)
        return resultado
