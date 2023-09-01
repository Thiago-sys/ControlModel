from PyQt5.QtWidgets import QDialog
from Modelos.CadCliente import Ui_Dialog
from UDataBaseManager import DatabaseManager
from UCustomMessageBox import CustomMessageBox
from PyQt5 import QtWidgets


class CadClienteDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state=None, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.btnGravar.clicked.connect(self.gravar)
        self.btnCancelar.clicked.connect(self.cancelar)

    def gravar(self):
        try:
            if self.db.connection.in_transaction:
                self.db.connection.rollback()
            self.db.connection.start_transaction()

            nome = self.edtNome.text()
            inscricao = self.edtCpf.text()
            telefone = self.edtTelefone.text()
            email = self.edtEmail.text()
            endereco = self.edtEnd.text()

            if self.state == "Insert":
                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente salvar esse cliente?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    insert_query = ("INSERT INTO TBLCLI (DSCCLI, INSCLI, TELCLI, EMAIL, ENDCLI) "
                                    "            VALUES (%s, %s, %s, %s, %s)")

                    values = (nome, inscricao, telefone, email, endereco)

                    # Executar a inserção
                    self.db.execute_query(insert_query, values)

                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Cliente salvo com sucesso.").information.exec_()
                    self.accept()
            else:
                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente salvar esse cliente?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    # Preparar a consulta SQL para inserção de um lançamento
                    update_query = ("UPDATE TBLCLI SET DSCCLI = %s, INSCLI = %s, TELCLI = %s, EMAIL = %s, ENDCLI = %s "
                                    "WHERE CODCLI = %s")

                    # Preparar os valores para a inserção na TBLLAN
                    values = (nome, inscricao, telefone, email, endereco, self.codigo)

                    # Executar a consulta SQL de inserção
                    self.db.execute_query(update_query, values)

                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Cliente salvo com sucesso.").information.exec_()
                    self.accept()
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            CustomMessageBox("Erro", f"Erro ao gravar o cliente: {str(e)}").error.exec_()
            self.reject()

    def cancelar(self):
        self.reject()
