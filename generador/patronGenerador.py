
from analizador.nodo import Nodo, TipoNodo

class Visitante:

    tabuladores = 0

    def visitar(self, nodo : TipoNodo):
        resultado = ''

        if nodo.tipo is TipoNodo.CAMPEONATO:
            print("Campeonato 0")
            resultado = self.visitarCampeonato(nodo)

        elif nodo.tipo is TipoNodo.ESCUDERIA:
            print("Escuderia 1")
            resultado = self.visitarEscuderia(nodo)

        elif nodo.tipo is TipoNodo.MIEMBROS:
            print("Miembros 2")
            resultado = self.visitarMiembros(nodo)

        elif nodo.tipo is TipoNodo.PILOTO:
            print("Piloto 3")
            resultado = self.visitarPiloto(nodo)

        elif nodo.tipo is TipoNodo.DIRECTOR:
            print("DIRECTOR 4")
            resultado = self.visitarDirector(nodo)

        elif nodo.tipo is TipoNodo.INGENIERO:
            print("INGENIERO 5")
            resultado = self.visitarIngeniero(nodo)

        elif nodo.tipo is TipoNodo.RECURSOS:
            print("RECURSOS 6")
            resultado = self.visitarRecursos(nodo)

        elif nodo.tipo is TipoNodo.PRESUPUESTO:
            print("PRESUPUESTO 7")
            resultado = self.visitarPresupuesto(nodo)

        elif nodo.tipo is TipoNodo.CAPITAL:
            print("CAPITAL 8")
            resultado = self.visitarCapital(nodo)

        elif nodo.tipo is TipoNodo.AUTO:
            print("AUTO 9")
            resultado = self.visitarAuto(nodo)

        elif nodo.tipo is TipoNodo.FUNCION:
            print("FUNCION 10")
            resultado = self.visitarFuncion(nodo)
        
        elif nodo.tipo is TipoNodo.LLAMADA_FUNCION:
            print("LLAMADA_FUNCION 11")
            resultado = self.visitarLlamadaFuncion(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS:
            print("PARAMETROS 12")
            resultado = self.visitarParametros(nodo)

        elif nodo.tipo is TipoNodo.PARAMETRO:
            print("PARAMETRO 13")
            resultado = self.visitarParametro(nodo)

        elif nodo.tipo is TipoNodo.TIPO_DATO:
            print("TIPO_DATO 14")
            resultado = self.visitarTipoDato(nodo)
        
        elif nodo.tipo is TipoNodo.VARIABLE:
            print("VARIABLE 15")
            resultado = self.visitarVariable(nodo)

        elif nodo.tipo is TipoNodo.RETORNO:
            print("RETORNO 16")
            resultado = self.visitarRetorno(nodo)
        
        elif nodo.tipo is TipoNodo.INSTRUCCIONES:
            print("INSTRUCCIONES 17")
            resultado = self.visitarInstrucciones(nodo)
        
        elif nodo.tipo is TipoNodo.CONDICIONES:
            print("CONDICIONES 18")
            resultado = self.visitarCondiciones(nodo)
        
        elif nodo.tipo is TipoNodo.CICLOS:
            print("CICLOS 19")
            resultado = self.visitarCiclos(nodo)

        elif nodo.tipo is TipoNodo.INSTRUCCION:
            print("INSTRUCCION 20")
            resultado = self.visitarInstruccion(nodo)
        
        elif nodo.tipo is TipoNodo.DECLARACION_VARIABLE:
            print("DECLARACION_VARIABLE 21")
            resultado = self.visitarDeclaracionVariable(nodo)
        
        elif nodo.tipo is TipoNodo.ASIGNACION:
            print("ASIGNACION 22")
            resultado = self.visitarAsignacion(nodo)
        
        elif nodo.tipo is TipoNodo.EXPRESION:
            print("EXPRESION 23")
            resultado = self.visitarExpresion(nodo)
        
        elif nodo.tipo is TipoNodo.OPERADOR:
            print("OPERADOR 24")
            resultado = self.visitarOperador(nodo)
        
        elif nodo.tipo is TipoNodo.ARGUMENTOS:
            print("ARGUMENTOS 25")
            resultado = self.visitarArgumentos(nodo)
        
        elif nodo.tipo is TipoNodo.AGRUPACION:
            print("AGRUPACION 26")
            resultado = self.visitarAgrupacion(nodo)

        elif nodo.tipo is TipoNodo.ACCESO_LISTA:
            print("ACCESO_LISTA 27")
            resultado = self.visitarAccesoLista(nodo)

        elif nodo.tipo is TipoNodo.VALOR:
            print("VALOR 28")
            resultado = self.visitarValor(nodo)
        
        elif nodo.tipo is TipoNodo.TIPO_INGENIERO:
            print("TIPO_INGENIERO 29")
            resultado = self.visitarTipoIngeniero(nodo)
        
        elif nodo.tipo is TipoNodo.CONDICIONESOUT:
            print("CONDICIONESOUT 30")
            resultado = self.visitarCondicionesOut(nodo)

        return resultado

    def visitarCampeonato(self, nodo):
        print()
        instrucciones = []
        #print('  ' * nivel + str(nodo))
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitarEscuderia(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornarTabuladores() + self.visitar(hijo))
        self.decrementarTabuladores()
        return 'escuderia ' + nodo.lexema + ' {\n' + '\n'.join(instrucciones) + '\n' + self.retornarTabuladores() + '}'

    def visitarMiembros(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)
    
    def visitarPiloto(self, nodo):
        return f'piloto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitarDirector(self, nodo):
        return f'director {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitarIngeniero(self, nodo):
        return f'ingeniero {nodo.lexema} {nodo.hijos[0]};'
    
    def visitarRecursos(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitarPresupuesto(self, nodo):
        return f'presupuesto {nodo.lexema};'

    def visitarCapital(self, nodo):
        return f'capital {nodo.lexema};'

    def visitarAuto(self, nodo):
        return f'auto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'

    def visitarFuncion(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementarTabuladores()
        return 'orden ' + nodo.lexema + ' (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornarTabuladores() + '}'
 
    def visitarLlamadaFuncion(self, nodo):
        argumentos = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return f'{nodo.lexema}({argumentos});'

    def visitarParametros(self, nodo):
        parametros = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return parametros
    
    def visitarParametro(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} {nodo.lexema}'
    
    def visitarTipoDato(self, nodo):
        return nodo.lexema

    def visitarVariable(self, nodo):
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])}"
        return f'{nodo.lexema}'

    def visitarRetorno(self, nodo):
        return f'confirmacion {self.visitar(nodo.hijos[0])}'

    def visitarInstrucciones(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornarTabuladores() + self.visitar(hijo))
        self.decrementarTabuladores()
        return '\n'.join(instrucciones)

    def visitarCondiciones(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornarTabuladores() + self.visitar(hijo))
        self.decrementarTabuladores()
        return 'box (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornarTabuladores() + '}'
    
    def visitarCondicionesOut(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornarTabuladores() + self.visitar(hijo))
        self.decrementarTabuladores()
        return '} out {\n' + '\n'.join(instrucciones) 

    def visitarCiclos(self, nodo):
        instrucciones = []
        self.incrementarTabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementarTabuladores()
        return 'circuito (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornarTabuladores() + '}'  

    def visitarInstruccion(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitarDeclaracionVariable(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};'

    def visitarAsignacion(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} = {self.visitar(nodo.hijos[1])}'
    
    def visitarExpresion(self, nodo):
        print(self.tabuladores)
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};"
        return f'{nodo.lexema}'
        #return f'{nodo.lexema};'

    def visitarOperador(self, nodo):
        return f"{nodo.lexema}"

    def visitarArgumentos(self, nodo):
        return ', '.join(self.visitar(hijo) for hijo in nodo.hijos)

    def visitarAgrupacion(self, nodo):
        return f'({self.visitar(nodo.hijos[0])})'
    
    def visitarAccesoLista(self, nodo):
        hijos_visitados = [self.visitar(hijo) for hijo in nodo.hijos]
        return f'{nodo.lexema}[{", ".join(hijos_visitados)}]'

    def visitarValor(self, nodo):
        return f' {nodo.lexema}'
    
    def visitarTipoIngeniero(self, nodo):
        return f' {nodo.lexema}'
    
    def retornarTabuladores(self):
        return " " * self.tabuladores

    def incrementarTabuladores(self):
        self.tabuladores += 1

    def decrementarTabuladores(self):
        self.tabuladores -= 1
