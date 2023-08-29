from PyQt5.QtWidgets import QDialog
from Modelos.CadItens import Ui_Dialog


class CadItensDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__(self)
        self.setupUi(self)


