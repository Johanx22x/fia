import os
import sys
from more_itertools import peekable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorador.explorador import Explorador
from explorador.tipo_token import TipoToken
from utilidades.error import ErrorAnalisis
from analizador.nodo import Nodo, TipoNodo


class Analizador:
    """Clase que representa un analizador léxico y sintáctico."""
    def __init__(self, tokens):
        self.tokens = iter(peekable(tokens))

    # TODO: Declare return types for all methods
    def analizar(self):
        """Genera un árbol sintáctico abstracto."""
        self.tokens = iter(self.tokens)
        return self.campeonato()

    def campeonato(self) -> Nodo:
        """Punto de entrada de la gramática."""
        nodo = Nodo(TipoNodo.CAMPEONATO, '')

        while True:
            try:
                token = self.tokens.peek()
                if token.tipo == TipoToken.PALABRAS_RESERVADAS:
                    if token.lexema == 'circuito':
                        token = next(self.tokens)
                        nodo.hijos.append(self.ciclos())
                    elif token.lexema == 'box':
                        token = next(self.tokens)
                        nodo.hijos.append(self.condiciones())
                    else:
                        token = next(self.tokens)
                        nodo.hijos.append(self.declaraciones(token))
                elif token.tipo == TipoToken.IDENTIFICADOR or token.tipo == TipoToken.TIPO_DATO:
                    nodo.hijos.append(self.instrucciones())
                else:
                    raise ErrorAnalisis('Se esperaba una declaración o una instrucción', token)
            except StopIteration:
                break
            except ErrorAnalisis as error:
                print(error)
                exit(-1)

        return nodo

    def declaraciones(self, token) -> Nodo:
        """Analiza las declaraciones."""
        try:
            if token.lexema == 'escuderia':
                return self.escuderia()
            elif token.lexema == 'orden':
                return self.funcion()
            else:
                raise ErrorAnalisis('Se esperaba una declaración', token)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def escuderia(self) -> Nodo:
        """Analiza una escudería."""
        try:
            token = next(self.tokens)
        except StopIteration:
            print("Error de análisis: Estructura de escudería incompleta.")
            exit(-1)

        nodo = Nodo(TipoNodo.ESCUDERIA, token.lexema)

        try:
            if self.tokens.peek().tipo == TipoToken.CORCHETE_IZQ:
                next(self.tokens)
            else:
                raise ErrorAnalisis('Se esperaba un corchete izquierdo', token)
        except StopIteration:
            print("Error de análisis: Estructura de escudería incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

        while True:
            try:
                token = next(self.tokens)
                if token.lexema == 'piloto':
                    nodo.hijos.append(self.piloto())
                elif token.lexema == 'director':
                    nodo.hijos.append(self.director())
                elif token.lexema == 'ingeniero':
                    nodo.hijos.append(self.ingeniero())
                elif token.lexema == 'presupuesto':
                    nodo.hijos.append(self.presupuesto())
                elif token.lexema == 'capital':
                    nodo.hijos.append(self.capital())
                elif token.lexema == 'auto':
                    nodo.hijos.append(self.auto())
                elif token.tipo == TipoToken.CORCHETE_DER:
                    break
                elif token.tipo != TipoToken.PALABRAS_RESERVADAS:
                    raise ErrorAnalisis('Se esperaba una declaración', token)
            except StopIteration:
                break
            except ErrorAnalisis as error:
                print(error)
                exit(-1)

        return nodo

    def piloto(self):
        """Analiza un piloto."""
        try:
            token = next(self.tokens)

            nodo = Nodo(TipoNodo.PILOTO, token.lexema)

            valor1 = next(self.tokens)
            valor2 = next(self.tokens)
            valor3 = next(self.tokens)
            valor4 = next(self.tokens)
            valor5 = next(self.tokens)
            
            if valor1.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor1)
            if valor2.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor2)
            if valor3.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor3)
            if valor4.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor4)
            if valor5.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor5)
            
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor1.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor2.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor3.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor4.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor5.lexema))

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de piloto incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def director(self):
        """Analiza un director."""
        try:
            token = next(self.tokens)

            nodo = Nodo(TipoNodo.DIRECTOR, token.lexema)

            valor1 = next(self.tokens)
            valor2 = next(self.tokens)
            valor3 = next(self.tokens)
            valor4 = next(self.tokens)
            valor5 = next(self.tokens)
            
            if valor1.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor1)
            if valor2.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor2)
            if valor3.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor3)
            if valor4.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor4)
            if valor5.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor5)
            
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor1.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor2.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor3.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor4.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor5.lexema))

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de director incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)
    
    def ingeniero(self):
        """Analiza un ingeniero."""
        try:
            token = next(self.tokens)

            nodo = Nodo(TipoNodo.INGENIERO, token.lexema)

            tipo = next(self.tokens)
            
            if tipo.lexema not in ['Aerodinamica', 'Mecanica']:
                raise ErrorAnalisis('Se esperaba un tipo de ingeniero', tipo)

            nodo.hijos.append(Nodo(TipoNodo.TIPO_INGENIERO, tipo.lexema))

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de ingeniero incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def presupuesto(self):
        """Analiza un presupuesto."""
        try:
            valor = next(self.tokens)
            
            if valor.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor)

            nodo = Nodo(TipoNodo.PRESUPUESTO, valor.lexema)

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de presupuesto incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def capital(self):
        """Analiza un capital."""
        try:
            valor = next(self.tokens)

            if valor.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor)
            
            nodo = Nodo(TipoNodo.CAPITAL, valor.lexema)

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de capital incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def auto(self):
        """Analiza un auto."""
        try:
            token = next(self.tokens)

            nodo = Nodo(TipoNodo.AUTO, token.lexema)

            valor1 = next(self.tokens)
            valor2 = next(self.tokens)
            valor3 = next(self.tokens)
            valor4 = next(self.tokens)
            valor5 = next(self.tokens)
            
            if valor1.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor1)
            if valor2.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor2)
            if valor3.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor3)
            if valor4.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor4)
            if valor5.tipo not in [TipoToken.ENTERO, TipoToken.FLOTANTE]:
                raise ErrorAnalisis('Se esperaba un valor numérico', valor5)
            
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor1.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor2.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor3.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor4.lexema))
            nodo.hijos.append(Nodo(TipoNodo.VALOR, valor5.lexema))

            token = next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de auto incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def funcion(self) -> Nodo:
        """Analiza una función."""
        try:
            token = next(self.tokens)
        except StopIteration:
            print("Error de análisis: Estructura de función incompleta.")
            exit(-1)

        nodo = Nodo(TipoNodo.FUNCION, token.lexema)

        try:
            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_IZQ:
                raise ErrorAnalisis('Se esperaba un paréntesis izquierdo', token)
        except StopIteration:
            print("Error de análisis: Estructura de función incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

        nodo.hijos.append(self.parametros())

        if self.tokens.peek().tipo == TipoToken.PARENTESIS_CUADRADO_IZQ:
            while next(self.tokens).tipo != TipoToken.PARENTESIS_CUADRADO_DER:
                continue

        try:
            token = next(self.tokens)

            if token.tipo != TipoToken.CORCHETE_IZQ:
                raise ErrorAnalisis('Se esperaba un corchete izquierdo', token)
        except StopIteration:
            print("Error de análisis: Estructura de función incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

        nodo.hijos.append(self.instrucciones())

        return nodo

    def parametros(self):
        """Analiza los parámetros de una función."""
        try:
            if self.tokens.peek().tipo == TipoToken.PARENTESIS_DER:
                next(self.tokens)
                return Nodo(TipoNodo.PARAMETROS, '')
        except StopIteration:
            print("Error de análisis: Estructura de parámetros incompleta.")
            exit(-1)
            
        nodo = Nodo(TipoNodo.PARAMETROS, '')

        while True:
            try:
                token = next(self.tokens)

                if token.tipo == TipoToken.PARENTESIS_DER:
                    break
                elif token.tipo == TipoToken.TIPO_DATO:
                    nodo.hijos.append(self.parametro())
                elif token.tipo == TipoToken.COMA:
                    continue
                else:
                    raise ErrorAnalisis('Se esperaba un tipo de dato o una coma', token)
            except StopIteration:
                break
            except ErrorAnalisis as error:
                print(error)
                exit(-1)

        return nodo

    def parametro(self):
        """Analiza un parámetro de una función."""
        try:
            token = next(self.tokens)

            if token.tipo != TipoToken.IDENTIFICADOR:
                raise ErrorAnalisis('Se esperaba un identificador', token)
        except StopIteration:
            print("Error de análisis: Estructura de parámetro incompleta.")
            exit(-1)

        nodo = Nodo(TipoNodo.PARAMETRO, token.lexema)

        return nodo


    def retorno(self):
        """Analiza un retorno."""
        try:
            nodo = Nodo(TipoNodo.RETORNO, '')

            nodo.hijos.append(self.expresion())

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de retorno incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def instrucciones(self):
        """Analiza instrucciones."""
        nodo = Nodo(TipoNodo.INSTRUCCIONES, '')

        while True:
            try:
                token = next(self.tokens)

                if token.tipo == TipoToken.CORCHETE_DER:
                    break
                elif token.tipo == TipoToken.PUNTO_Y_COMA:
                    continue
                elif token.tipo == TipoToken.PALABRAS_RESERVADAS:
                    if token.lexema == 'box':
                        nodo.hijos.append(self.condiciones())
                    elif token.lexema == 'circuito':
                        nodo.hijos.append(self.ciclos())
                    elif token.lexema == 'confirmacion':
                        nodo.hijos.append(self.retorno())
                elif token.tipo == TipoToken.TIPO_DATO:
                    nodo.hijos.append(self.declaracion_variable(token))
                elif token.tipo == TipoToken.IDENTIFICADOR:
                    nodo.hijos.append(self.instruccion(token))
                else:
                    raise ErrorAnalisis('Se esperaba una instrucción', token)
            except StopIteration:
                break
            except ErrorAnalisis as error:
                print(error)
                exit(-1)

        return nodo

    def condiciones(self):
        """Analiza condiciones."""
        try:
            nodo = Nodo(TipoNodo.CONDICIONES, '')

            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_IZQ:
                raise ErrorAnalisis('Se esperaba un paréntesis izquierdo', token)

            nodo.hijos.append(self.expresion())

            token = next(self.tokens)

            if token.tipo != TipoToken.CORCHETE_IZQ:
                raise ErrorAnalisis('Se esperaba un corchete izquierdo', token)

            nodo.hijos.append(self.instrucciones())

            if self.tokens.peek().tipo == TipoToken.PALABRAS_RESERVADAS and self.tokens.peek().lexema == 'out':
                token = next(self.tokens)
                token = next(self.tokens)

                if token.tipo != TipoToken.CORCHETE_IZQ:
                    raise ErrorAnalisis('Se esperaba un corchete izquierdo', token)

                nodo.hijos.append(self.instrucciones())

            return nodo

        except StopIteration:
            print("Error de análisis: Estructura de condiciones incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def ciclos(self):
        """Analiza ciclos."""
        try:
            nodo = Nodo(TipoNodo.CICLOS, '')

            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_IZQ:
                raise ErrorAnalisis('Se esperaba un paréntesis izquierdo', token)

            nodo.hijos.append(self.expresion())

            token = next(self.tokens)

            if token.tipo != TipoToken.CORCHETE_IZQ:
                raise ErrorAnalisis('Se esperaba un corchete izquierdo', token)

            nodo.hijos.append(self.instrucciones())

            return nodo

        except StopIteration:
            print("Error de análisis: Estructura de ciclos incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def instruccion(self, token):
        """Analiza una instrucción."""
        try:
            if self.tokens.peek().tipo == TipoToken.OPERADORES_ASIGNACION:
                return self.asignacion(token)
            elif self.tokens.peek().tipo == TipoToken.PARENTESIS_IZQ:
                return self.llamada_funcion(token)
            else:
                raise ErrorAnalisis('Se esperaba una asignación o una llamada a función', token)
        except StopIteration:
            print("Error de análisis: Estructura de instrucción incompleta.")
            exit(-1)

    def declaracion_variable(self, token):
        """Analiza una declaración de variable."""
        tipo_dato = token.lexema

        nodo = Nodo(TipoNodo.DECLARACION_VARIABLE, '')

        nodo.hijos.append(Nodo(TipoNodo.TIPO_DATO, tipo_dato))
        nodo.hijos.append(self.asignacion())

        return nodo

    def asignacion(self, token=None):
        """Analiza una asignación."""
        try:
            if token is None:
                token = next(self.tokens)

            if token.tipo != TipoToken.IDENTIFICADOR:
                raise ErrorAnalisis('Se esperaba un identificador', token)

            nodo = Nodo(TipoNodo.ASIGNACION, "")

            nodo.hijos.append(Nodo(TipoNodo.VARIABLE, token.lexema))

            token = next(self.tokens)

            if token.lexema != '=':
                raise ErrorAnalisis('Se esperaba un signo igual', token)

            nodo.hijos.append(self.expresion())

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de asignación incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def expresion(self):
        """Analiza una expresión."""
        try:
            token = next(self.tokens)

            if token.tipo == TipoToken.ENTERO or token.tipo == TipoToken.FLOTANTE or token.tipo == TipoToken.BOOLEANO or token.tipo == TipoToken.CADENA:
                nodo = Nodo(TipoNodo.EXPRESION, token.lexema)
            elif token.tipo == TipoToken.IDENTIFICADOR:
                nodo = self.busqueda(token)
            elif token.tipo == TipoToken.PARENTESIS_IZQ:
                nodo = Nodo(TipoNodo.AGRUPACION, '')
                nodo.hijos.append(self.expresion())
            else:
                raise ErrorAnalisis('Se esperaba un valor, un identificador o un paréntesis izquierdo', token)

            if self.tokens.peek().tipo == TipoToken.OPERADORES_ARITMETICOS or self.tokens.peek().tipo == TipoToken.OPERADORES_LOGICOS or self.tokens.peek().tipo == TipoToken.OPERADORES_COMPARACION:
                nodo.hijos.append(self.operador())
                nodo.hijos.append(self.expresion())

            if self.tokens.peek().tipo == TipoToken.PARENTESIS_DER:
                next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de expresión incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def busqueda(self, token):
        """Analiza una búsqueda de variable o llamada de funcion."""
        if self.tokens.peek().tipo == TipoToken.PARENTESIS_IZQ:
            return self.llamada_funcion(token)
        if self.tokens.peek().tipo == TipoToken.PARENTESIS_CUADRADO_IZQ:
            return self.acceso_lista(token)
        return Nodo(TipoNodo.VARIABLE, token.lexema)

    def acceso_lista(self, token):
        """Analiza un acceso a lista."""
        try:
            nodo = Nodo(TipoNodo.ACCESO_LISTA, token.lexema)

            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_CUADRADO_IZQ:
                raise ErrorAnalisis('Se esperaba un paréntesis cuadrado izquierdo', token)

            nodo.hijos.append(self.expresion())

            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_CUADRADO_DER:
                raise ErrorAnalisis('Se esperaba un paréntesis cuadrado derecho', token)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de acceso a lista incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def operador(self):
        """Analiza un operador."""
        try:
            token = next(self.tokens)

            if token.tipo != TipoToken.OPERADORES_ARITMETICOS and token.tipo != TipoToken.OPERADORES_LOGICOS and token.tipo != TipoToken.OPERADORES_COMPARACION:
                raise ErrorAnalisis('Se esperaba un operador', token)

            return Nodo(TipoNodo.OPERADOR, token.lexema)
        except StopIteration:
            print("Error de análisis: Estructura de operador incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def llamada_funcion(self, token):
        """Analiza una llamada a función."""
        try:
            nodo = Nodo(TipoNodo.LLAMADA_FUNCION, token.lexema)

            token = next(self.tokens)

            if token.tipo != TipoToken.PARENTESIS_IZQ:
                raise ErrorAnalisis('Se esperaba un paréntesis izquierdo', token)

            nodo.hijos.append(self.argumentos())

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de llamada a función incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)

    def argumentos(self):
        """Analiza los argumentos de una función."""
        try:
            if self.tokens.peek().tipo == TipoToken.PARENTESIS_DER:
                return Nodo(TipoNodo.ARGUMENTOS, '')
        except StopIteration:
            print("Error de análisis: Estructura de argumentos incompleta.")
            exit(-1)
        
        nodo = Nodo(TipoNodo.ARGUMENTOS, '')

        while True:
            try:
                token = next(self.tokens)

                if token.tipo == TipoToken.PARENTESIS_DER:
                    break
                elif token.tipo == TipoToken.ENTERO or token.tipo == TipoToken.FLOTANTE or token.tipo == TipoToken.BOOLEANO or token.tipo == TipoToken.CADENA or token.tipo == TipoToken.IDENTIFICADOR:
                    nodo.hijos.append(self.expresion_llamada_funcion(token))
                else:
                    raise ErrorAnalisis('Se esperaba un valor, un identificador o una coma', token)
            except StopIteration:
                break
            except ErrorAnalisis as error:
                print(error)
                exit(-1)

        return nodo

    def expresion_llamada_funcion(self, token):
        """Analiza una expresión de una llamada a función."""
        try:
            if token.tipo == TipoToken.ENTERO or token.tipo == TipoToken.FLOTANTE or token.tipo == TipoToken.BOOLEANO or token.tipo == TipoToken.CADENA:
                nodo = Nodo(TipoNodo.EXPRESION, token.lexema)
            elif token.tipo == TipoToken.IDENTIFICADOR:
                nodo = self.busqueda(token)
            elif token.tipo == TipoToken.PARENTESIS_IZQ:
                nodo = Nodo(TipoNodo.AGRUPACION, '')
                nodo.hijos.append(self.expresion_llamada_funcion(next(self.tokens)))
            else:
                raise ErrorAnalisis('Se esperaba un valor, un identificador o un paréntesis izquierdo', token)

            if self.tokens.peek().tipo == TipoToken.OPERADORES_ARITMETICOS or self.tokens.peek().tipo == TipoToken.OPERADORES_LOGICOS or self.tokens.peek().tipo == TipoToken.OPERADORES_COMPARACION:
                nodo.hijos.append(self.operador())
                nodo.hijos.append(self.expresion_llamada_funcion(next(self.tokens)))

            if self.tokens.peek().tipo == TipoToken.COMA:
                next(self.tokens)

            return nodo
        except StopIteration:
            print("Error de análisis: Estructura de expresión de llamada a función incompleta.")
            exit(-1)
        except ErrorAnalisis as error:
            print(error)
            exit(-1)