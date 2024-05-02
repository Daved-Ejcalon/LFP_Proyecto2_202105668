from Error.Errores import Errores

class Funcion():
    def __init__(self):
        self.nombre = ''
        self.tipo = ''
        self.identificador = ''
        self.json = ''
    
    def __str__(self) -> str:
        return f'{self.tipo} {self.nombre} = {self.tipo} ( {self.identificador} , {self.json} )'
    
    def analizar(self):
        pass

    def recuperacionError(self, lista_lexemas):
        contador = 0
        for lex in lista_lexemas:
            if lex.lexema == ';':
                break
            contador += 1

        return contador


class CrearDB(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 6:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, 1
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        ptcoma = self.lista_lexemas[5].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        return self, 6

    def __str__(self):
        return f'use(‘{self.nombre}’);'

class EliminarBD(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 6:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        ptcoma = self.lista_lexemas[5].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        return self, 6

    def __str__(self):
        return f'{self.nombre}.dropDatabase();'

class CrearColeccion(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 7:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        ptcoma = self.lista_lexemas[6].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        return self, 7

    def __str__(self):
        return f'{self.nombre}.createCollection(‘{self.identificador}’);'

class EliminarColeccion(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 7:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        ptcoma = self.lista_lexemas[6].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)

        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        return self, 7

    def __str__(self):
        return f'{self.nombre}.{self.identificador}.drop();'

class InsertarUnico(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 8:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        archivojson = self.lista_lexemas[6].lexema
        ptcoma = self.lista_lexemas[7].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if archivojson == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el archivo JSON", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)

        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        self.json = archivojson
        return self, 8

    def __str__(self):
        return f'{self.nombre}.{self.nombre}.insertOne({self.json});'
    
class ActualizarUnico(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 8:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        archivojson = self.lista_lexemas[6].lexema
        ptcoma = self.lista_lexemas[7].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if archivojson == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el archivo JSON", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        self.json = archivojson
        return self, 8

    def __str__(self):
        return f'{self.nombre}.{self.identificador}.updateOne({self.json});'

class EliminarUnico(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 8:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        archivojson = self.lista_lexemas[6].lexema
        ptcoma = self.lista_lexemas[7].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if archivojson == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el archivo JSON", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        self.json = archivojson
        return self, 8

    def __str__(self):
        return f'{self.nombre}.{self.identificador}.deleteOne({self.json});'

class BuscarTodo(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 7:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema
        ptcoma = self.lista_lexemas[6].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if ptcoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        return self, 7

    def __str__(self):
        return f'{self.nombre}.{self.identificador}.find();'

class BuscarUnico(Funcion):
    def __init__(self, lista_lexemas, lista_errores):
        self.lista_lexemas = lista_lexemas
        self.lista_errores = lista_errores

        super().__init__()

    def analizar(self):

        funcion = self.lista_lexemas[0].lexema
        fila = self.lista_lexemas[0].getFila()
        columna = self.lista_lexemas[0].getColumna()

        if len(self.lista_lexemas) < 7:
            self.lista_errores.append(Errores(funcion,"Semántico", "Faltan parametros", fila, columna))
            return None, 1
        
        nombre = self.lista_lexemas[1].lexema
        igual = self.lista_lexemas[2].lexema
        nueva = self.lista_lexemas[3].lexema
        funcion2 = self.lista_lexemas[4].lexema
        identificador = self.lista_lexemas[5].lexema

        if nombre == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el nombre de la base de datos", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if igual != '=':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el signo igual", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if nueva not in ['nueva', 'new']:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta la palabra nueva", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas) 
        if funcion2 != funcion:
            self.lista_errores.append(Errores(funcion,"Semántico", f"Falta la palabra {funcion}", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        if identificador == None:
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el identificador", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        ptycoma = self.lista_lexemas[6].lexema
        if ptycoma != ';':
            self.lista_errores.append(Errores(funcion,"Semántico", "Falta el punto y coma", fila, columna))
            return None, self.recuperacionError(self.lista_lexemas)
        
        self.tipo = funcion
        self.nombre = nombre
        self.identificador = identificador
        return self, 7

    def __str__(self):
        return f'{self.nombre}.{self.identificador}.findOne();'