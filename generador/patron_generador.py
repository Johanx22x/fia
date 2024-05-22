"""patron_generador.py: Implementación del patrón de diseño Visitor."""

from analizador.nodo import Nodo, TipoNodo

class Visitante:
    """Clase que visita los nodos del árbol sintáctico abstracto."""

    tabuladores = 0
    
    def retornar_tabuladores(self) -> str:
        """Retorna una cadena con la cantidad de tabuladores necesarios."""
        return " " * self.tabuladores

    def incrementar_tabuladores(self) -> None:
        """Incrementa la cantidad de tabuladores."""
        self.tabuladores += 1

    def decrementar_tabuladores(self) -> None:
        """Decrementa la cantidad de tabuladores."""
        self.tabuladores -= 1

    def visitar(self, nodo : TipoNodo) -> str:
        """Visita un nodo del árbol sintáctico abstracto."""
        visitante = getattr(self, f'visitar_{nodo.tipo.name.lower()}')
        return visitante(nodo)

    def visitar_campeonato(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo campeonato."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_escuderia(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo escuderia."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'escuderia ' + nodo.lexema + ' {\n' + '\n'.join(instrucciones) + '\n' + self.retornar_tabuladores() + '}'

    def visitar_miembros(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo miembros."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)
    
    def visitar_piloto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo piloto."""
        return f'piloto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitar_director(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo director."""
        return f'director {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'
    
    def visitar_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ingeniero."""
        return f'ingeniero {nodo.lexema} {nodo.hijos[0]};'
    
    def visitar_recursos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo recursos."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_presupuesto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo presupuesto."""
        return f'presupuesto {nodo.lexema};'

    def visitar_capital(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo capital."""
        return f'capital {nodo.lexema};'

    def visitar_auto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo auto."""
        return f'auto {nodo.lexema} {"".join(self.visitar(hijo) for hijo in nodo.hijos)};'

    def visitar_funcion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo función."""
        instrucciones = []
        self.incrementar_tabuladores()
        if len(nodo.hijos) > 2:
            for hijo in nodo.hijos[1:]:
                instrucciones.append(self.visitar(hijo))
            self.decrementar_tabuladores()
            return 'orden ' + nodo.lexema + ' (' + self.visitar(nodo.hijos[0]) + ') ' + self.visitar(nodo.hijos[1]) + ' {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'orden ' + nodo.lexema + ' (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'
 
    def visitar_llamada_funcion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo llamada_función."""
        argumentos = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return f'{nodo.lexema}({argumentos});'

    def visitar_parametros(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo parámetros."""
        parametros = ', '.join(self.visitar(hijo) for hijo in nodo.hijos)
        return parametros
    
    def visitar_parametro(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo parámetro."""
        return f'{self.visitar(nodo.hijos[0])} {nodo.lexema}'
    
    def visitar_tipo_dato(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_dato."""
        return nodo.lexema

    def visitar_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo variable."""
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])}"
        return f'{nodo.lexema}'

    def visitar_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo retorno."""
        return f'confirmacion {self.visitar(nodo.hijos[0])}'

    def visitar_tipo_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_retorno."""
        return f'[{nodo.lexema}]'

    def visitar_instrucciones(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo instrucciones."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return '\n'.join(instrucciones)

    def visitar_condiciones(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo condiciones."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'box (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'
    
    def visitar_condiciones_out(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo condiciones_out."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        return '} out {\n' + '\n'.join(instrucciones) 

    def visitar_ciclos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ciclos."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'circuito (' + self.visitar(nodo.hijos[0]) + ') {\n' + '\n'.join(instrucciones[1:]) + '\n' + self.retornar_tabuladores() + '}'  

    def visitar_instruccion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo instrucción."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_declaracion_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo declaración_variable."""
        return f'{self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};'

    def visitar_asignacion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo asignación."""
        return f'{self.visitar(nodo.hijos[0])} = {self.visitar(nodo.hijos[1])}'
    
    def visitar_expresion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo expresión."""
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])};"
        return f'{nodo.lexema}'

    def visitar_operador(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo operador."""
        return f"{nodo.lexema}"

    def visitar_argumentos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo argumentos."""
        return ', '.join(self.visitar(hijo) for hijo in nodo.hijos)

    def visitar_agrupacion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo agrupación."""
        return f'({self.visitar(nodo.hijos[0])})'
    
    def visitar_acceso_lista(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo acceso_lista."""
        hijos_visitados = [self.visitar(hijo) for hijo in nodo.hijos]
        return f'{nodo.lexema}[{", ".join(hijos_visitados)}]'

    def visitar_valor(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo valor."""
        return f' {nodo.lexema}'
    
    def visitar_tipo_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_ingeniero."""
        return f' {nodo.lexema}'
