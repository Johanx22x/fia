"""verificador.py es un modulo usado para verificar la sintaxis del código fuente y
generar la tabla de simbolos."""
import sys
import os
from enum import Enum, auto

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from verificador.tipo_simbolo import TipoSimbolo
from utilidades.error import ErrorSemantico
from analizador.nodo import Nodo

BUILT_IN_FUNCTIONS = [
        {'nombre': 'radio', 'tipo': TipoSimbolo.NINGUNO},
        {'nombre': 'aleatorio', 'tipo': TipoSimbolo.ENTERO},
    ]


class Visitante:
    ...


class TipoExpresion(Enum):
    """Enumeración usada para definir el tipo de una expresión."""
    LOGICA = auto()
    ARITMETICA = auto()


class Expresion:
    """Clase usada para definir una expresión en la tabla de expresiones."""

    def __init__(self, visitante: Visitante, tipo: str, expresion: str) -> None:
        self.visitante = visitante
        self.tipo = tipo
        self.expresion = expresion

    def push(self, item: str) -> None:
        """Agregar un item a la expresión."""
        self.expresion.append(item)

    def obtener_tipo_helper(self, item: str) -> str:
        """Obtener el tipo de un item."""
        if item.isnumeric():
            return "ENTERO"
        elif item.replace(".", "", 1).isnumeric():
            return "FLOTANTE"
        elif item == "verdadero" or item == "falso":
            return "BOOLEANO"
        elif item.replace("_", "").replace('"', "").replace("'", "").replace(" ", "").isalpha():
            simbolo = self.visitante.tabla_simbolos.buscar_simbolo_soft(item)
            if simbolo:
                return simbolo.tipo.name
            return "CADENA"
        return "NINGUNO"

    def obtener_tipo(self) -> str:
        """Obtener el tipo de una expresión."""
        tipos = [self.obtener_tipo_helper(item) for item in self.expresion]

        # Si hay un tipo diferente a los demás, disparar un error
        if len(set(tipos)) > 1:
            raise ErrorSemantico("[" + ', '.join(self.expresion) + "]", "tipos incompatibles en la expresión")

        if self.tipo == TipoExpresion.LOGICA:
            return "BOOLEANO"
        return tipos[0]


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
        self.simbolos_backup = []
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
        self.simbolos_backup.append(simbolo)

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

    def buscar_simbolo_soft(self, nombre: str) -> Simbolo:
        for simbolo in self.simbolos:
            if simbolo.nombre == nombre:
                return simbolo
        return None

    def __str__(self) -> str:
        res = 'Tabla de simbolos:\n'
        for simbolo in self.simbolos_backup:
            res += str(simbolo) + '\n'
        return res


class Visitante:
    """Clase usada para visitar los nodos del árbol de sintaxis abstracta."""
    retornos = []
    expresiones = []

    def __init__(self, tabla_simbolos) -> None:
        self.tabla_simbolos = tabla_simbolos

    def visitar(self, nodo: Nodo) -> None:
        try:
            metodo = 'visitar_' + nodo.tipo.name.lower()
            visitante = getattr(self, metodo, None)
            if visitante:
                visitante(nodo)
            else:
                raise Exception(f"Nodo {nodo.tipo} no soportado")
        except Exception as error:
            print(error)
            sys.exit(1)

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

        if tipo != "NINGUNO":
            self.retornos.append(tipo.upper())

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
        if len(self.expresiones) != 0:
            self.expresiones[-1].push(nombre)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_argumentos(self, nodo: Nodo) -> None:
        self.expresiones.append(Expresion(self, TipoExpresion.ARITMETICA, []))
        for hijo in nodo.hijos:
            self.visitar(hijo)
        self.expresiones.pop()

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

        self.expresiones.append(Expresion(self, TipoExpresion.ARITMETICA, []))

        for hijo in nodo.hijos[1].hijos[1:]:
            self.visitar(hijo)

        try:
            if simbolo.tipo.name != self.expresiones[-1].obtener_tipo():
                raise ErrorSemantico(nombre, f"no coincide con el tipo {simbolo.tipo.name}")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

    def visitar_ciclos(self, nodo: Nodo) -> None:
        self.tabla_simbolos.abrir_alcance()
        self.expresiones.append(Expresion(self, TipoExpresion.LOGICA, []))
        self.visitar(nodo.hijos[0])

        try:
            if self.expresiones[-1].obtener_tipo() != "BOOLEANO":
                raise ErrorSemantico("ciclo", "la expresión no es booleana")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

        for hijo in nodo.hijos[1:]:
            self.visitar(hijo)

        self.tabla_simbolos.cerrar_alcance()

    def visitar_condiciones(self, nodo: Nodo) -> None:
        self.tabla_simbolos.abrir_alcance()
        self.expresiones.append(Expresion(self, TipoExpresion.LOGICA, []))

        for hijo in nodo.hijos:
            self.visitar(hijo)

        try:
            if self.expresiones[-1].obtener_tipo() != "BOOLEANO":
                raise ErrorSemantico("condición", "la expresión no es booleana")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

        self.tabla_simbolos.cerrar_alcance()

    def visitar_condiciones_out(self, nodo: Nodo) -> None:
        self.tabla_simbolos.abrir_alcance()
        for hijo in nodo.hijos:
            self.visitar(hijo)
        self.tabla_simbolos.cerrar_alcance()

    def visitar_variable(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        self.tabla_simbolos.buscar_simbolo(nombre)

        self.expresiones[-1].push(nombre)

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

        self.expresiones[-1].push(nombre)

        self.expresiones.append(Expresion(self, TipoExpresion.ARITMETICA, []))

        self.visitar(nodo.hijos[0])

        try:
            if self.expresiones[-1].obtener_tipo() != "ENTERO":
                raise ErrorSemantico(nombre, f"no coincide con el tipo {self.obtener_tipo(self.expresiones[-1])}")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

        for hijo in nodo.hijos[1:]:
            self.visitar(hijo)

    def visitar_retorno(self, nodo: Nodo) -> None:
        self.expresiones.append(Expresion(self, TipoExpresion.ARITMETICA, []))

        for hijo in nodo.hijos:
            self.visitar(hijo)

        try:
            if self.retornos[-1] != self.expresiones[-1].obtener_tipo():
                raise ErrorSemantico(f"retorno [{', '.join(self.expresiones[-1].expresion)}]", f"no coincide con el tipo {self.retornos[-1]}")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)
        except IndexError:
            raise ErrorSemantico(self.expresiones[-1].obtener_tipo(), "no se puede retornar en este contexto")

    def visitar_asignacion(self, nodo: Nodo) -> None:
        nombre = nodo.hijos[0].lexema
        simbolo = self.tabla_simbolos.buscar_simbolo(nombre)

        self.expresiones.append(Expresion(self, TipoExpresion.ARITMETICA, []))

        for hijo in nodo.hijos[1:]:
            self.visitar(hijo)

        try:
            if simbolo.tipo.name != self.expresiones[-1].obtener_tipo():
                raise ErrorSemantico(nombre, f"no coincide con el tipo {simbolo.tipo.name}")
            self.expresiones = self.expresiones[:-1]
        except ErrorSemantico as error:
            print(error)
            sys.exit(1)

    def visitar_expresion(self, nodo: Nodo) -> None:
        self.expresiones[-1].push(nodo.lexema)

        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_agrupacion(self, nodo: Nodo) -> None:
        for hijo in nodo.hijos:
            self.visitar(hijo)

    def visitar_escuderia(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.ESCUDERIA, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        self.tabla_simbolos.abrir_alcance()

        for hijo in nodo.hijos:
            self.visitar(hijo)

        self.tabla_simbolos.cerrar_alcance()

    def visitar_piloto(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.PILOTO, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos[1:]:
            if not hijo.lexema.count(".") == 1:
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")
            if not hijo.lexema.replace(".", "", 1).isnumeric():
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")

        if not nodo.hijos[0].lexema.isnumeric():
            raise ErrorSemantico(nodo.hijos[0].lexema, "no es un valor válido, se esperaba un valor entero")

    def visitar_director(self, nodo: Nodo) -> None:
        nombre = nodo.lexema
        simbolo = Simbolo(nombre, TipoSimbolo.DIRECTOR, 0)
        self.tabla_simbolos.agregar_simbolo(simbolo)

        for hijo in nodo.hijos[1:4]:
            if not hijo.lexema.isnumeric():
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor entero")

        for hijo in nodo.hijos[4:] + nodo.hijos[:1]:
            if not hijo.lexema.count(".") == 1:
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")
            if not hijo.lexema.replace(".", "", 1).isnumeric():
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")

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
            if not hijo.lexema.count(".") == 1:
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")
            if not hijo.lexema.replace(".", "", 1).isnumeric():
                raise ErrorSemantico(hijo.lexema, "no es un valor válido, se esperaba un valor flotante")

    def visitar_valor(self, nodo: Nodo) -> None:
        pass

    def visitar_tipo_ingeniero(self, nodo: Nodo) -> None:
        if nodo.lexema not in ["Mecanica", "Aerodinamica"]:
            raise ErrorSemantico(nodo.lexema, "no es un tipo de ingeniero válido")

    def visitar_presupuesto(self, nodo: Nodo) -> None:
        if not nodo.lexema.isnumeric():
            raise ErrorSemantico(nodo.lexema, "no es un presupuesto válido")

    def visitar_capital(self, nodo: Nodo) -> None:
        if not nodo.lexema.count(".") == 1:
            raise ErrorSemantico(nodo.lexema, "no es un capital válido, se esperaba un valor flotante")
        if not nodo.lexema.replace(".", "", 1).isnumeric():
            raise ErrorSemantico(nodo.lexema, "no es un capital válido, se esperaba un valor flotante")


class Verificador:
    """Clase usada para verificar la semántica del código fuente."""

    def __init__(self, arbol: Nodo) -> None:
        self.arbol = arbol
        self.tabla_simbolos = TablaSimbolos()
        self.visitante = Visitante(self.tabla_simbolos)

    def verificar(self) -> None:
        self.visitante.visitar(self.arbol)
