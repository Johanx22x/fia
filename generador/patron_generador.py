"""patron_generador.py: Implementación del patrón de diseño Visitor."""

from analizador.nodo import Nodo, TipoNodo

class Visitante:
    """Clase que visita los nodos del árbol sintáctico abstracto."""

    tabuladores = 0
    instrucciones1 = []

    activadoEscuderia = False
    activandoEscuderiaAux = False

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
        self.instrucciones11 = []
        self.incrementar_tabuladores()
        clase = f'class Escuderia:\n' \
                f'{self.retornar_tabuladores()}def __init__(self, nombre, pilotos, director, ingenieros, presupuesto, capital, autos):\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.nombre = nombre\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.pilotos = pilotos\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.director = director\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.ingenieros = ingenieros\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.presupuesto = presupuesto\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.capital = capital\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.autos = autos\n' \
                f'\nclass Piloto:\n' \
                f'{self.retornar_tabuladores()}def __init__(self, nombre, *stats):\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.nombre = nombre\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.stats = stats\n' \
                f'\nclass Director:\n' \
                f'{self.retornar_tabuladores()}def __init__(self, nombre, *stats):\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.nombre = nombre\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.stats = stats\n' \
                f'\nclass Ingeniero:\n' \
                f'{self.retornar_tabuladores()}def __init__(self, nombre, especialidad):\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.nombre = nombre\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.especialidad  = especialidad\n' \
                f'\nclass Auto:\n' \
                f'{self.retornar_tabuladores()}def __init__(self, nombre, *stats):\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.nombre = nombre\n' \
                f'{self.retornar_tabuladores()}{self.retornar_tabuladores()}self.stats  = stats\n'
                         
        if self.activadoEscuderia == False:
            self.activadoEscuderia = True
            self.activandoEscuderiaAux = True
            self.instrucciones1.append(clase) 
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        self.decrementar_tabuladores()
        if self.activandoEscuderiaAux == True:
            self.activandoEscuderiaAux = False
            inicio = '\n'.join(self.instrucciones1) + '\n' + nodo.lexema + ' = Escuderia(' + '\n nombre = "' + nodo.lexema + '",\n' + ' pilotos=[\n'+ '\n'.join(instrucciones) + '\n' + self.retornar_tabuladores()
            self.incrementar_tabuladores()
            return inicio + f'{self.retornar_tabuladores()}]\n)'
        else:
            inicio = '\n' + nodo.lexema + ' = Escuderia(' + '\n nombre = "' + nodo.lexema + '",\n' + ' pilotos=[\n'+ '\n'.join(instrucciones) + '\n' + self.retornar_tabuladores()

            self.incrementar_tabuladores()
            return inicio + f'{self.retornar_tabuladores()}]\n)'

    def visitar_miembros(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo miembros."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)
    
    def visitar_piloto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo piloto y lo agrega a la lista temporal de pilotos."""
        self.incrementar_tabuladores()
        piloto = f'{self.retornar_tabuladores()}Piloto("{nodo.lexema}",{",".join(self.visitar(hijo) for hijo in nodo.hijos)}),'
        self.decrementar_tabuladores()
        return piloto
    
    def visitar_director(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo director."""
        return f'],\n{self.retornar_tabuladores()}director=Director("{nodo.lexema}",{",".join(self.visitar(hijo) for hijo in nodo.hijos)}),\n{self.retornar_tabuladores()}ingenieros=['
    
    def visitar_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ingeniero"""
        self.incrementar_tabuladores()
        ingeniero = f'{self.retornar_tabuladores()}Ingeniero("{nodo.lexema}",{",".join(self.visitar(hijo) for hijo in nodo.hijos)}),'
        self.decrementar_tabuladores()
        return ingeniero
    
    def visitar_recursos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo recursos."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_presupuesto(self, nodo: Nodo) -> str:
        return f'],\n{self.retornar_tabuladores()}presupuesto={nodo.lexema},'

    def visitar_capital(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo capital."""
        return f'capital={nodo.lexema}, \n{self.retornar_tabuladores()}autos=['

    def visitar_auto(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo auto y lo agrega a la lista temporal de autos."""
        self.incrementar_tabuladores()
        auto = f'{self.retornar_tabuladores()}Auto("{nodo.lexema}",{",".join(self.visitar(hijo) for hijo in nodo.hijos)}),'
        self.decrementar_tabuladores()
        return auto

    def visitar_funcion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo función."""
        instrucciones = []
        self.incrementar_tabuladores()
        if len(nodo.hijos) > 2:
            for hijo in nodo.hijos[1:]:
                instrucciones.append(self.visitar(hijo))
            self.decrementar_tabuladores()
            return 'def ' + nodo.lexema + '(' + self.visitar(nodo.hijos[0]) + ')' + ' -> ' +  self.visitar(nodo.hijos[1]) + ':' '\n' + '\n'.join(instrucciones[1:]) + self.retornar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'def ' + nodo.lexema + '(' + self.visitar(nodo.hijos[0]) + '):\n' + '\n'.join(instrucciones[1:]) + self.retornar_tabuladores()
 
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
        return f'{nodo.lexema}: {self.visitar(nodo.hijos[0])}'
    
    def visitar_tipo_dato(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_dato."""
        tipo_tipo_dato = {
            "entero": "int",
            "flotante": "float",
            "cadena": "str",
            "booleano": "bool",
            # 
        }
        if nodo.lexema.lower() in tipo_tipo_dato:
            return tipo_tipo_dato[nodo.lexema.lower()]
        else:
            return nodo.lexema 

    def visitar_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo variable."""
        if len(nodo.hijos) > 0:
            return f"{nodo.lexema} {self.visitar(nodo.hijos[0])} {self.visitar(nodo.hijos[1])}"
        return f'{nodo.lexema}'

    def visitar_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo retorno."""
        return f'return {self.visitar(nodo.hijos[0])}' + '\n'

    def visitar_tipo_retorno(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_retorno."""
        tipo_retorno = {
            "entero": "int",
            "flotante": "float",
            "cadena": "str",
            "booleano": "bool",
            # 
        }
        if nodo.lexema.lower() in tipo_retorno:
            return tipo_retorno[nodo.lexema.lower()]
        else:
            return nodo.lexema 

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
        for hijo in nodo.hijos:
            instrucciones.append(self.retornar_tabuladores() + self.visitar(hijo))
        return 'if (' + self.visitar(nodo.hijos[0]) + '):\n' + '\n'.join(instrucciones[1:])
    
    def visitar_condiciones_out(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo condiciones_out."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return 'else:\n' + '\n'.join(instrucciones)

    def visitar_ciclos(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo ciclos."""
        instrucciones = []
        self.incrementar_tabuladores()
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        self.decrementar_tabuladores()
        return 'while (' + self.visitar(nodo.hijos[0]) + '): \n' + '\n'.join(instrucciones[1:])

    def visitar_instruccion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo instrucción."""
        instrucciones = []
        for hijo in nodo.hijos:
            instrucciones.append(self.visitar(hijo))
        return '\n'.join(instrucciones)

    def visitar_declaracion_variable(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo declaración_variable."""
        return f'{self.visitar(nodo.hijos[1])}'

    def visitar_asignacion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo asignación."""
        return f'{self.visitar(nodo.hijos[0])} = {self.visitar(nodo.hijos[1])}'
    
    def visitar_expresion(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo expresión."""
        valores_booleanos = {
            "verdadero": "True",
            "falso": "False"
        }
        if nodo.lexema.lower() in valores_booleanos:
            return valores_booleanos[nodo.lexema.lower()]
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
        primer_hijo = f'[{self.visitar(nodo.hijos[0])}]'
        otros_hijos = [self.visitar(hijo) for hijo in nodo.hijos[1:]]
        hijos_visitados = [primer_hijo] + otros_hijos
        return f'{nodo.lexema}{" ".join(hijos_visitados)}'

    def visitar_valor(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo valor."""
        return f' {nodo.lexema}'
    
    def visitar_tipo_ingeniero(self, nodo: Nodo) -> str:
        """Visita un nodo de tipo tipo_ingeniero."""
        return f'"{nodo.lexema}"'
