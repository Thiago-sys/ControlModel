from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Modelos.CadGrupos import Ui_Dialog
from UCustomMessageBox import CustomMessageBox
from UDataBaseManager import DatabaseManager


class CadGruposDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state=None, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.btnGravar.clicked.connect(self.gravar)
        self.btnCancelar.clicked.connect(self.cancelar)


    def gravar(self):
        if self.edtDescricao.text().strip() == "":
            CustomMessageBox("Erro", f"Os seguintes campos são obrigatórios: \nDescrição").error.exec_()
            self.edtDescricao.setFocus()
            return

        try:
            if self.state == 'Insert':
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar inserção",
                                          "Deseja realmente inserir este grupo?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    descricao = self.edtDescricao.text()

                    insert_query = "INSERT INTO TBLGRP (DSCGRP) VALUES (%s)"

                    values = [descricao]

                    self.db.execute_query(insert_query, values)
                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Grupo inserido com sucesso.").information.exec_()
                    self.accept()
            else:
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar edição",
                                          "Deseja realmente editar este grupo?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    descricao = self.edtDescricao.text()

                    update_query = "UPDATE TBLGRP SET DSCGRP = %s WHERE CODGRP = %s"

                    values = (descricao, self.codigo)

                    self.db.execute_query(update_query, values)
                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Grupo editado com sucesso.").information.exec_()
                    self.accept()

        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            CustomMessageBox("Erro", f"Erro ao inserir grupo: {str(e)}").error.exec_()
            self.reject()

    def cancelar(self):
        self.reject()