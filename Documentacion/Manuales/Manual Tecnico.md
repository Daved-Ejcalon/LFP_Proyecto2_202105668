# LFP | PROYECTO 2  

# 📋 Indice
1. [Información](#información)
2. [Uso](#uso)
    1. [Requisitos](#requisitos)
    2. [Aplicación](#aplicación)
        1. [Entrada](#entrada)
        2. [Interfaz Gráfica](#interfaz-gráfica)
3. [Manual Técnico](#manual-técnico)
    1. [Funcionamiento](#funcionamiento)
        1. [Compilador](#compilador)
        2. [Tabla de tokens](#tabla-de-tokens)
        3. [Autómata finito determinista](#autómata-finito-determinista)
        4. [Gramática libre de contexto](#gramática-libre-de-contexto)
    2. [Herramientas utilizadas](#herramientas-utilizadas)
    3. [Codigo fuente](#codigo-fuente)


# Información
Herramienta que permite el diseño de sentencias de base de datos no relacionales de MongoDB de una forma sencilla para el usuario, con la ayuda de un compilador que permite compilar archivos de entrada y visualizar el resultado de un entorno externo.

# Uso

## Requisitos
- Python 3.8 o superior
- PyQt6

## Aplicación

### Entrada
La entrada podrá tener los siguientes formatos:
```
Funcion Nombre = nueva Funcion ( ) ;
Funcion Nombre = nueva Funcion ( "Identificador" ) ;
Funcion Nombre = nueva Funcion ( "Identificador", "JSON" ) ;
```

Entre las funciones que se pueden utilizar se encuentran:

- `CrearDB`
- `EliminarDB`
- `CrearColeccion`
- `EliminarColeccion`
- `InsertarUnico`
- `ActualizarUnico`
- `EliminarUnico`
- `BuscarUnico`
- `BuscarTodo`

### Interfaz Gráfica
La interfaz gráfica se encarga de mostrar al usuario una ventana con un editor de texto para ingresar las sentencias de entrada, un botón para compilar el archivo y un área de texto para mostrar el resultado de la compilación, al igual que tener la funcionalidad de poder ver los tokens y los errores generados.


* **Editor de texto**: Se encarga de mostrar el código de entrada, se puede escribir o abrir un archivo de texto en formato .lfp

![Editor de texto](https://i.ibb.co/TbK60p4/ventana.png)

* **Menu archivo**: Se cuenta con varias opciones para el manejo de archivos, como abrir, guardar, guardar como y nuevo.

![Abrir archivo](https://i.ibb.co/5x4gt8q/entrada.png)

* **Analizar**: Se encarga de analizar el código de entrada y mostrar los tokens y errores generados, mostrando el resultado en el área de texto inferior.

![Analizar](https://i.ibb.co/DR9BCr7/analizar.png)

* **Tokens**: Se encarga de mostrar los tokens generados en el análisis del código de entrada.

![Tokens](https://i.ibb.co/JxJvTHL/tokens.png)

* **Errores**: Se encarga de mostrar los errores generados en el análisis del código de entrada.

![Errores](https://i.ibb.co/8jrzxwd/errores.png)

# Manual Técnico

## Funcionamiento

### Compilador
El compilador se encarga de leer un archivo de entrada y generar un archivo de salida con el código de Python correspondiente a las sentencias de MongoDB.

Se utiliza el uso de estados para simular un autómata finito que permita reconocer las sentencias de entrada, luego se analizara los lexemas generados para verificar que coincidan con las sentencias permitidas.

### Tabla de tokens

![Tabla de tokens](https://i.ibb.co/6HS9Spv/tabla-tokens.png)

### Autómata finito determinista

![AFD](https://i.ibb.co/5sJzkDv/AFD.png)

### Gramática libre de contexto

```
S0 -> C S0
    | " " S1

S1 -> C S1
    | " " S2

S2 -> "=" S3

S3 -> C S3
    | " " S4

S4 -> C S4
    | "(" S5

S5 -> ")" S11
    | "\"" S6

S6 -> C S6
    | '"\"" S7

S7 -> ")" S11
    | "," S8

S8 -> "\"" S9

S9 -> JSON S9
    | "\"" S10

S10 -> ")" S11

S11 -> ";" S12
```


## Herramientas utilizadas

- Python
    - PyQt6

## Codigo fuente
##### Clase Abstract.py: 
Este fragmento de código define una clase abstracta llamada Expression que es parte de una jerarquía de clases para representar expresiones en un lenguaje de programación o un sistema de análisis.

![Abstract](https://i.ibb.co/w7kgmqF/Abstract.png)



##### Clase Lexema.py: 
Define una clase Lexema de la subclase de la clase abstracta Expression, representa diferentes tipos de elementos léxicos en un analizador léxico.

Definición de la clase Lexema:

La clase Lexema hereda de la clase Expression.Tiene un constructor init que inicializa los atributos lexema, tipo, fila y columna. lexema parece ser el contenido del lexema, tipo el tipo de lexema (por ejemplo, "FUNCION", "NOMBRE", etc.), y fila y columna representan la ubicación del lexema en el código fuente.
    
**Define los métodos operar, getFila, getColumna, getTipo y str.**

* operar(self, arbol=None): Este método devuelve el contenido del lexema.
* getFila(self): Este método devuelve la fila donde se encuentra el lexema en el código fuente.
* getColumna(self): Este método devuelve la columna donde se encuentra el lexema en el código fuente.
* getTipo(self): Este método devuelve el tipo del lexema.
* str(self): Este método devuelve una representación en cadena del lexema.

Métodos getFila y getColumna: Estos métodos llaman al método correspondiente de la clase padre (Expression) para obtener la fila y la columna del lexema.

![Lexema](https://i.ibb.co/mB6M4Xd/Lexema.png)

##### Clase Errores.py: 
Define la clase llamada Errores, que es una subclase de Expression importada desde Abstract.Abstract. Aquí hay una descripción de los principales elementos de esta clase:

* **Atributos**:
        Lexema: Representa el lexema relacionado con el error.
        Tipo: Tipo de error (por ejemplo, "Lexico").
        Mensaje: Descripción detallada del error.
        Fila: Número de fila donde ocurrió el error.
        Columna: Número de columna donde ocurrió el error.

* **Métodos**:
        init: Método constructor que inicializa los atributos de la clase.
        operar: Método que devuelve una representación del error.
        getColumna: Método para obtener la columna donde ocurrió el error.
        getFila: Método para obtener la fila donde ocurrió el error.
        getTipo: Método para obtener el tipo de error.
        getMensaje: Método para obtener el mensaje detallado del error.
        getLexema: Método para obtener el lexema relacionado con el error.

Esta clase parece estar diseñada para representar y manipular errores que ocurren durante el análisis léxico de algún proceso. La estructura y los métodos definidos permiten acceder a información detallada sobre el error, incluido su tipo, mensaje, ubicación en el código fuente, etc.

![Errores](https://i.ibb.co/s1LBsc1/Errores.png)

##### Clase Analizador.py: 
Define una clase Analizador que se utiliza para analizar un archivo de entrada y generar un archivo de salida con el código de Python correspondiente a las sentencias de MongoDB. En resumen general el script es parte principal del analizador léxico para un lenguaje de programación específico. Acontinuicion se detallan las funciones principales del script:

* **Importaciones**: Importa algunas clases y funciones necesarias de otros módulos.
 -from Instrucciones.Resultado import * (Clase que maneja los -resultados)
 -from Error.Errores import * (Clase que maneja errores)
 -from Abstract.Lexema import *(Clase que maneja los lexemas)
 -import json (Libreria para manejar JSON)

* **Inicialización de variables globales**: Inicializa algunas variables globales necesarias para el análisis léxico.

* **Función instruccion**: Esta función toma una cadena como entrada y realiza el análisis léxico para identificar diferentes elementos léxicos, como funciones, nombres, asignaciones, etc. Utiliza un enfoque basado en estados (estado_actual) para determinar el tipo de lexema actual y cómo debe analizarse.

* **Funciones armar_lexema**: Estas funciones ayudan a construir lexemas a partir de una cadena de entrada. Por ejemplo, armar_lexema crea un lexema hasta que encuentra un delimitador como un espacio, un salto de línea o un paréntesis.

* **Función analizar**: Esta función utiliza los resultados del análisis léxico para producir una lista de instrucciones. Utiliza una instancia de Resultado para procesar los lexemas y generar las instrucciones correspondientes.

* **Función recuperacion**: Esta función maneja la recuperación de errores durante el análisis léxico. En caso de error, descarta los caracteres restantes hasta encontrar un delimitador (en este caso, un punto y coma).

* Otras funciones auxiliares: Hay algunas funciones adicionales para manejar errores, recuperación de errores y reiniciar el analizador.


##### Clase Funcion.py: 
    
* **Clase Funcion**: Esta clase sirve como una clase base para otras clases que representan funciones específicas en la base de datos. Tiene un método __str__ que devuelve una representación de cadena de la función.

* **Clase CrearDB(Funcion)**: Esta clase representa la operación de crear una base de datos. Implementa un método analizar que verifica si los parámetros necesarios están presentes y devuelve la instancia de la clase con los atributos establecidos si la verificación es exitosa.

* **Clase EliminarBD(Funcion)**: Similar a CrearDB, pero representa la operación de eliminar una base de datos.

* **Clase CrearColeccion(Funcion)**: Representa la operación de crear una colección en la base de datos.

* **Clase EliminarColeccion(Funcion)**: Similar a CrearColeccion, pero representa la operación de eliminar una colección.

* **Clase InsertarUnico(Funcion)**: Representa la operación de insertar un documento en una colección.

* **Clase ActualizarUnico(Funcion)**: Representa la operación de actualizar un documento en una colección.

* **Clase EliminarUnico(Funcion)**: Representa la operación de eliminar un documento de una colección.

* **Clase BuscarTodo(Funcion)**: Representa la operación de buscar todos los documentos en una colección.

* **Clase BuscarUnico(Funcion)**: Representa la operación de buscar un documento específico en una colección.



##### Clase Resultado.py: 

Este fragmento de código define la clase Resultado, que se utiliza para analizar y procesar una lista de lexemas (tokens) y generar el resultado correspondiente, que puede ser una función específica o un error.

Esta clase toma una lista de lexemas y una lista de errores como entrada. 

* **Metodos**:
getLexemas(): Retorna la lista de lexemas.
getResultado(): Analiza la lista de lexemas para determinar qué función debe ejecutarse y devuelve el resultado junto con la cantidad de lexemas utilizados en la operación. Si no se encuentra una función válida, se agrega un error a la lista de errores.

El código utiliza una estructura de coincidencia (match) para determinar qué función debe ejecutarse según el primer lexema de la lista. Luego, instancia la clase correspondiente de la función y llama al método analizar() de esa clase para realizar el análisis. Finalmente, devuelve el resultado y la cantidad de lexemas utilizados en la operación.

![Funcion](https://i.ibb.co/Cw4bp7y/Funcion.png)
