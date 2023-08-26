from PyQt5.QtWidgets import QDialog
from Modelos.MovEstoque import Ui_Dialog


class MovEstoque(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)