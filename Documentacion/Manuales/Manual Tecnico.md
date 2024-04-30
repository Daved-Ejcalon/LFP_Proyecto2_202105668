# LFP | PROYECTO 2  


# 📋 Indice
1. [Información](#información)
2. [Uso](#manual-de-usuario)
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

![Editor de texto](./Imagenes/ventana.png)

* **Menu archivo**: Se cuenta con varias opciones para el manejo de archivos, como abrir, guardar, guardar como y nuevo.

![Menu archivo](./Imagenes/archivo_menu.png)
![Abrir archivo](./Imagenes/entrada.png)

* **Analizar**: Se encarga de analizar el código de entrada y mostrar los tokens y errores generados, mostrando el resultado en el área de texto inferior.

![Analizar](./Imagenes/analizar.png)

* **Tokens**: Se encarga de mostrar los tokens generados en el análisis del código de entrada.

![Tokens](./Imagenes/tokens.png)

* **Errores**: Se encarga de mostrar los errores generados en el análisis del código de entrada.

![Errores](./Imagenes/errores.png)

# Manual Técnico

## Funcionamiento

### Compilador
El compilador se encarga de leer un archivo de entrada y generar un archivo de salida con el código de Python correspondiente a las sentencias de MongoDB.

Se utiliza el uso de estados para simular un autómata finito que permita reconocer las sentencias de entrada, luego se analizara los lexemas generados para verificar que coincidan con las sentencias permitidas.

### Tabla de tokens

![Tabla de tokens](./Imagenes/tabla_tokens.png)

### Autómata finito determinista

![AFD](./Imagenes/AFD.png)

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