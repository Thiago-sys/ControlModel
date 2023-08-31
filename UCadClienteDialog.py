from PyQt5.QtWidgets import QDialog
from Modelos.CadCliente import Ui_Dialog
from UDataBaseManager import DatabaseManager


class CadClienteDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state=None, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo
