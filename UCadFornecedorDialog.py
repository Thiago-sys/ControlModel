from PyQt5.QtWidgets import QDialog
from Modelos.CadFornecedor import Ui_Dialog
from UDataBaseManager import DatabaseManager
from UCustomMessageBox import CustomMessageBox
from PyQt5 import QtWidgets


class CadFornecedorDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state=None, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.btnGravar.clicked.connect(self.gravar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.rdgCPF.clicked.connect(self.attMask)
        self.rdgCNPJ.clicked.connect(self.attMask)


    def gravar(self):
        try:
            if self.db.connection.in_transaction:
                self.db.connection.rollback()
            self.db.connection.start_transaction()

            nome = self.edtNome.text()
            if self.rdgCPF.isChecked():
                tipoIns = "PF"
            else:
                tipoIns = "PJ"
            inscricao = self.edtIns.text()
            telefone = self.edtTelefone.text()
            email = self.edtEmail.text()
            endereco = self.edtEnd.text()

            if self.state == "Insert":
                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente salvar esse fornecedor?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    insert_query = ("INSERT INTO TBLFOR (DSCFOR, TIPINS, INSFOR, TELFOR, EMAIL, ENDFOR) "
                                    "            VALUES (%s, %s, %s, %s, %s, %s")

                    values = (nome, tipoIns, inscricao, telefone, email, endereco)

                    # Executar a inserção
                    self.db.execute_query(insert_query, values)

                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Fornecedor gravado com sucesso.").information.exec_()
                    self.accept()
            else:
                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente salvar esse fornecedor?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    # Preparar a consulta SQL para inserção de um lançamento
                    update_query = "UPDATE TBLFOR SET DSCFOR = %s, TIPINS = %s, INSFOR = %s, TELFOR = %s,   " \
                                   "                  EMAIL = %s, ENDFOR = %s WHERE CODFOR = %s"

                    # Preparar os valores para a inserção na TBLLAN
                    values = (nome, tipoIns, inscricao, telefone, email, endereco, self.codigo)

                    # Executar a consulta SQL de inserção
                    self.db.execute_query(update_query, values)

                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Fornecedor gravado com sucesso.").information.exec_()
                    self.accept()
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            CustomMessageBox("Erro", f"Erro ao gravar o fornecedor: {str(e)}").error.exec_()
            self.reject()

    def cancelar(self):
        self.reject()

    def attMask(self):
        if self.rdgCPF.isChecked():
            self.edtIns.setInputMask('999.999.999-99')
        else:
            self.edtIns.setInputMask('99.999.999/9999-99')