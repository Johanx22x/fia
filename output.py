 
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

Ferrari = Escuderia('Ferrari',
	[Piloto('sebastianVettel', '321''213.2''123.1''32.1''43.3'),],
	[Director('totoWolf', '12.2''21''4''32''94.2'),],
	[Ingeniero('marc', 'Mecanica'),Ingeniero('jorge', 'Aerodinamica'),],
	1000000.0,
	321312.42,
	[Auto('w11', '213.0''32.2''321.2''31.1''32.1'),Auto('f_s2', '32.1''32.1''32.1''32.1''32.1'),]
	)
numero = 1
while (numero < 10):
	print(numero, )
	numero = numero + 1

