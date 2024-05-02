from Instrucciones.Funcion import *
from Error.Errores import Errores

class Resultado():
    def __init__(self, lexemas, errores):
        self.lexemas = lexemas
        self.errores = errores

    def getLexemas(self):
        return self.lexemas
    

    def getResultado(self):
        funcion = self.lexemas[0].lexema
        fila = self.lexemas[0].getFila()
        columna = self.lexemas[0].getColumna()

        if funcion in ['CrearDB', 'CrearBD']:
            func = CrearDB(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion in ['EliminarBD', 'EliminarDB']:
            func = EliminarBD(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'CrearColeccion':
            func = CrearColeccion(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'EliminarColeccion':
            func = EliminarColeccion(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'InsertarUnico':
            func = InsertarUnico(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'ActualizarUnico':
            func = ActualizarUnico(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'EliminarUnico':
            func = EliminarUnico(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'BuscarTodo':
            func = BuscarTodo(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        elif funcion == 'BuscarUnico':
            func = BuscarUnico(self.lexemas, self.errores)
            res, lexemas_usados = func.analizar()
            return res, lexemas_usados
        
        # Si no se encontró la función
        self.errores.append(Errores(funcion,"Semántico", "No se encontró la función", fila, columna))
        return None, 1

        # match funcion:
        #     case 'CrearDB':
        #         func = CrearDB(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'EliminarBD':
        #         func = EliminarBD(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'CrearColeccion':
        #         func = CrearColeccion(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'EliminarColeccion':
        #         func = EliminarColeccion(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'InsertarUnico':
        #         func = InsertarUnico(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'ActualizarUnico':
        #         func = ActualizarUnico(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'EliminarUnico':
        #         func = EliminarUnico(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'BuscarTodo':
        #         func = BuscarTodo(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados
        #     case 'BuscarUnico':
        #         func = BuscarUnico(self.lexemas, self.errores)
        #         res, lexemas_usados = func.analizar()
        #         return res, lexemas_usados