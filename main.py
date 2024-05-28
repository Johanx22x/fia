import argparse

from explorador.explorador import Explorador
from analizador.analizador import Analizador
from verificador.verificador import Verificador
from generador.generador import Generador

def init() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="FIA", description="Transpilador de FIA a Python", epilog="¡Gracias por usar FIA!")
    parser.add_argument("-i", "--input", required=True, help="Nombre del archivo de entrada")
    parser.add_argument("-o", "--output", required=False, help="Nombre del archivo de salida")
    parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Mostrar información adicional")
    return parser.parse_args()


def main():
    # Inicializar argumentos
    args = init()

    # Leer el código fuente
    with open(args.input, "r") as file:
        codigo_fuente = file.read()

    # Tokenizar el código fuente
    explorador = Explorador(codigo_fuente)
    tokens = explorador.tokenizar()

    if args.verbose:
        print("Tokens:")
        for token in tokens:
            print(token)
        print()
        print()

    # Analizar los tokens
    analizador = Analizador(tokens)
    arbol = analizador.analizar()

    if args.verbose:
        arbol.imprimir()
        print()
        print()

    # Verificar la semántica del código
    verificador = Verificador(arbol)
    verificador.verificar()

    if args.verbose:
        print(verificador.tabla_simbolos)
        print()
        print()

    # Generar el código Python
    generador = Generador(arbol)
    pycode = generador.generar()

    if args.verbose:
        print(pycode)
        print()
        print()

    # Escribir el código Python en un archivo
    if args.output:
        with open(args.output, "w") as file:
            file.write(pycode)
    else:
        with open("output.py", "w") as file:
            file.write(pycode)


if __name__ == "__main__":
    main()
