

class Nodo:

    def __init__(self, tipo, contenido, atributos = None):
        self.tipo = tipo
        self.contenido = contenido
        self.atributos = atributos or {}
    
    def preorden(self) -> str:
        cadena = f"<'{self.tipo}', '{self.contenido}', {self.atributos}>" + "\n"
        if "hijos" in self.atributos:
            for hijo in self.atributos["hijos"]:
                cadena += hijo.preorden()
        return cadena
    
def generar(self, nivel=0) -> str:

    if self.tipo == "CAMPEONATO":
        codigo = ""
        for hijo in self.atributos["hijos"]:
            codigo += hijo.generar()
        return codigo
    
    elif self.tipo == "DECLARACIONES":
        codigo = ""
        for escuderia in self.atributos["escuderias"]:
            codigo += escuderia.generar()
        for funcion in self.atributos["funciones"]:
            codigo += funcion.generar()
        return codigo
    
    elif self.tipo == "ESCUDERIA":
        codigo = f"Escuderia: {self.atributos['identificador']}\n"
        codigo += "{\n"
        for miembro in self.atributos["miembros"]:
            codigo += f"\tMiembro: {miembro}\n"
        for recurso in self.atributos["recursos"]:
            codigo += f"\tRecurso: {recurso}\n"
        for auto in self.atributos["autos"]:
            codigo += f"\tAuto: {auto}\n"
        codigo += "}\n"
        return codigo
    
    elif self.tipo == "MIEMBRO":
        codigo = ""
        for piloto in self.atributos["pilotos"]:
            codigo += piloto.generar(nivel=1)
        for director in self.atributos["directores"]:
            codigo += director.generar(nivel=1)
        for ingeniero in self.atributos["ingenieros"]:
            codigo += ingeniero.generar(nivel=1)
        return codigo
    
    elif self.tipo == "PILOTO":
        return "\t"*nivel + f"self.{self.atributos['identificador']} = Piloto({self.atributos['entero']}, 
        {self.atributos['flotante1']}, {self.atributos['flotante2']}, {self.atributos['flotante3']}, 
        {self.atributos['flotante4']}, {self.atributos['flotante5']})\n"
    
    elif self.tipo == "DIRECTOR":
        return "\t"*nivel + f"self.{self.atributos['identificador']} = Director({self.atributos['flotante']}, 
        {self.atributos['entero1']}, {self.atributos['entero2']}, {self.atributos['entero3']}, 
        {self.atributos['flotante']})\n"

    
    elif self.tipo == "INGENIERO":
        return "\t"*nivel + f"self.{self.atributos['identificador']} = Ingeniero('{self.atributos['tipoIngeniero']}')\n"
    
    elif self.tipo == "RECURSOS":
        if 'presupuesto' in self.atributos:
            return self.atributos['presupuesto'].generar(nivel)
        elif 'capital' in self.atributos:
            return self.atributos['capital'].generar(nivel)
    
    elif self.tipo == "PRESUPUESTO":
        return "\t"*nivel + f"self.presupuesto = {self.atributos['flotante']}\n"
    
    elif self.tipo == "CAPITAL":
        return "\t"*nivel + f"self.capital = {self.atributos['flotante']}\n"
    
    elif self.tipo == "AUTO":
        return "\t"*nivel + f"self.{self.atributos['identificador']} = Auto({self.atributos['flotante1']}, 
        {self.atributos['flotante2']}, {self.atributos['flotante3']}, {self.atributos['flotante4']}, 
        {self.atributos['flotante5']})\n"
    
    elif self.tipo == "FUNCION":
        parametros = ", ".join([f"{param.generar()}: {tipo}" for param, tipo in zip(self.atributos["parametros"], self.atributos["tipos"])])
        codigo = "\t"*nivel + f"def {self.atributos['identificador']}({parametros}):\n"
        for instruccion in self.atributos["instrucciones"]:
            codigo += instruccion.generar(nivel + 1)
        if 'retorno' in self.atributos:
            codigo += "\t"*(nivel+1) + f"return {self.atributos['retorno'].generar()}\n"
        return codigo
    
    elif self.tipo == "RETORNO":
        return "\t"*nivel + f"return {self.atributos['expresion'].generar()}\n"

    elif self.tipo == "INSTRUCCIONES":
        codigo = ""
        for condicion in self.atributos["condiciones"]:
            codigo += condicion.generar(nivel)
        for ciclo in self.atributos["ciclos"]:
            codigo += ciclo.generar(nivel)
        for instruccion in self.atributos["instrucciones"]:
            codigo += instruccion.generar(nivel)
        return codigo
    
    elif self.tipo == "CONDICIONES":
        return f"if {self.atributos['expresion'].generar()}:\n\t{self.atributos['instrucciones'].generar()}\nelse:\n\t{self.atributos['instrucciones'].generar()}\n"

    elif self.tipo == "CICLOS":
        return f"while {self.atributos['expresion'].generar()}:\n\t{self.atributos['instrucciones'].generar()}\n"

    elif self.tipo == "INSTRUCCION":
        return f"{self.atributos['declaracionVariable'].generar()};\n{self.atributos['asignacion'].generar()};\n{self.atributos['llamadaFuncion'].generar()};\n"

    elif self.tipo == "DECLARACIONVARIABLE":
        return f"{self.atributos['tipoDato']} {self.atributos['asignacion'].generar()}"

    elif self.tipo == "ASIGNACION":
        return f"{self.atributos['identificador']} = {self.atributos['expresion'].generar()}"
    
    elif self.tipo == "EXPRESION":
        return f"({self.atributos['valor'].generar()} {self.atributos['operador']} {self.atributos['expresion'].generar()})" if self.atributos.get('operador') else f"{self.atributos['valor'].generar()}"

    elif self.tipo == "LLAMADA_FUNCION":
        parametros = ", ".join([param.generar() for param in self.atributos["parametros"] if param.tipo != "COMA"])
        if self.atributos["identificador"] == "imprimir":
           return "\t"*nivel + f"print({parametros})\n"
        return "\t"*nivel + f"{self.atributos['identificador']}({parametros})\n"
    
def __str__(self):
    return f"<'{self.tipo}', '{self.contenido}', {self.atributos}>"

def __repr__(self):
    return str(self)