 
import random

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

contador = 0
print("Contador: ", contador, )
while (contador < 10):
	contador_suma = contador + 1
	print("Contador suma:", contador_suma, )

random = random.randint(1, 10, )
