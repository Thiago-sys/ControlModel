from PyQt6.QtWidgets import QDialog
from Modelos.MesAno import Ui_Dialog


class MesAnoDialog(QDialog, Ui_Dialog):
    def __init__(self, MesAno):
        super().__init__()
        self.setupUi(self)

        self.MesAno = MesAno

        self.btnJan.clicked.connect(lambda: self.selectMesAno(self.btnJan))
        self.btnFev.clicked.connect(lambda: self.selectMesAno(self.btnFev))
        self.btnMar.clicked.connect(lambda: self.selectMesAno(self.btnMar))
        self.btnAbr.clicked.connect(lambda: self.selectMesAno(self.btnAbr))
        self.btnMai.clicked.connect(lambda: self.selectMesAno(self.btnMai))
        self.btnJun.clicked.connect(lambda: self.selectMesAno(self.btnJun))
        self.btnJul.clicked.connect(lambda: self.selectMesAno(self.btnJul))
        self.btnAgo.clicked.connect(lambda: self.selectMesAno(self.btnAgo))
        self.btnSet.clicked.connect(lambda: self.selectMesAno(self.btnSet))
        self.btnOut.clicked.connect(lambda: self.selectMesAno(self.btnOut))
        self.btnNov.clicked.connect(lambda: self.selectMesAno(self.btnNov))
        self.btnDez.clicked.connect(lambda: self.selectMesAno(self.btnDez))

        self.btnNext.clicked.connect(self.proximo)
        self.btnBack.clicked.connect(self.anterior)

    def selectMesAno(self, sender):
        self.accept()
        mes = int(sender.property("ret"))
        ano = int(self.lblAno.text())
        self.MesAno.set_mes_ano(mes, ano)

    def proximo(self):
        ano = int(self.lblAno.text())
        ano += 1

        self.lblAno.setText(str(ano))

    def anterior(self):
        ano = int(self.lblAno.text())
        ano -= 1

        self.lblAno.setText(str(ano))