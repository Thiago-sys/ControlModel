from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from UCadLanDialog import CadLanDialog
from UCustomMessageBox import CustomMessageBox
from datetime import datetime


class SubWindowLancamentos(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        
        self.subLan = QtWidgets.QWidget()
        self.subLan.setEnabled(True)
        self.subLan.setStyleSheet("")
        self.subLan.setObjectName("subLan")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.subLan)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLan = QtWidgets.QTableWidget(self.subLan)
        self.gridLan.setObjectName("gridLan")
        self.gridLan.setColumnCount(13)
        self.gridLan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridLan.setHorizontalHeaderItem(12, item)
        self.gridLan.horizontalHeader().setVisible(True)
        self.gridLan.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLan.horizontalHeader().setDefaultSectionSize(120)
        self.gridLan.horizontalHeader().setHighlightSections(True)
        self.gridLan.horizontalHeader().setMinimumSectionSize(120)
        self.gridLan.horizontalHeader().setSortIndicatorShown(False)
        self.gridLan.horizontalHeader().setStretchLastSection(False)
        self.gridLan.verticalHeader().setHighlightSections(True)
        self.verticalLayout_2.addWidget(self.gridLan)
        self.fraBotoesLan = QtWidgets.QFrame(self.subLan)
        self.fraBotoesLan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesLan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesLan.setObjectName("fraBotoesLan")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fraBotoesLan)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnInserirLan = QtWidgets.QPushButton(self.fraBotoesLan)
        self.btnInserirLan.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirLan.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirLan.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnInserirLan.setText("")
        self.btnInserirLan.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirLan.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirLan.setObjectName("btnInserirLan")
        self.horizontalLayout_6.addWidget(self.btnInserirLan)
        self.btnEditarLan = QtWidgets.QPushButton(self.fraBotoesLan)
        self.btnEditarLan.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarLan.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnEditarLan.setText("")
        self.btnEditarLan.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarLan.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarLan.setObjectName("btnEditarLan")
        self.horizontalLayout_6.addWidget(self.btnEditarLan)
        self.btnExcluirLan = QtWidgets.QPushButton(self.fraBotoesLan)
        self.btnExcluirLan.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirLan.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnExcluirLan.setText("")
        self.btnExcluirLan.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirLan.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirLan.setObjectName("btnExcluirLan")
        self.horizontalLayout_6.addWidget(self.btnExcluirLan)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btnFecharLan = QtWidgets.QPushButton(self.fraBotoesLan)
        self.btnFecharLan.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharLan.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharLan.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnFecharLan.setText("")
        self.btnFecharLan.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharLan.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharLan.setObjectName("btnFecharLan")
        self.horizontalLayout_6.addWidget(self.btnFecharLan)
        self.verticalLayout_2.addWidget(self.fraBotoesLan)

        _translate = QtCore.QCoreApplication.translate
        self.subLan.setWindowTitle(_translate("MainWindow", "Lançamentos"))
        item = self.gridLan.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridLan.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data do lançamento"))
        item = self.gridLan.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Operação"))
        item = self.gridLan.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.gridLan.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Código do Item"))
        item = self.gridLan.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Item"))
        item = self.gridLan.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Quantidade"))
        item = self.gridLan.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Código do Cliente"))
        item = self.gridLan.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.gridLan.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Código do Fornecedor"))
        item = self.gridLan.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Fornecedor"))
        item = self.gridLan.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Complemento"))
        item = self.gridLan.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Grupo do lançamento"))

        self.gridLan.setColumnHidden(4, True) # Ocultando a coluna de Código do Item
        self.gridLan.setColumnWidth(5, 200)   # Redimencionando a coluna de Item
        self.gridLan.setColumnHidden(7, True) # Ocultando a coluna de Código do Cliente
        self.gridLan.setColumnWidth(8, 200)   # Redimencionando a coluna de Cliente
        self.gridLan.setColumnHidden(9, True) # Ocultando a coluna de Código do Fornecedor
        self.gridLan.setColumnWidth(10, 200)  # Redimencionando a coluna de Fornecedor
        self.gridLan.setColumnWidth(11, 300)  # Redimencionando a coluna de Complemento
        self.gridLan.setColumnWidth(12, 200)  # Redimencionando a coluna de Grupo

        self.btnInserirLan.clicked.connect(self.inserirLan)
        self.btnEditarLan.clicked.connect(lambda event: self.editarLan(self.gridLan))
        self.btnExcluirLan.clicked.connect(lambda event: self.excluirLan(self.gridLan))

        self.buscarlancamentos(self.gridLan)
        self.gridLan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get(self):
        return self.subLan

    def inserirLan(self):
        cadlan = CadLanDialog(self.db, "Insert")
        cadlan.exec_()

        self.buscarlancamentos(self.gridLan)

    def editarLan(self, gridLan):
        selected_items = gridLan.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()

            # Obter os dados da linha selecionada
            data_objeto = datetime.strptime(gridLan.item(selected_row, 1).text(), "%d/%m/%Y")
            data = data_objeto.strftime("%Y-%m-%d")  # Data do lançamento
            natureza = gridLan.item(selected_row, 2).text()  # Natureza (Venda ou Compra)
            codigoCliente = gridLan.item(selected_row, 7).text()  # Código do cliente
            codigoFornecedor = gridLan.item(selected_row, 9).text() # Código do fornecedor
            complemento = gridLan.item(selected_row, 11).text()  # Complemento
            grupo = gridLan.item(selected_row, 12).text()  # Grupo (GRPLAN)

            codigo = self.buscarCodigos(data, grupo)

            cadlan = CadLanDialog(self.db, "Edit", codigo, grupo)
            cadlan.setWindowTitle("Editar Lançamento")
            cadlan.dteDtaVendas.setDisabled(True)
            cadlan.dteDtaCompras.setDisabled(True)

            try:
                # Abrir a tela CadLanDialog com os dados preenchidos
                if natureza == 'Venda':
                    cadlan.tabWidget.setCurrentIndex(0)  # Selecionar a tab de vendas
                    cadlan.tabWidget.setTabEnabled(1, False)

                    cadlan.dteDtaVendas.setDate(QtCore.QDate.fromString(data, "yyyy-MM-dd"))
                    cadlan.selecionarClientePorCodigo(codigoCliente)
                    cadlan.edtCompVendas.setPlainText(complemento)

                    grid = cadlan.gridLanVendas

                    # Consultar os itens do grupo de lançamentos e preencher a grid
                    query_itens = f"SELECT L.CODLAN, I.DSCITE, L.QTDITE, L.VLRLAN, L.CODITE " \
                                  f"FROM TBLLAN L LEFT JOIN TBLITE I ON L.CODITE = I.CODITE WHERE GRPLAN = {grupo}"
                    data_itens = self.db.fetch_data(query_itens)

                    grid.setRowCount(len(data_itens))
                    for row_num, row_data in enumerate(data_itens):
                        for col_num, value in enumerate(row_data):
                            grid.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))

                    cadlan.calcularSaldoTotal(grid, cadlan.dblValorTotVendas)
                    cadlan.exec_()
                elif natureza == 'Compra':
                    cadlan.tabWidget.setCurrentIndex(1)  # Selecionar a tab de compras # Selecionar a tab de vendas
                    cadlan.tabWidget.setTabEnabled(0, False)

                    cadlan.dteDtaCompras.setDate(QtCore.QDate.fromString(data, "yyyy-MM-dd"))
                    cadlan.selecionarFornecedorPorCodigo(codigoFornecedor)
                    cadlan.edtCompCompras.setPlainText(complemento)

                    grid = cadlan.gridLanCompras

                    # Consultar os itens do grupo de lançamentos e preencher a grid
                    query_itens = f"SELECT L.CODLAN, I.DSCITE, L.QTDITE, L.VLRLAN, L.CODITE " \
                                  f"FROM TBLLAN L LEFT JOIN TBLITE I ON L.CODITE = I.CODITE WHERE GRPLAN = {grupo}"
                    data_itens = self.db.fetch_data(query_itens)

                    grid.setRowCount(len(data_itens))
                    for row_num, row_data in enumerate(data_itens):
                        for col_num, value in enumerate(row_data):
                            grid.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))

                    cadlan.calcularSaldoTotal(grid, cadlan.dblValorTotVendas)
                    cadlan.exec_()
            except Exception as e:
                self.db.connection.rollback()  # Desfaz as alterações em caso de erro
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao buscar os lançamentos: {str(e)}")

        self.buscarlancamentos(self.gridLan)

    def excluirLan(self, gridLan):
        try:
            selected_items = gridLan.selectedItems()

            if selected_items:
                selected_row = selected_items[0].row()

                result = CustomMessageBox("Confirmar Exclusão", "Deseja excluir esse grupo de lançamento? \n"
                                          "Ao realizar essa ação todos os lançamentos do grupo serão excluídos").confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridLan.item(selected_row, 12).text())

                    delete_query = f"DELETE FROM TBLLAN L WHERE L.GRPLAN = {codigo}"
                    self.db.execute_query(delete_query)

                    self.buscarlancamentos(gridLan)
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao excluir os lançamento(s): {str(e)}")

    def buscarlancamentos(self, gridLan):
        # Consulta à tabela TBLLAN usando a classe DatabaseManager
        query = "SELECT L.CODLAN, L.DTALAN, IF(L.NATLAN = 'V', 'Venda', 'Compra') AS NATUREZA, L.VLRLAN, L.CODITE, " \
                "I.DSCITE, L.QTDITE, L.CODCLI, C.DSCCLI, L.CODFOR, F.DSCFOR, L.COMLAN, L.GRPLAN                    " \
                "FROM TBLLAN L LEFT JOIN TBLITE I ON L.CODITE = I.CODITE                                           " \
                "              LEFT JOIN TBLCLI C ON L.CODCLI = C.CODCLI                                           " \
                "              LEFT JOIN TBLFOR F ON L.CODFOR = F.CODFOR                                           "
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        gridLan.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    if col_num == 0:
                        item = QtWidgets.QTableWidgetItem(str(value))
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        gridLan.setItem(row_num, col_num, item)
                    elif col_num == 1:
                        data_objeto = datetime.strptime(str(value), "%Y-%m-%d")
                        data_formatada = data_objeto.strftime("%d/%m/%Y")
                        gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(data_formatada))
                    elif col_num == 3:
                        item = QtWidgets.QTableWidgetItem(
                            'R$ {:,.2f}'.format(value).replace(',', '.').replace('.', ','))
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        gridLan.setItem(row_num, col_num, item)
                    else:
                        gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))

    def buscarCodigos(self, data, grupo):
        query = "SELECT L.CODLAN FROM TBLLAN L WHERE L.DTALAN = %s AND L.GRPLAN = %s"
        cods = self.db.fetch_data(query, (data, grupo))

        cods_list = [cod[0] for cod in cods]
        return cods_list

