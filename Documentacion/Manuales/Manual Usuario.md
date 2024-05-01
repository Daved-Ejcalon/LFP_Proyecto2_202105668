## MANUAL DE USUARIO
#### LENGUAJES FORMALES Y DE PROGRAMACIÓN, B+ 
#### DAVED ABSHALON EJCALON CHONAY - 202105668

### Requisitos

- **Sistema operativo:** Windows 10
- **Procesador:** Intel Core 2 Duo E8200, AMD Phenom II X6 1075 a 3,0 GHz
- **Memoria:** 1 GB de RAM
- **Almacenamiento:** 1 GB de espacio disponible
- **Tarjeta gráfica:** NVIDIA GT 630 / AMD HD 7750
- **Internet:** Acceso a internet, con cualquier explorador web
- **Visual Studio:** Con Python instalado

### Inicio

Para poder utilizar el programa, el usuario deberá iniciar el programa en el IDE Visual Studio Code. Al iniciar el programa, se desplegará un cuadro de diálogo donde se mostrarán las opciones principales del programa.

Entre las opciones del programa están "Archivo", "Analizar", "Tokens" y "Errores". En la primera opción llamada "Archivo" están las siguientes sub-opciones para el funcionamiento:

![Inicio](https://i.ibb.co/jLV0KyK/1.png)

### Menú Archivo

1. **Nuevo:** Limpia el área de edición de código, en la cual el usuario puede editar sus sentencias. Si existe un archivo abierto, deberá preguntar si desea guardar los cambios antes de limpiar el editor. Esta opción debe preguntar el nombre del archivo y la ruta donde se guardará.
   
2. **Abrir:** Permite abrir un archivo ya creado previamente que contiene las sentencias que generan los comandos de MongoDB. Cuando se cargue el archivo, se podrá editar en el área de código.

3. **Guardar:** Permite guardar el código que se está escribiendo actualmente.

4. **Guardar Como:** Esta opción permite guardar el código de las sentencias que se está editando con otro nombre.

5. **Salir:** Con esta opción se cierra la aplicación.

![Menu Archivo](https://i.ibb.co/tJdKPgp/archivo-menu.png)

### Menú Análisis

Generar sentencias MongoDB: Esta opción analizará léxica y sintácticamente el contenido que este en el área de código, si existieran errores se mostraran TODOS los errores encontrados tanto léxicos como sintácticos que se encontraron, estos errores se mostrarán en el área de errores. De no existir errores se debe crear y mostrar las sentencias finales que estarán en sintaxis para MongoDB.

![Menu Analisis](https://i.ibb.co/Xk9yvKR/2.png)

### Menu Tokens

Mostrará una tabla en la cual estarán listados todos los tokens que se reconocieron en el archivo de entrada, con los siguientes campos:

1. **Número correlativo**
2. **Token**
3. **Número de Token**
4. **Lexema**

![Menu Tokens](https://i.ibb.co/MV4RncP/4.png)

### Área de Errores

El área de errores está conformada por una tabla en la que se cargarán tanto los errores léxicos como los errores sintácticos después de compilar algún archivo. Para los errores se deben mostrar las siguientes características:

1. **Tipo de error:** Puede ser léxico o sintáctico.
2. **Línea:** en la que ocurrió el error.
3. **Posición del error** Columna.
4. **Descripción:** Que token o componente lexico se espero.

![Area de Errores](https://i.ibb.co/tx3qRR9/5.png)

## Utilización del programa

Para la utilización de correcta del programa bastará con darle click a “Abrir” al presionar este botón se abrirá el explorador de archivos de sistema operativo, deberá seleccionar el archivo indicado con extensión. lfp, posteriormente se le mostrará el código cargado, una vez hecho esto dará click en “Analizar” y su traducción estará realizada.
