# FIA

Este proyecto es un transpilador diseñado para convertir código FIA en Python.
FIA es un lenguaje de programación inspirado en el campeonato de F1. La idea es
crear un lenguaje en el que alguien pueda recrear fácilmente un torneo de F1
utilizando las estructuras personalizadas y únicas que ofrece el lenguaje.

___

## Estructura del proyecto

### `gramatica`:

En esta carpeta se encuentran los archivos relacionados con la gramática del    
lenguaje (EBNF, ejemplos de código, etc).

### `explorador`:

En esta carpeta se encuentran los archivos relacionados con el explorador del
lenguaje, el encargado de generar los componentes léxicos.

### `utilidades`:

En esta carpeta se encuentran los archivos relacionados con las utilidades
necesarias para el proyecto, manejo de errores, etc.

### `analizador`:

En esta carpeta se encuentran los archivos relacionados con el analizador
sintáctico del lenguaje, el encargado de generar el árbol de análisis.

### `verificador`:

En esta carpeta se encuentran los archivos relacionados con el verificador del
lenguaje, el encargado de verificar la semántica del código.

### `generador`:

En esta carpeta se encuentran los archivos relacionados con el generador de 
código del lenguaje, el encargado de generar el código Python a partir del
código FIA.
