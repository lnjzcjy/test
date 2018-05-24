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
         Ktp        = (273.15+temp)*101.3/pres/293.15                 # ok
         Kmkatt     = 0.972                                            # ok
         nxR        = 5.546
         Nx         = nxR *2.58e-4                                    # what is the unit? 2.58e-4C/(kg.nC) Nx in SI unit
         Nd         = Nx*33.97*Kmkatt                                  #ok 33.97 j/kg
         Swa        = 1.116                                            # ok                                                      
         Pu         = 1.0                                            #ok
         Pcel       = 1.0                                              #ok
         inpu_ktp   = inpu * Ktp
         dose       = inpu_ktp * Nd * Swa *Pu* Pcel*100.0
         dose_setup = 86.6
         error      = (dose / dose_setup)-1.0
         output ="Ktp is  "+str(Ktp)+"\nDose is "+ str(dose)+"cgy\n error is "+str(error)+"\n"+ "\n\nhere is the calculate processing: \n Dw(Peff)=M*ND*Sw,air*Pu*Pcel\n we also know that the Dw(Peff) mean setup is chanble under water 5cm (5.2cm) field is 10cm*10cm 6MV photons pdd=86.6% so 100mu means "+str(dose_setup)+"cgy\n\nDw("+str(dose)+")=(M_KTP"+str(inpu_ktp)+"=M("+str(inpu)+")*Ktp("+str(Ktp)+"))*ND("+str(Nd)+")*Sw,a("+str(Swa)+")*Pu("+str(Pu)+")*Pcel("+str(Pcel)+")\n #Nd("+str(Nd)+")=Nx("+str(Nx)+") * W/e(33.97J/C)* Katt * Km(Kmkatt = "+str(Kmkatt)+")"+"\n#Nx("+str(Nx)+")=nxR("+str(nxR)+")*2.58e-4(C/kg.nC)"
         self.text_outp.setText(output)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
