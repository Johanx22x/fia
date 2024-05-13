
from generador.patronGenerador import Nodo

class Generador:

    visitador  : Nodo
    """Generador de codigo Python"""
    def __init__(self, arbol: Nodo) -> None:
        """Inicializa el generador"""
        self.arbol = arbol
        self.visitador = Nodo('tipo', 'contenidobuenas')

    def generar(self) -> str:
        """Genera codigo Python"""
        print("estamos en generar")
        print(self.arbol)
        print("no más arbol")
        resultado = self.visitador.generar(self.arbol)
        return resultado
    
    def imprimir(self) -> None:
        print("buenas")
        """Imprime el arbol"""
        self.arbol.imprimir()
        

        