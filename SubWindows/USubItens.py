from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from UCadItensDialog import CadItensDialog
from datetime import datetime
from UCustomMessageBox import CustomMessageBox


class SubWindowItens(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.subItens = QtWidgets.QWidget()
        self.subItens.setObjectName("subItens")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.subItens)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridItens = QtWidgets.QTableWidget(self.subItens)
        self.gridItens.setObjectName("gridItens")
        self.gridItens.setColumnCount(8)
        self.gridItens.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridItens.setHorizontalHeaderItem(7, item)
        self.gridItens.horizontalHeader().setDefaultSectionSize(130)
        self.gridItens.horizontalHeader().setMinimumSectionSize(130)
        self.gridItens.verticalHeader().setDefaultSectionSize(13)
        self.gridItens.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_4.addWidget(self.gridItens)
        self.fraBotoesItens = QtWidgets.QFrame(self.subItens)
        self.fraBotoesItens.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesItens.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesItens.setObjectName("fraBotoesItens")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fraBotoesItens)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnInserirItens = QtWidgets.QPushButton(self.fraBotoesItens)
        self.btnInserirItens.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirItens.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirItens.setStyleSheet("background-color: transparent; \n"
                                           "border: none;")
        self.btnInserirItens.setText("")
        self.btnInserirItens.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirItens.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirItens.setObjectName("btnInserirItens")
        self.horizontalLayout_4.addWidget(self.btnInserirItens)
        self.btnEditarItens = QtWidgets.QPushButton(self.fraBotoesItens)
        self.btnEditarItens.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarItens.setStyleSheet("background-color: transparent; \n"
                                          "border: none;")
        self.btnEditarItens.setText("")
        self.btnEditarItens.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarItens.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarItens.setObjectName("btnEditarItens")
        self.horizontalLayout_4.addWidget(self.btnEditarItens)
        self.btnExcluirItens = QtWidgets.QPushButton(self.fraBotoesItens)
        self.btnExcluirItens.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirItens.setStyleSheet("background-color: transparent; \n"
                                           "border: none;")
        self.btnExcluirItens.setText("")
        self.btnExcluirItens.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirItens.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirItens.setObjectName("btnExcluirItens")
        self.horizontalLayout_4.addWidget(self.btnExcluirItens)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btnFecharItens = QtWidgets.QPushButton(self.fraBotoesItens)
        self.btnFecharItens.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharItens.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharItens.setStyleSheet("background-color: transparent; \n"
                                          "border: none;")
        self.btnFecharItens.setText("")
        self.btnFecharItens.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharItens.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharItens.setObjectName("btnFecharItens")
        self.horizontalLayout_4.addWidget(self.btnFecharItens)
        self.verticalLayout_4.addWidget(self.fraBotoesItens)

        _translate = QtCore.QCoreApplication.translate
        self.subItens.setWindowTitle(_translate("MainWindow", "Itens"))
        item = self.gridItens.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridItens.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.gridItens.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data da última compra"))
        item = self.gridItens.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor de compra"))
        item = self.gridItens.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CODFOR"))
        item = self.gridItens.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fornecedor"))
        item = self.gridItens.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CODGRP"))
        item = self.gridItens.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Grupo"))

        self.gridItens.setColumnHidden(4, True)
        self.gridItens.setColumnHidden(6, True)

        self.btnInserirItens.clicked.connect(self.inserir)
        self.btnEditarItens.clicked.connect(lambda event: self.editar(self.gridItens))
        self.btnExcluirItens.clicked.connect(lambda event: self.excluir(self.gridItens))

        self.buscarItens(self.gridItens)

        self.gridItens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get(self):
        return self.subItens

    def inserir(self):
        cadItens = CadItensDialog(self.db, "Insert")
        cadItens.exec_()

        self.buscarItens(self.gridItens)

    def editar(self, gridItem):
        selected_items = gridItem.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()

            codigo = gridItem.item(selected_row, 0).text()
            descricao = gridItem.item(selected_row, 1).text()
            valor = float(gridItem.item(selected_row, 2).text().replace('R$ ', '').replace('.', '').replace(',', '.'))
            data_objeto = datetime.strptime(gridItem.item(selected_row, 3).text(), "%d/%m/%Y")
            data = data_objeto.strftime("%Y-%m-%d")
            codFornecedor = gridItem.item(selected_row, 4).text()
            codGrupo = gridItem.item(selected_row, 6).text()

            cadItem = CadItensDialog(self.db, "Edit", codigo)
            cadItem.setWindowTitle("Editar Item")

            cadItem.edtDescricao.setText(descricao)
            cadItem.dteData.setDate(QtCore.QDate.fromString(data, "yyyy-MM-dd"))
            cadItem.dblValor.setValue(valor)
            cadItem.selecionarFornecedorPorCodigo(codFornecedor)
            cadItem.selecionarGrupoPorCodigo(codGrupo)

            cadItem.exec_()

            self.buscarItens(gridItem)

    def excluir(self, gridItem):
        try:
            selected_items = gridItem.selectedItems()

            if selected_items:
                selected_row = selected_items[0].row()

                result = CustomMessageBox("Confirmar Exclusão", "Deseja excluir esse item?").confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridItem.item(selected_row, 0).text())

                    delete_query = f"DELETE FROM TBLITE I WHERE I.CODITE = {codigo}"
                    self.db.execute_query(delete_query)

                    self.buscarItens(gridItem)
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao excluir o item: {str(e)}")

    def buscarItens(self, grid):
        # Consulta à tabela TBLLAN usando a classe DatabaseManager
        query = "SELECT I.CODITE, I.DSCITE, I.VLRITE, I.DTAAQU, I.CODFOR, F.DSCFOR, I.CODGRP, G.DSCGRP " \
                "FROM TBLITE I LEFT JOIN TBLFOR F ON I.CODFOR = F.CODFOR                               " \
                "              LEFT JOIN TBLGRP G ON I.CODGRP = G.CODGRP                               "
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        grid.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    grid.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    if col_num == 0:
                        item = QtWidgets.QTableWidgetItem(str(value))
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        grid.setItem(row_num, col_num, item)
                    elif col_num == 2:
                        grid.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(
                            'R$ {:,.2f}'.format(value).replace(',', ';').replace('.', ',').replace(';', '.')))
                    elif col_num == 3:
                        data_objeto = datetime.strptime(str(value), "%Y-%m-%d")
                        data_formatada = data_objeto.strftime("%d/%m/%Y")
                        item = QtWidgets.QTableWidgetItem(data_formatada)
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        grid.setItem(row_num, col_num, item)
                    else:
                        grid.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))