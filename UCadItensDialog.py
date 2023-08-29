from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Modelos.CadItens import Ui_Dialog
from UCustomMessageBox import CustomMessageBox
from UDataBaseManager import DatabaseManager
from datetime import date


class CadItensDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state=None, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.btnGravar.clicked.connect(self.gravar)
        self.btnCancelar.clicked.connect(self.cancelar)

        self.dteData.setDate(date.today())

        self.FornecedorIndexMap = {}
        self.GrupoIndexMap = {}

        self.buscarGrupos()
        self.buscarFornecedores()


    def gravar(self):
        try:
            if self.state == 'Insert':
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar inserção",
                                          "Deseja realmente inserir este item?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    descricao = self.edtDescricao.text()
                    data = self.dteData.date().toPyDate()
                    valor = self.dblValor.value()
                    codFornecedor = int(self.obterCodFornecedorSelecionado())
                    codGrupo = int(self.obterCodGrupoSelecionado())

                    insert_query = "INSERT INTO TBLITE (DSCITE, VLRITE, DTAAQU, CODFOR, CODGRP) " \
                                   "            VALUES (%s, %s, %s, %s, %s)"

                    values = (descricao, valor, data, codFornecedor, codGrupo)

                    self.db.execute_query(insert_query, values)
                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Item inserido com sucesso.").information.exec_()
                    self.accept()
            else:
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar edição",
                                          "Deseja realmente editar este item?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    descricao = self.edtDescricao.text()
                    data = self.dteData.date().toPyDate()
                    valor = self.dblValor.value()
                    codFornecedor = int(self.obterCodFornecedorSelecionado())
                    codGrupo = int(self.obterCodGrupoSelecionado())

                    update_query = "UPDATE TBLITE SET DSCITE = %s, VLRITE = %s, DTAAQU = %s, CODFOR = %s, CODGRP = %s "\
                                   "WHERE CODITE = %s"

                    values = (descricao, valor, data, codFornecedor, codGrupo, self.codigo)

                    self.db.execute_query(update_query, values)
                    self.db.connection.commit()
                    # Exibir mensagem de sucesso
                    CustomMessageBox("Sucesso", "Item editado com sucesso.").information.exec_()
                    self.accept()

        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            CustomMessageBox("Erro", f"Erro ao inserir item: {str(e)}").error.exec_()
            self.reject()

    def cancelar(self):
        self.reject()

    def buscarGrupos(self):
        query = "SELECT G.CODGRP, G.DSCGRP FROM TBLGRP G"
        data = self.db.fetch_data(query)

        for index, row in enumerate(data):
            grupo = str(row[1])
            self.cbxGrupo.addItem(grupo)
            self.GrupoIndexMap[grupo] = int(row[0])

    def obterCodGrupoSelecionado(self):
        grupo_selecionado = self.cbxGrupo.currentText()
        if grupo_selecionado in self.GrupoIndexMap:
            return self.GrupoIndexMap[grupo_selecionado]
        return None

    def selecionarGrupoPorCodigo(self, codigo_grupo):
        for index in range(self.cbxGrupo.count()):
            if self.GrupoIndexMap.get(self.cbxGrupo.itemText(index)) == codigo_grupo:
                self.cbxGrupo.setCurrentIndex(index)
                break

    def buscarFornecedores(self):
        query = "SELECT F.CODFOR, F.DSCFOR FROM TBLFOR F"
        data = self.db.fetch_data(query)

        for index, row in enumerate(data):
            fornecedor = str(row[1])
            self.cbxFornecedor.addItem(fornecedor)
            self.FornecedorIndexMap[fornecedor] = int(row[0])

    def obterCodFornecedorSelecionado(self):
        fornecedor_selecionado = self.cbxFornecedor.currentText()
        if fornecedor_selecionado in self.FornecedorIndexMap:
            return self.FornecedorIndexMap[fornecedor_selecionado]
        return None

    def selecionarFornecedorPorCodigo(self, codigo_fornecedor):
        for index in range(self.cbxFornecedor.count()):
            if self.FornecedorIndexMap.get(self.cbxFornecedor.itemText(index)) == codigo_fornecedor:
                self.cbxFornecedor.setCurrentIndex(index)
                break
