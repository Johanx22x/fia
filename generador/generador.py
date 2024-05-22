"""generador.py: Generador de codigo Python"""

from generador.patron_generador import Visitante

class Generador:
    """Generador de codigo Python"""

    def __init__(self, arbol: Visitante) -> None:
        """Inicializa el generador"""
        self.arbol = arbol
        self.visitador = Visitante()

    def generar(self) -> str:
        """Genera codigo Python"""
        return self.visitador.visitar(self.arbol)
