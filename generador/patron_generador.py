"""patron_generador.py: Implementación del patrón de diseño Visitor."""

from analizador.nodo import Nodo, TipoNodo

class Visitante:
    """Clase que visita los nodos del árbol sintáctico abstracto."""

    tabuladores = 0
    
    def retornar_tabuladores(self):
        return " " * self.tabuladores

    def incrementar_tabuladores(self):
        self.tabuladores += 1

    def decrementar_tabuladores(self):
        self.tabuladores -= 1

    def visitar(self, nodo : TipoNodo) -> str:
        """Visita un nodo del árbol sintáctico abstracto."""
        visitante = getattr(self, f'visitar_{nodo.tipo.name.lower()}')
        return visitante(nodo)

    def visitar_campeonato(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_escuderia(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'escuderia ' + nodo.lexema + ' {\n' + '\n'.join(instrucciones) + '\n' + self.retornar_tabuladores() + '}'

    def visitar_miembros(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)
    
    def visitar_piloto(self, nodo):
        return f'piloto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitar_director(self, nodo):
        return f'director {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitar_ingeniero(self, nodo):
        return f'ingeniero {nodo.lexema} {nodo.hijos[0]};'
    
    def visitar_recursos(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_presupuesto(self, nodo):
        return f'presupuesto {nodo.lexema};'

    def visitar_capital(self, nodo):
        return f'capital {nodo.lexema};'

    def visitar_auto(self, nodo):
        return f'auto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'

    def visitar_funcion(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'orden ' + nodo.lexema + ' (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'
 
    def visitar_llamada_funcion(self, nodo):
        argumentos = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return f'{nodo.lexema}({argumentos});'

    def visitar_parametros(self, nodo):
        parametros = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return parametros
    
    def visitar_parametro(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} {nodo.lexema}'
    
    def visitar_tipo_dato(self, nodo):
        return nodo.lexema

    def visitar_variable(self, nodo):
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])}"
        return f'{nodo.lexema}'

    def visitar_retorno(self, nodo):
        return f'confirmacion {self.visitar(nodo.hijos[0])}'

    def visitar_instrucciones(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return '\n'.join(instrucciones)

    def visitar_condiciones(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'box (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'
    
    def visitar_condiciones_out(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return '} out {\n' + '\n'.join(instrucciones) 

    def visitar_ciclos(self, nodo):
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'circuito (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'  

    def visitar_instruccion(self, nodo):
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_declaracion_variable(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};'

    def visitar_asignacion(self, nodo):
        return f'{self.visitar(nodo.hijos[0])} = {self.visitar(nodo.hijos[1])}'
    
    def visitar_expresion(self, nodo):
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};"
        return f'{nodo.lexema}'

    def visitar_operador(self, nodo):
        return f"{nodo.lexema}"

    def visitar_argumentos(self, nodo):
        return ', '.join(self.visitar(hijo) for hijo in nodo.hijos)

    def visitar_agrupacion(self, nodo):
        return f'({self.visitar(nodo.hijos[0])})'
    
    def visitar_acceso_lista(self, nodo):
        hijos_visitados = [self.visitar(hijo) for hijo in nodo.hijos]
        return f'{nodo.lexema}[{", ".join(hijos_visitados)}]'

    def visitar_valor(self, nodo):
        return f' {nodo.lexema}'
    
    def visitar_tipo_ingeniero(self, nodo):
        return f' {nodo.lexema}'
