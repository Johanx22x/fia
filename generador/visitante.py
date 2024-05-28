"""visitante.py: Implementación del patrón de diseño Visitor para generar
código Python"""

import sys

from analizador.nodo import Nodo, TipoNodo

BUILD_IN_FUNCTIONS = {
        "radio": "print",
        "aleatorio": "random.randint",
        }

OPERATORS = {
    "||": "or",
    "&&": "and",
    }

EXPRESSIONS = {
    "verdadero": "True",
    "falso": "False",
    }

DEPENDENCIA = """import random

class Escuderia:
    def __init__(self, nombre, pilotos=[], directores=[], ingenieros=[], presupuesto=0, capital=0, autos=[]) -> None:
        self.nombre = nombre
        self.pilotos = pilotos
        self.directores = directores
        self.ingenieros = ingenieros
        self.presupuesto = presupuesto
        self.capital = capital
        self.autos = autos

    def __str__(self) -> str:
        return f"Escuderia: {self.nombre}"

class Piloto:
    def __init__(self, nombre, *stats) -> None:
        self.nombre = nombre
        self.stats = stats

    def __str__(self) -> str:
        return f"Piloto: {self.nombre}"

class Director:
    def __init__(self, nombre, *stats) -> None:
        self.nombre = nombre
        self.stats = stats

    def __str__(self) -> str:
        return f"Director: {self.nombre}"

class Ingeniero:
    def __init__(self, nombre, especialidad) -> None:
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self) -> str:
        return f"Ingeniero: {self.nombre}"

class Auto:
    def __init__(self, modelo, *stats) -> None:
        self.modelo = modelo
        self.stats = stats

    def __str__(self) -> str:
        return f"Auto: {self.modelo}"

"""


class Visitante:
    """Clase que visita los nodos del árbol sintáctico abstracto."""
    tab = "\t"
    tabs = 0

    pilotos = []
    directores = []
    ingenieros = []
    autos = []
    presupuesto = 0
    capital = 0

    def visitar(self, nodo: Nodo) -> str:
        """Visita un nodo y retorna el código Python generado."""
        try:
            visitar = getattr(self, f"visitar_{nodo.tipo.name.lower()}")
        except AttributeError:
            print(f"No se ha implementado el método visitar_{nodo.tipo.name.lower()}")
            sys.exit(-1)
        return visitar(nodo)

    def visitar_campeonato(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo CAMPEONATO."""
        codigo = DEPENDENCIA
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_escuderia(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ESCUDERIA."""
        codigo = ""

        codigo += f"{self.tab * self.tabs}{nodo.lexema} = Escuderia('{nodo.lexema}',\n"
        self.tabs += 1
        for hijo in nodo.hijos:
            self.visitar(hijo)
        
        # Agregar pilotos
        codigo += f"{self.tab * self.tabs}["
        for piloto in self.pilotos:
            codigo += piloto
        codigo += f"],\n"

        # Agregar directores
        codigo += f"{self.tab * self.tabs}["
        for director in self.directores:
            codigo += director
        codigo += f"],\n"

        # Agregar ingenieros
        codigo += f"{self.tab * self.tabs}["
        for ingeniero in self.ingenieros:
            codigo += ingeniero
        codigo += f"],\n"
                                                                        
        # Agregar presupuesto
        codigo += f"{self.tab * self.tabs}{self.presupuesto},\n"

        # Agregar capital
        codigo += f"{self.tab * self.tabs}{self.capital},\n"

        # Agregar autos 
        codigo += f"{self.tab * self.tabs}["
        for auto in self.autos:
            codigo += auto
        codigo += f"]\n"

        # Resetear variables
        self.pilotos = []
        self.directores = []
        self.ingenieros = []
        self.autos = []
        self.presupuesto = 0
        self.capital = 0

        codigo += f"{self.tab * self.tabs})\n"
        self.tabs -= 1
        return codigo

    def visitar_piloto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo PILOTO."""
        codigo = f"Piloto('{nodo.lexema}', "
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        codigo += "),"
        self.pilotos.append(codigo)

    def visitar_director(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo DIRECTOR."""
        codigo = f"Director('{nodo.lexema}', "
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        codigo += "),"
        self.directores.append(codigo)

    def visitar_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo INGENIERO."""
        codigo = f"Ingeniero('{nodo.lexema}', "
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        codigo += "),"
        self.ingenieros.append(codigo)

    def visitar_tipo_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo TIPO_INGENIERO."""
        return f"'{nodo.lexema}'"

    def visitar_auto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo AUTO."""
        codigo = f"Auto('{nodo.lexema}', "
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        codigo += "),"
        self.autos.append(codigo)

    def visitar_presupuesto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo PRESUPUESTO."""
        self.presupuesto = float(nodo.lexema)

    def visitar_capital(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo CAPITAL."""
        self.capital = float(nodo.lexema)

    def visitar_valor(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo VALOR."""
        return f"'{nodo.lexema}'"

    def visitar_instrucciones(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo INSTRUCCIONES."""
        codigo = ""
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo) + "\n"
        return codigo

    def visitar_declaracion_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo DECLARACION_VARIABLE."""
        codigo = ""
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_agrupacion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo AGRUPACION."""
        codigo = "("
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        codigo += ")"
        return codigo

    def visitar_asignacion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ASIGNACION_VARIABLE."""
        codigo = f"{self.tab * self.tabs}"

        codigo += self.visitar(nodo.hijos[0])
        codigo += " = "
        for hijo in nodo.hijos[1:]:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_tipo_dato(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo TIPO_DATO."""
        # NOTE: En Python no es necesario declarar el tipo de dato
        return f""

    def visitar_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo VARIABLE."""
        codigo = f"{nodo.lexema}"
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_operador(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo OPERADOR."""
        if nodo.lexema in OPERATORS:
            return f" {OPERATORS[nodo.lexema]} "
        return f" {nodo.lexema} "

    def visitar_expresion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo EXPRESION."""
        codigo = ""
        if nodo.lexema in EXPRESSIONS:
            codigo += EXPRESSIONS[nodo.lexema]
        else:
            codigo = f"{nodo.lexema}"
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_ciclos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo CICLOS."""
        codigo = f"{self.tab * self.tabs}while ({self.visitar(nodo.hijos[0])}):\n"
        self.tabs += 1
        for hijo in nodo.hijos[1:]:
            codigo += self.visitar(hijo)
        self.tabs -= 1
        return codigo

    def visitar_funcion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo FUNCION."""
        codigo = f"{self.tab * self.tabs}def {nodo.lexema}("
        codigo += self.visitar(nodo.hijos[0])
        codigo += "):\n"

        self.tabs += 1
        for hijo in nodo.hijos[1:]:
            codigo += self.visitar(hijo)
        self.tabs -= 1
        return codigo

    def visitar_parametros(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo PARAMETROS."""
        codigo = ""
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_parametro(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo PARAMETRO."""
        return f"{nodo.lexema}, "

    def visitar_tipo_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo TIPO_RETORNO."""
        # NOTE: En Python no es necesario declarar el tipo de retorno
        return ""

    def visitar_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo RETORNO."""
        return f"{self.tab * self.tabs}return {self.visitar(nodo.hijos[0])}"

    def visitar_acceso_lista(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ACCESO_LISTA."""
        codigo = f"{nodo.lexema}["
        codigo += self.visitar(nodo.hijos[0])
        codigo += "]"
        for hijo in nodo.hijos[1:]:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_condiciones(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo CONDICIONES."""
        codigo = f"{self.tab * self.tabs}if {self.visitar(nodo.hijos[0])}:\n"
        self.tabs += 1
        for hijo in nodo.hijos[1:]:
            if hijo.tipo == TipoNodo.CONDICIONES_OUT:
                self.tabs -= 1
            codigo += self.visitar(hijo)
        self.tabs -= 1
        return codigo

    def visitar_condiciones_out(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo CONDICIONES_OUT."""
        codigo = f"{self.tab * self.tabs}else:\n"
        self.tabs += 1
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_llamada_funcion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo LLAMADA_FUNCION."""
        codigo = ""
        if nodo.lexema in BUILD_IN_FUNCTIONS:
            codigo += f"{self.tab * self.tabs}{BUILD_IN_FUNCTIONS[nodo.lexema]}("
        else:
            codigo += f"{self.tab * self.tabs}{nodo.lexema}("
        codigo += self.visitar(nodo.hijos[0])
        codigo += ")"
        for hijo in nodo.hijos[1:]:
            codigo += self.visitar(hijo)
        return codigo

    def visitar_argumentos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ARGUMENTOS."""
        codigo = ""
        for hijo in nodo.hijos:
            codigo += self.visitar(hijo)
            codigo += ", "
        return codigo
