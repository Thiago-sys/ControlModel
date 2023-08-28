from Modelos.Partida import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from UDataBaseManager import DatabaseManager
from PyQt5 import QtWidgets
from UCustomMessageBox import CustomMessageBox


class PartidaDialog(QDialog, Ui_Dialog):
    def __init__(self, db:DatabaseManager, grid, state, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.grid = grid
        self.state = state
        self.codigo = codigo

        self.btnGravar.setIcon(QIcon("icons/2x/save.png"))
        self.btnGravar.clicked.connect(self.gravar)

        self.btnCancelar.setIcon(QIcon("icons/2x/cancel.png"))
        self.btnCancelar.clicked.connect(self.cancelar)

        self.itemIndexMap = {}

        self.buscarItens()

    def gravar(self):

        if self.state == 'Insert':
            item_selecionado = self.obterCodItemSelecionado()
            produto = self.cbxProduto.currentText()
            quantidade = self.edtQntd.text()
            valor = self.dblValor.value()

            row_count = self.grid.rowCount()  # Obter o número atual de linhas
            self.grid.insertRow(row_count)  # Inserir uma nova linha na grid

            # Preencher as células da nova linha com os valores
            self.grid.setItem(row_count, 0, QtWidgets.QTableWidgetItem('0')) # Passando zero para evitar erro na hora de buscar os itens da grid
            self.grid.setItem(row_count, 1, QtWidgets.QTableWidgetItem(produto))
            self.grid.setItem(row_count, 2, QtWidgets.QTableWidgetItem(quantidade))
            self.grid.setItem(row_count, 3, QtWidgets.QTableWidgetItem(str(valor)))
            self.grid.setItem(row_count, 4, QtWidgets.QTableWidgetItem(str(item_selecionado)))

            result = CustomMessageBox("Pergunta", "Deseja inserir uma nova partida?").confirmation.exec_()

            if result == QtWidgets.QMessageBox.No:
                self.accept()
        else:
            confirmation = QtWidgets.QMessageBox.question(
                self, "Pergunta", "Confirma a edição da partida?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            if confirmation == QtWidgets.QMessageBox.Yes:
                item_selecionado = self.obterCodItemSelecionado()
                selected_items = self.grid.selectedItems()
                selected_row = selected_items[0].row()

                # Atualizar os valores na gridLan após a edição
                self.grid.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(str(self.codigo)))
                self.grid.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(self.cbxProduto.currentText()))
                self.grid.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(str(self.edtQntd.text())))
                self.grid.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(str(self.dblValor.value())))
                self.grid.setItem(selected_row, 4, QtWidgets.QTableWidgetItem(str(item_selecionado)))

                self.accept()

    def cancelar(self):
        self.reject()

    def buscarItens(self):
        query = "SELECT I.CODITE, I.DSCITE FROM TBLITE I"
        data = self.db.fetch_data(query)

        for index, row in enumerate(data):
            item = str(row[1])
            self.cbxProduto.addItem(item)
            self.itemIndexMap[item] = int(row[0])

    def obterCodItemSelecionado(self):
        item_selecionado = self.cbxProduto.currentText()
        if item_selecionado in self.itemIndexMap:
            return self.itemIndexMap[item_selecionado]
        return None
