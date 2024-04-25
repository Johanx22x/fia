from explorador.explorador import Explorador
from analizador.analizador import Analizador

# TODO: Implementar el uso de argparse
# para modificar el comportamiento del programa
def init():
    ...


def main():
    # Obtener el código fuente del archivo
    with open("./gramatica/ejercicio1.fia", "r") as file:
        codigo_fuente = file.read()

    # Tokenizar el código fuente
    explorador = Explorador(codigo_fuente)
    tokens = explorador.tokenizar()

    # Analizar los tokens
    analizador = Analizador(tokens)
    arbol = analizador.analizar()

    # TODO: Verificación del árbol

    # TODO: Generación de código Python

if __name__ == "__main__":
    main()
