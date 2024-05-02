from Instrucciones.Resultado import *
from Error.Errores import *
from Abstract.Lexema import *
import json

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores
global estado_actual

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []
estado_actual = 0

def intruccion(cadena): 
    global n_linea
    global n_columna
    global lista_lexemas
    global estado_actual
    lexema = ''

    while cadena:
        char = cadena[0]
        charComentario = cadena[:2]


        # Comentarios   
        if charComentario == '--': # Comentario unilinea
            charComentario = ''

            while len(cadena) and char != '\n':
                n_linea += 1

                cadena = cadena[1:]
                char = cadena[0]
            
                if len(cadena) == 1:
                    cadena = ''
                    break

            n_columna = 1
            cadena = cadena[2:]
            continue

        elif charComentario == '/*': # Comentario unilinea

            while len(cadena) and  charComentario != '*/':
                n_linea += 1


                cadena = cadena[1:]
                charComentario = cadena[:2]
            
                if len(cadena) == 2:
                    cadena = ''
                    break

            n_columna = 1
            cadena = cadena[2:]
            continue
        
        # Ignorar
        if char =="\t": # Si el caracter es un tabulador
            n_columna += 4
            cadena = cadena[4:]
            continue
        elif char == "\n": # Si el caracter es un salto de linea
            #cadena = cadena[1:]
            n_linea += 1
            n_columna = 1
            cadena = cadena[1:]
            continue
        elif char == ' ' or char == '\r': # Si el caracter es un espacio o un salto de carro
            n_columna += 1
            cadena = cadena[1:]
            continue
        
        # Reconocer lexemas

        if estado_actual == 0: # Estado FUNCION

            if char.isalpha(): # Inicio de texto
                lexema, cadena = armar_lexema(cadena)
                if lexema and cadena: # Si lexema y cadena no son nulos
                    n_columna += 1
                    
                    l = Lexema(lexema, "FUNCION", n_linea, n_columna) #Armar lexema
                    lista_lexemas.append(l)  # Agregamos lexemas a la lista_lexema
                    n_columna += len(lexema) + 1

                    if cadena[0] == ' ':
                        n_columna += 1
                        estado_actual = 1
                    else:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba espacio", n_linea, n_columna))
                        n_columna += 1
                else:
                    lista_errores.append(Errores(char,"Lexico","Formato de string inválido", n_linea, n_columna))
                    n_columna += 1
            elif char == ' ':
                n_columna += 1
                estado_actual = 1
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1

        elif estado_actual == 1: # Estado NOMBRE
            if char.isalpha(): # Inicio de texto
                lexema, cadena = armar_lexema(cadena)
                if lexema and cadena: # Si lexema y cadena no son nulos
                    n_columna += 1
                    
                    l = Lexema(lexema, "NOMBRE", n_linea, n_columna) #Armar lexema
                    lista_lexemas.append(l)  # Agregamos lexemas a la lista_lexema
                    n_columna += len(lexema) + 1

                    if cadena[0] == ' ':
                        n_columna += 1
                        estado_actual = 2
                    else:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba espacio", n_linea, n_columna))
                        n_columna += 1
                else:
                    lista_errores.append(Errores(char,"Lexico","Formato de string inválido", n_linea, n_columna))
                    n_columna += 1
            elif char == ' ':
                n_columna += 1
                estado_actual = 2
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1
        
        elif estado_actual == 2: # Estado ASIGNACION
            if char == '=':
                c = Lexema(char, "ASIGNACION", n_linea, n_columna)
                lista_lexemas.append(c)
                cadena = cadena[1:]
                n_columna += 1
                estado_actual = 3
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba asignacion (=)", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 3: # Estado NUEVA
            if char.isalpha(): # Inicio de texto
                lexema, cadena = armar_lexema(cadena)
                if lexema and cadena: # Si lexema y cadena no son nulos
                    
                    if lexema.lower() not in ['nueva', 'new']:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba la palabra \"nueva\"", n_linea, n_columna))
                        n_columna += 1
                    else:
                        n_columna += 1
                        l = Lexema(lexema, "NUEVA", n_linea, n_columna) #Armar lexema
                        lista_lexemas.append(l)  # Agregamos lexemas a la lista_lexema
                        n_columna += len(lexema) + 1

                        if cadena[0] == ' ':
                            n_columna += 1
                            estado_actual = 4
                else:
                    lista_errores.append(Errores(char,"Lexico","Formato de string inválido", n_linea, n_columna))
                    n_columna += 1
            elif char == ' ':
                n_columna += 1
                estado_actual = 4
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 4: # Estado FUNCION
            if char == '(':
                n_columna += 1
                estado_actual = 5
            elif char.isalpha(): # Inicio de texto
                lexema, cadena = armar_lexema(cadena)
                if lexema and cadena: # Si lexema y cadena no son nulos
                    n_columna += 1
                    
                    l = Lexema(lexema, "FUNCION", n_linea, n_columna) #Armar lexema
                    lista_lexemas.append(l)  # Agregamos lexemas a la lista_lexema
                    n_columna += len(lexema) + 1

                    # Eliminar espacios
                    while cadena[0] == ' ':
                        n_columna += 1
                        cadena = cadena[1:]

                    if cadena[0] == '(':
                        n_columna += 1
                        estado_actual = 5
                    else:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba parentesis", n_linea, n_columna))

                        n_columna += 1
            
                else:
                    lista_errores.append(Errores(char,"Lexico","Formato de string inválido", n_linea, n_columna))
                    n_columna += 1
            elif char == '(':
                n_columna += 1
                estado_actual = 5
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 5: # Estado comillas

            if char == '\"' or char == "“": # Inicio de string
                estado_actual = 6
                n_columna += 1
            elif char == ')':
                estado_actual = 11
                n_columna += 1
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba comillas", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 6: # Estado TEXTO

            if char.isalpha(): # Inicio de texto
                lexema, cadena = armar_lexema_string(cadena)
                if lexema and cadena: # Si lexema y cadena no son nulos
                    n_columna += 1
                    l = Lexema(lexema, "IDENTIFICADOR", n_linea, n_columna) #Armar lexema
                    lista_lexemas.append(l)  # Agregamos lexemas a la lista_lexema
                    n_columna += len(lexema) + 1

                    if cadena[0] in ['\"', "”"]:
                        n_columna += 1
                        estado_actual = 7
                    else:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba comillas", n_linea, n_columna))
                        n_columna += 1
                else:
                    lista_errores.append(Errores(char,"Lexico","Formato de string inválido", n_linea, n_columna))
                    n_columna += 1
            elif char in ['\"', "”"]:
                n_columna += 1
                estado_actual = 7
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 7: # Estado COMA o PARENTESIS

            if char == ',':
                #c = Lexema(char, n_linea, n_columna)
                #lista_lexemas.append(c)
                n_columna += 1
                estado_actual = 8
            elif char == ')':
                #c = Lexema(char, n_linea, n_columna)
                #lista_lexemas.append(c)
                n_columna += 1
                estado_actual = 11
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba coma o parentesis", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 8: # Estado comillas
                
            if char == '\"' or char == "“":
                estado_actual = 9
                n_columna += 1
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba comillas", n_linea, n_columna))
                n_columna += 1  
        elif estado_actual == 9: # Estado JSON
                
            if char == '{':
                lexema, cadena = armar_lexema_json(cadena)
                if lexema and cadena:
                    n_columna += 1
                    l = Lexema(lexema, "JSON", n_linea, n_columna)
                    lista_lexemas.append(l)
                    n_columna += len(lexema) + 1

                    # Eliminar espacios
                    while cadena[0] == ' ':
                        n_columna += 1
                        cadena = cadena[1:]

                    #Eliminar salto de linea
                    while cadena[0] == '\n':
                        n_linea += 1
                        n_columna = 1
                        cadena = cadena[1:]

                    if cadena[0] in ['\"', "”"]:
                        n_columna += 1
                        estado_actual = 10
                    else:
                        lista_errores.append(Errores(char,"Lexico","Se esperaba comillas", n_linea, n_columna))
                        n_columna += 1
                else:
                    lista_errores.append(Errores(char,"Lexico","Json con formato inválido", n_linea, n_columna))
                    n_columna += 1
            elif char in ['\"', "”"]:
                n_columna += 1
                estado_actual = 10
            else:
                lista_errores.append(Errores(char,"Lexico", "No se reconoció el caracter", n_linea, n_columna))
                n_columna += 1       
        elif estado_actual == 10: # Estado PARENTESIS CIERRE
            if char == ')':
                n_columna += 1
                estado_actual = 11
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba parentesis", n_linea, n_columna))
                n_columna += 1
        elif estado_actual == 11: # Estado PUNTO Y COMA
            if char == ';':
                n_columna += 1
                estado_actual = 0 # Reiniciar estados
                c = Lexema(char, "PUNTOYCOMA", n_linea, n_columna)
                lista_lexemas.append(c)
            else:
                lista_errores.append(Errores(char,"Lexico", "Se esperaba punto y coma", n_linea, n_columna))
                n_columna += 1
        # Actualizar cadena
        cadena = cadena[1:]

    return lista_lexemas

def armar_lexema(cadena): # Crea lexema y retorna cadena restante
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    cadena_aux = ''

    for char in cadena:
        
        if char in [' ', '\n', '\t', '(', ';', ',']: # Delimitadores
            return lexema, cadena[len(cadena_aux):]
        else:
            lexema += char   #! creamos nuestros Token

        cadena_aux += char

    return None, None

def armar_lexema_string(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    cadena_aux = ''

    for char in cadena:
        
        if char in ['\"', "”"]: # Delimitadores
            return lexema, cadena[len(cadena_aux):]
        else:
            lexema += char   #! creamos nuestros Token

        cadena_aux += char

    return None, None

def armar_lexema_json(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    char = cadena[0]
    

    while char != '}':
        
        lexema += char
        cadena = cadena[1:]
        char = cadena[0]

        if char == '{':
            lex, cadena = armar_lexema_json(cadena)
            lexema += lex

            if not lexema:
                return None, None
            
            cadena = cadena[1:]
            char = cadena[0]

    lexema += char
    # Verificar si el lexema tiene el formato adecuado de JSON
    try:
        json.loads(lexema)
        resultado = lexema.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        return resultado, cadena[1:]  # JSON válido, retornar lexema y el resto de la cadena
    except json.JSONDecodeError:
        return None, cadena

def analizar():
    global lista_lexemas
    global instrucciones
    global lista_errores
    temp_instrucciones = []

    while lista_lexemas:
        func =  Resultado(lista_lexemas, lista_errores)

        if func == None:
            num_borrar = recuperacionError(lista_lexemas)
            lista_lexemas = lista_lexemas[num_borrar:]
            continue

        res, numlex = func.getResultado()

        print(f"Se quitara {numlex} lexemas de la lista ")
        
        lista_lexemas = lista_lexemas[numlex:]

        temp_instrucciones.append(res)
        
    return temp_instrucciones

def analizar_():
    global instrucciones
    temp_instrucciones = []

    operacion = analizar() # Operar la funcion

    while operacion:
        temp_instrucciones.append(operacion) # Agregar la operacion a la lista de instrucciones
        operacion = analizar() # Operar la funcion

    return temp_instrucciones

def getErrores():
    global lista_errores
    return lista_errores

def recuperacion(cadena):
    global n_linea
    global n_columna
    global lista_errores

    # se recupera del error, desechando caracteres hasta encontrar
    # un delimitador, en este caso un salto de linea
    caracter = cadena[0]
    
    while caracter != ';': # Delimitador
        cadena = cadena[1:]
        caracter = cadena[0]
        n_columna += 1

    n_linea += 1
    cadena = cadena[1:]

    return cadena


def recuperacionError(lista_lexemas):
    contador = 0
    for lex in lista_lexemas:
        if lex.lexema == ';':
            break
        contador += 1

    return contador

def resetAnalizador():
    global n_linea
    global n_columna
    global instrucciones
    global lista_lexemas
    global lista_errores
    global estado_actual

    n_linea = 1
    n_columna = 1
    instrucciones = []
    lista_lexemas = []
    lista_errores = []
    estado_actual = 0
