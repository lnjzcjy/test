import sys
from PyQt5 import QtCore, QtWidgets, uic

qtCreatorFile = "main.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)                                             # this must be call for setup ui 
        self.button_comp.clicked.connect(self.calculate)
    def calculate(self):                                               # (self) 
         temp = self.spin_temp.value()
         pres = self.spin_pres.value()
         inpu = self.spin_inpu.value()
         rightvalue = 0.0
         error      = 0.0
         output ="the right value is  "+ str(temp+pres+inpu)+"  and there is some error that is abuot  "+str(error)+" !"
         self.text_outp.setText(output)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
