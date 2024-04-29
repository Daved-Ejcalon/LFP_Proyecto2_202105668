from Abstract.Abstract import Expression

class Errores(Expression):
    def __init__(self, lexema, tipo, mensaje, fila, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.mensaje = mensaje
        super().__init__(fila, columna)

    def operar(self, no=None):
        lex = f"Error {self.tipo} en ({self.lexema}): {self.mensaje} en la fila {self.fila} y columna {self.columna}"
        return lex

    def getColumna(self):
        return super().getColumna()

    def getFila(self):
        return super().getFila()
    
    def getTipo(self):
        return self.tipo
    
    def getMensaje(self):
        return self.mensaje
    
    def getLexema(self):
        return self.lexema