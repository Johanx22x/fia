from explorador.explorador import Explorador
from analizador.analizador import Analizador
from generador.generador import Generador

# TODO: Implementar el uso de argparse
# para modificar el comportamiento del programa
def init():
    ...


def main():
    # Obtener el código fuente del archivo
    with open("./gramatica/ejercicio15.fia", "r") as file:
        codigo_fuente = file.read()

    # Tokenizar el código fuente
    explorador = Explorador(codigo_fuente)
    tokens = explorador.tokenizar()

    #for token in tokens:
    #    print(token)

    #print()
    #print()

    # Analizar los tokens
    analizador = Analizador(tokens)
    arbol = analizador.analizar()
    arbol.imprimir()

    # TODO: Verificación del árbol

    # TODO: Generación de código Python
    
    generador = Generador(arbol)
    generador.generar()
    ##print(codigo_python)


if __name__ == "__main__":
    main()
