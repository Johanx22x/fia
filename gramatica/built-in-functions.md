# Funciones del ambiente estándar

## `radio()`

Es una función equivalente a `print()` que imprime el texto en la consola.

```
radio("Hola mundo");
```

## `avg()`

Esta función calcula el promedio o la puntuación, dependiendo del tipo de
objeto que se le envía como argumento. En el caso de los pilotos, calcula su
puntuación.

```
avg([1, 2, 3, 4, 5]);
avg(piloto);
```

## `carrera()`

Esta función permite a las escuderias participar en una carrera. La función
recibe como argumento dos o más escuderias y retorna la escuderia ganadora.

```
carrera(escuderia1, escuderia2, escuderia3);
```

## `negociacion()`

Esta función se utiliza para tramitar cambios en las propiedades de cada
escudería, como personal y recursos.

Parámetros:

- escuderia1: La primera escudería involucrada en la negociación. Esta es la que proporciona el recurso.
- escuderia2: La segunda escudería involucrada en la negociación. Esta es la que recibe el recurso.
- propiedad: La propiedad o recurso que se desea intercambiar.
- cantidad (opcional): La cantidad del recurso que se intercambiará, en caso de ser un recurso.

```
negociacion(escuderia1, escuderia2, ingeniero);
negociacion(escuderia1, escuderia2, "capital", 100);
```

## `distancia()`

Esta función calcula la distancia ("longitud") de una cadena de texto.

```
distancia("Hola mundo"); // 10
```
