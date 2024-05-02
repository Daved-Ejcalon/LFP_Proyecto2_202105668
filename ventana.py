from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout,  QFileDialog, QMessageBox, QTextEdit
from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction, QTextOption
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import  QTableWidget, QTableWidgetItem
import sys
import os
import copy
from Analizador import *

global archivo_abierto
archivo_abierto = ''

class Window(QMainWindow):
    def __init__(self, ):
        super().__init__()

        # ** Configuraciones de la ventana
        self.setWindowTitle('Proyecto #2 LFP')
        self.setFixedSize(575, 500) # ancho, alto
        #self.setWindowIcon(QIcon("logo.ico"))

        # Crear la interfaz
        self.createUI()
    
    # Funciones interfaz
    def createUI(self):

        # Establecer el fondo de color
        self.setStyleSheet(f"background-color: #4793AF;")

        # Label para el título
        self.label_titulo = QLabel("...", self)                                         
        self.label_titulo.setStyleSheet(f"color: black; font-size: 15px; font-weight: bold;")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Barra
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        # Estilo de la barra
        menuBar.setStyleSheet("background-color: #1679AB; color: white; font-size: 12px;")

        # Creating menus using a QMenu object
        fileMenu = QMenu("&Archivo", self)
        menuBar.addMenu(fileMenu)

        nuevoAction = QAction("&Nuevo", self)
        nuevoAction.triggered.connect(self.nuevo_archivo)
        fileMenu.addAction(nuevoAction)
        
        abrirAction = QAction("&Abrir", self)
        abrirAction.triggered.connect(self.abrir_archivo)
        fileMenu.addAction(abrirAction)

        guardarAction = QAction("&Guardar", self)
        guardarAction.triggered.connect(self.guardar_archivo)
        fileMenu.addAction(guardarAction)

        guardarComoAction = QAction("Guardar &como", self)
        guardarComoAction.triggered.connect(self.guardar_como)
        fileMenu.addAction(guardarComoAction)

        # Creating menus using a title

        analizarAction = QAction("Anali&zar", self)
        analizarAction.triggered.connect(self.analizar)
        menuBar.addAction(analizarAction)

        tokensAction = QAction("&Tokens", self)
        tokensAction.triggered.connect(self.tokens)
        menuBar.addAction(tokensAction)

        erroresAction = QAction("&Errores", self)
        erroresAction.triggered.connect(self.errores)
        menuBar.addAction(erroresAction)

        # Text area
        self.text_area = QTextEdit(self)
        self.text_area.setFixedSize(525, 275)
        self.text_area.setStyleSheet("background-color: white; color: black; font-size: 12px; border-radius: 5px;")
        self.text_area.setPlaceholderText("Ingrese el texto a analizar")
        self.text_area.setAcceptRichText(False)
        self.text_area.setTabChangesFocus(True)
        self.text_area.setAcceptRichText(False)
        self.text_area.setAcceptDrops(True)
        self.text_area.setUndoRedoEnabled(True)
        self.text_area.setWordWrapMode(QTextOption.WrapMode.NoWrap)

        # Text area
        self.text_consola = QTextEdit(self)
        self.text_consola.setFixedSize(525, 150)
        self.text_consola.setStyleSheet("background-color: #F6F5F2; color: black; font-size: 12px; border-radius: 5px;")
        self.text_consola.setPlaceholderText("Resultado mongoDB")
        self.text_consola.setAcceptRichText(False)
        self.text_consola.setTabChangesFocus(False)
        self.text_consola.setAcceptRichText(False)
        self.text_consola.setAcceptDrops(True)
        self.text_consola.setUndoRedoEnabled(True)
        self.text_consola.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.text_consola.setReadOnly(True)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label_titulo)
        main_layout.addWidget(self.text_area)
        main_layout.addWidget(self.text_consola)
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Widget principal
        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
    
    # Funciones de eventos
    def actualizar_titulo(self):

        global archivo_abierto
        # Obtener nombre archivo de la ruta

        if archivo_abierto != '':
            nombre_archivo = archivo_abierto.split('/')[-1]
            self.label_titulo.setText(nombre_archivo)
        else:
            self.label_titulo.setText("...")

    # Funciones barra menu
    def nuevo_archivo(self):
        global archivo_abierto
        if archivo_abierto != '':
            
            # Preguntar si desea guardar los cambios
            respuesta = QMessageBox.question(self, 'Guardar cambios', '¿Desea guardar los cambios en el archivo actual?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if respuesta == QMessageBox.StandardButton.Yes:
                self.guardar_archivo()
                self.text_area.clear()
                archivo_abierto = ''
                self.actualizar_titulo()
            elif respuesta == QMessageBox.StandardButton.No:
                self.text_area.clear()
                archivo_abierto = ''
                self.actualizar_titulo()
            else:
                return 
        
        else:
            self.text_area.clear()
            archivo_abierto = ''
            self.actualizar_titulo()

    def abrir_archivo(self):
        global archivo_abierto
        archivo_abierto = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos LFP (*.lfp);;Archivos de texto (*.txt)')[0]

        if archivo_abierto != '':
            
            # Verificar si el archivo existe
            if not os.path.exists(archivo_abierto):
                QMessageBox.warning(self, 'Error', 'El archivo no existe')
                return

            # Limpiar el text area
            self.text_area.clear()

            # Leer el archivo
            with open(archivo_abierto, 'r', encoding='utf-8') as file:
                texto = file.read()
                self.text_area.setPlainText(texto)
                file.close()
            
            # Actualizar el título
            self.actualizar_titulo()

    def guardar_archivo(self):
        global archivo_abierto
        if archivo_abierto == '':
            QMessageBox.warning(self, 'Error', 'No se ha seleccionado un archivo para guardar')
            return
        
        # Obtener el texto del text area
        texto = self.text_area.toPlainText()

        # Guardar el archivo
        with open(archivo_abierto, 'w', encoding='utf-8') as file:
            file.write(texto)
            file.close()
        
        # Actualizar el título
        self.actualizar_titulo()

        # Mostrar mensaje de éxito
        QMessageBox.information(self, 'Guardado', 'El archivo se ha guardado correctamente')

    def guardar_como(self):

        # Verificar si el texto está vacío
        texto = self.text_area.toPlainText()
        if texto == '':
            QMessageBox.warning(self, 'Error', 'No hay texto para guardar')
            return

        global archivo_abierto
        archivo_abierto = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Archivos LFP (*.lfp);;Archivos de texto (*.txt)')[0]

        if archivo_abierto != '':
            # Guardar el archivo
            with open(archivo_abierto, 'w', encoding='utf-8') as file:
                file.write(texto)
                file.close()
            
            # Actualizar el título
            self.actualizar_titulo()

            # Mostrar mensaje de éxito
            QMessageBox.information(self, 'Guardado', 'El archivo se ha guardado correctamente')

    def analizar(self):

        # Obtener el texto del text area
        data = self.text_area.toPlainText()

        if data == '':
            QMessageBox.warning(self, 'Error', 'No hay texto para analizar')
            return

        # Remplazar caracteres de texto, saltos de linea y espacios
        data = data.replace("\\\"", "\"")
        data = data.replace("\\n", "\n")
        data = data.replace("\\r", "\r")
        data = data.replace("\\t", "\t")

        try:
            resetAnalizador()
            #lista_lexs = []

            # analizar archivo
            instrucciones = intruccion(data) # Asigna instrucciones con la lista de lexemas
            #lista_lexs = copy.deepcopy(instrucciones)

            resultado_instrucciones = analizar()

            print("Resultado del análisis: ")
            print("*"*50)
            str_res = ''
            for respuesta in resultado_instrucciones:
                str_res += str(respuesta) + '\n'
            
            print(str_res)
            self.text_consola.setPlainText(str_res)
            print("*"*50)
            
            print("\n")
            
            print("*"*50)
            print("Errores: ")
            for error in getErrores():
                print(error.operar())
            print("*"*50)

            # Mostrar mensaje de éxito
            QMessageBox.information(self, 'Análisis', 'El texto se ha analizado correctamente')

        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error', 'Ha ocurrido un error al analizar el texto')

    def tokens(self):
        print("Mostrar tokens")
        # Verificar si hay texto
        data = self.text_area.toPlainText()
        if data == '':
            QMessageBox.warning(self, 'Error', 'No hay texto para analizar tokens')
            return

        # Remplazar caracteres de texto, saltos de linea y espacios
        data = data.replace("\\\"", "\"")
        data = data.replace("\\n", "\n")
        data = data.replace("\\r", "\r")
        data = data.replace("\\t", "\t")

        try:
            resetAnalizador()
            lista_lexs = []

            # analizar archivo
            instrucciones = intruccion(data) # Asigna instrucciones con la lista de lexemas
            lista_lexs = copy.deepcopy(instrucciones)
            
            # Verificar si hay tokens
            if len(lista_lexs) == 0:
                QMessageBox.information(self, 'Tokens', 'No se han encontrado tokens')
                return

            ventana = VentanaTokens(self)
            ventana.llenar_tabla(lista_lexs)
            ventana.show()

        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error', 'Ha ocurrido un error al analizar el texto')

    def errores(self):
        
        # Verificar si hay texto
        data = self.text_area.toPlainText()
        if data == '':
            QMessageBox.warning(self, 'Error', 'No hay texto para analizar errores')
            return

        # Remplazar caracteres de texto, saltos de linea y espacios
        data = data.replace("\\\"", "\"")
        data = data.replace("\\n", "\n")
        data = data.replace("\\r", "\r")
        data = data.replace("\\t", "\t")

        try:
            resetAnalizador()

            # analizar archivo
            instrucciones = intruccion(data) # Asigna instrucciones con la lista de lexemas
            l_errores = getErrores()

            # Verificar si hay errores
            if len(l_errores) == 0:
                QMessageBox.information(self, 'Errores', 'No se han encontrado errores')
                return

            ventana = VentanaErrores(self)
            ventana.llenar_tabla(l_errores)
            ventana.show()


        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error', 'Ha ocurrido un error al analizar el texto')

    def darken_hex(self, hex_color, factor=0.7):
        """
        Genera un color ligeramente más oscuro a partir de un código de color hexadecimal.

        :param hex_color: Cadena que representa el código de color hexadecimal.
        :param factor: Factor de oscurecimiento, un valor entre 0 y 1.
        """
        # Asegúrate de que la cadena comience con '#'
        if not hex_color.startswith('#'):
            return hex_color

        # Convierte el código hexadecimal a valores RGB
        rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        
        # Aplica el factor de oscurecimiento
        r, g, b = rgb_color
        r_nuevo = max(0, int(r * factor))
        g_nuevo = max(0, int(g * factor))
        b_nuevo = max(0, int(b * factor))

        # Convierte los valores RGB de vuelta a formato hexadecimal
        nuevo_hex_color = "#{:02X}{:02X}{:02X}".format(r_nuevo, g_nuevo, b_nuevo)

        return nuevo_hex_color


class VentanaTokens(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tabla de Tokens")
        self.setGeometry(100, 100, 475, 350)

        self.table_widget = QTableWidget(self)

        # Estilo de la tabla
        self.table_widget.setStyleSheet("background-color: white; color: black; font-size: 12px; border-radius: 5px;")
        # Establecer el tamaño de la tabla
        self.table_widget.setFixedSize(450, 325)    


        # Establecer el número de filas y columnas
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)

        headers = ["Token", "Lexema", "Fila", "Columna"]
        self.table_widget.setHorizontalHeaderLabels(headers)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def llenar_tabla(self, lista_lex):

        for token in lista_lex:  # Datos de ejemplo
            row = self.table_widget.rowCount()

            # Añadir una fila
            self.table_widget.setRowCount(row + 1)

            item = QTableWidgetItem(token.getTipo())
            self.table_widget.setItem(row, 0, item)

            item = QTableWidgetItem(token.operar())
            self.table_widget.setItem(row, 1, item)

            item = QTableWidgetItem(str(token.getFila()))
            self.table_widget.setItem(row, 2, item)

            item = QTableWidgetItem(str(token.getColumna()))
            self.table_widget.setItem(row, 3, item)

            # Agregar tooltip con el lexema
            self.table_widget.item(row, 1).setToolTip(token.operar())

class VentanaErrores(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tabla de Errores")
        self.setGeometry(100, 100, 575, 350)

        self.table_widget = QTableWidget(self)

        # Estilo de la tabla
        self.table_widget.setStyleSheet("background-color: white; color: black; font-size: 12px; border-radius: 5px;")
        # Establecer el tamaño de la tabla
        self.table_widget.setFixedSize(550, 325)    


        # Establecer el número de filas y columnas
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(5)

        headers = ["Tipo", "Linea", "Columna", "Token", "Descripcion"]
        self.table_widget.setHorizontalHeaderLabels(headers)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def llenar_tabla(self, lista_errores):
        
        for error in lista_errores:  # Datos de ejemplo
            row = self.table_widget.rowCount()

            # Añadir una fila
            self.table_widget.setRowCount(row + 1)

            item = QTableWidgetItem(error.getTipo())
            self.table_widget.setItem(row, 0, item)

            item = QTableWidgetItem(str(error.getFila()))
            self.table_widget.setItem(row, 1, item)

            item = QTableWidgetItem(str(error.getColumna()))
            self.table_widget.setItem(row, 2, item)

            item = QTableWidgetItem(error.getLexema())
            self.table_widget.setItem(row, 3, item)

            item = QTableWidgetItem(error.getMensaje())
            self.table_widget.setItem(row, 4, item)

            # Agregar tooltip con el lexema y mensaje
            self.table_widget.item(row, 3).setToolTip(error.getLexema())
            self.table_widget.item(row, 4).setToolTip(error.getMensaje())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Window()
    ventana.show()
    sys.exit(app.exec())