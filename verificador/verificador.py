"""verificador.py es un modulo usado para verificar la sintaxis del código fuente y
generar la tabla de simbolos."""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from verificador.tipo_simbolo import TipoSimbolo
from utilidades.error import ErrorSemantico
from analizador.nodo import Nodo

BUILT_IN_FUNCTIONS = [
        {'nombre': 'radio', 'tipo': TipoSimbolo.NINGUNO},
    ]


class Simbolo:
    """Clase usada para definir un simbolo en la tabla de simbolos."""

    def __init__(self, nombre: str, tipo: TipoSimbolo, alcance: int) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.alcance = alcance

    def __str__(self) -> str:
        return f'simbolo: <{self.nombre}, {self.tipo}, {self.alcance}>'

    def __repr__(self) -> str:
        return self.__str__()

class TablaSimbolos:
    """Clase usada para definir la tabla de simbolos."""

    def __init__(self) -> None:
        self.simbolos = []
        self.alcance = 0
        self.cargar_ambiente_estandar()

    def abrir_alcance(self) -> None:
        self.alcance += 1

    def cerrar_alcance(self) -> None:
        self.alcance -= 1
        self.simbolos = [simbolo for simbolo in self.simbolos if simbolo.alcance <= self.alcance]

    def agregar_simbolo(self, simbolo: Simbolo) -> None:
        # Revisar si el simbolo ya existe
        try:
            for s in self.simbolos:
                if s.nombre == simbolo.nombre:
                    raise ErrorSemantico(simbolo.nombre, "ya se encuentra definido")
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

        simbolo.alcance = self.alcance
        self.simbolos.append(simbolo)

    def cargar_ambiente_estandar(self) -> None:
        for funcion in BUILT_IN_FUNCTIONS:
            self.agregar_simbolo(Simbolo(funcion['nombre'], funcion['tipo'], 0))

    def buscar_simbolo(self, nombre: str) -> Simbolo:
        try:
            for simbolo in self.simbolos:
                if simbolo.nombre == nombre:
                    return simbolo
            raise ErrorSemantico(nombre, "no se encuentra definido")
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

    def __str__(self) -> str:
        res = 'Tabla de simbolos:\n'
        res += 'Profundidad de alcance: ' + str(self.alcance) + '\n'
        for simbolo in self.simbolos:
            res += str(simbolo) + '\n'
        return res


class Visitante:
    """Clase usada para visitar los nodos del árbol de sintaxis abstracta."""

    def __init__(self, tabla_simbolos) -> None:
        self.tabla_simbolos = tabla_simbolos

    def visitar(self, nodo: Nodo) -> None:
        metodo = 'visitar_' + nodo.tipo.name.lower()
        visitante = getattr(self, metodo, None)
        if visitante:
            visitante(nodo)
        else:
            raise Exception(f"Nodo {nodo.tipo} no soportado")

    def visitar_campeonato(self, nodo: Nodo) -> None:
        self.tabla_simbolos.abrir_alcance()
        for hijo in nodo.hijos:
            self.visitar(hijo)
        self.tabla_simbolos.cerrar_alcance()

    def visitar_funcion(self, nodo: Nodo) -> None:
        hijos_pos = 1
        nombre = nodo.lexema
        tipo = "NINGUNO"

        if len(nodo.hijos) == 3:
            hijos_pos = 2
            tipo = nodo.hijos[1].lexema

        simbolo = Simbolo(nombre, TipoSimbolo[tipo.upper()], 0)

        self.tabla_simbolos.agregar_simbolo(simbolo)
        self.tabla_simbolos.abrir_alcance()

        # Visitar los parámetros
        for hijo in nodo.hijos[0].hijos:
            self.visitar(hijo)

        # Visitar las instrucciones de la función
        for hijo in nodo.hijos[hijos_pos].hijos:
            self.visitar(hijo)

        self.tabla_simbolos.cerrar_alcance()

    def visitar_llamada_funcion(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        self.tabla_simbolos.buscar_simbolo(nombre)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_argumentos(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_parametro(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        tipo = nodo.hijos[0].lexema
        simbolo = Simbolo(nombre, TipoSimbolo[tipo.upper()], 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

    def visitar_declaracion_variable(self, nodo: Nodo) -> None:
        nombre = nodo.hijos[1].hijos[0].lexema
        tipo = nodo.hijos[0].lexema
        simbolo = Simbolo(nombre, TipoSimbolo[tipo.upper()], 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

    def visitar_ciclos(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_condiciones(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_condiciones_out(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_variable(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        self.tabla_simbolos.buscar_simbolo(nombre)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_operador(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_instrucciones(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_acceso_lista(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = self.tabla_simbolos.buscar_simbolo(nombre)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_retorno(self, nodo: Nodo) -> None:
        # TODO: Verificar que el tipo de retorno sea el correcto
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_asignacion(self, nodo: Nodo) -> None:
        # TODO: Verificar que el tipo de la variable sea el correcto
        nombre = nodo.hijos[0].lexema
        self.tabla_simbolos.buscar_simbolo(nombre)

        for hijo in nodo.hijos[1:]:
            self.visitar(hijo)

    def visitar_expresion(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_agrupacion(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_escuderia(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.ESCUDERIA, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_piloto(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.PILOTO, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_director(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.DIRECTOR, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_ingeniero(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.INGENIERO, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_auto(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.AUTO, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_valor(self, nodo: Nodo) -> None:
        pass

    def visitar_tipo_ingeniero(self, nodo: Nodo) -> None:
        pass

    def visitar_presupuesto(self, nodo: Nodo) -> None:
        pass

    def visitar_capital(self, nodo: Nodo) -> None:
        pass


class Verificador:
    """Clase usada para verificar la semántica del código fuente."""

    def __init__(self, arbol: Nodo) -> None:
        self.arbol = arbol
        self.tabla_simbolos = TablaSimbolos()
        self.visitante = Visitante(self.tabla_simbolos)

    def verificar(self) -> None:
        self.visitante.visitar(self.arbol)
