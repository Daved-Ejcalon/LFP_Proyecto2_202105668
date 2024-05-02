from Abstract.Abstract import Expression

class Lexema(Expression):

    def __init__(self, lexema, tipo, fila, columna):
        self.lexema = lexema
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol=None):   #! Retorna mi Lexema
        return self.lexema

    def getFila(self):              #! Retorna la fila
        return super().getFila()

    def getColumna(self):           #! Retorna la columna
        return super().getColumna()

    def getTipo(self):              #! Retorna el tipo
        return self.tipo
    
    def __str__(self) -> str:
        return f'{self.lexema}'