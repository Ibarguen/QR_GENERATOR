import sys
import qrcode
import time
from PIL import Image
from PyQt4 import QtCore, QtGui
from Example_progressbar import *

class Apk(QtGui.QWidget):


    def __init__(self, parent=None):
        self.name_image =''
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Charger.clicked.connect(self.generar_code)
        #self.ui.input.text.connect(self.imprimir)

    def generar_code(self):
        count = 0
        for count in range(0, 100):
            count += 1
            time.sleep(0.01)
            self.ui.progressBar.setValue(count)

            continue

        self.ui.label.text()
        imagen = qrcode.make(self.ui.label)

        self.name_image=('qrcode')+'.png'
        self.archivo_imagen = open(self.name_image, 'wb')
        imagen.save(self.archivo_imagen)
        self.archivo_imagen.close()

        ruta_imagen = './' + self.name_image
        Image.open(ruta_imagen).show()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    mi_app = Apk()
    mi_app.show()
    sys.exit(app.exec_())