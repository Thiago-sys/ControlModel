from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from UCustomMessageBox import CustomMessageBox
from UMovEstoqueDialog import MovEstoqueDialog
from datetime import datetime


class SubWindowEstoque(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.subEst = QtWidgets.QWidget()
        self.subEst.setObjectName("subEst")
        self.gridLayout = QtWidgets.QGridLayout(self.subEst)
        self.gridLayout.setObjectName("gridLayout")
        self.fraMovEst = QtWidgets.QFrame(self.subEst)
        self.fraMovEst.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraMovEst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraMovEst.setObjectName("fraMovEst")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fraMovEst)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblMovEst = QtWidgets.QLabel(self.fraMovEst)
        self.lblMovEst.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMovEst.setObjectName("lblMovEst")
        self.verticalLayout_3.addWidget(self.lblMovEst)
        self.gridMovEst = QtWidgets.QTableWidget(self.fraMovEst)
        self.gridMovEst.setObjectName("gridMovEst")
        self.gridMovEst.setColumnCount(11)
        self.gridMovEst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridMovEst.setHorizontalHeaderItem(10, item)
        self.gridMovEst.horizontalHeader().setMinimumSectionSize(50)
        self.verticalLayout_3.addWidget(self.gridMovEst)
        self.gridLayout.addWidget(self.fraMovEst, 0, 0, 1, 1)
        self.fraEst = QtWidgets.QFrame(self.subEst)
        self.fraEst.setMinimumSize(QtCore.QSize(315, 0))
        self.fraEst.setMaximumSize(QtCore.QSize(315, 16777215))
        self.fraEst.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraEst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraEst.setObjectName("fraEst")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fraEst)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblEst = QtWidgets.QLabel(self.fraEst)
        self.lblEst.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEst.setObjectName("lblEst")
        self.verticalLayout_6.addWidget(self.lblEst)
        self.gridEst = QtWidgets.QTableWidget(self.fraEst)
        self.gridEst.setObjectName("gridEst")
        self.gridEst.setColumnCount(4)
        self.gridEst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.gridEst)
        self.gridLayout.addWidget(self.fraEst, 0, 1, 1, 1)
        self.fraBotoesEst = QtWidgets.QFrame(self.subEst)
        self.fraBotoesEst.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesEst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesEst.setObjectName("fraBotoesEst")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraBotoesEst)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnInserirEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnInserirEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnInserirEst.setText("")
        self.btnInserirEst.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirEst.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setObjectName("btnInserirEst")
        self.horizontalLayout_2.addWidget(self.btnInserirEst)
        self.btnEditarEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnEditarEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarEst.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnEditarEst.setText("")
        self.btnEditarEst.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarEst.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarEst.setObjectName("btnEditarEst")
        self.horizontalLayout_2.addWidget(self.btnEditarEst)
        self.btnExcluirEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnExcluirEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirEst.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnExcluirEst.setText("")
        self.btnExcluirEst.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirEst.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirEst.setObjectName("btnExcluirEst")
        self.horizontalLayout_2.addWidget(self.btnExcluirEst)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnFecharEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnFecharEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharEst.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharEst.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnFecharEst.setText("")
        self.btnFecharEst.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharEst.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharEst.setObjectName("btnFecharEst")
        self.horizontalLayout_2.addWidget(self.btnFecharEst)
        self.gridLayout.addWidget(self.fraBotoesEst, 1, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate
        self.subEst.setWindowTitle(_translate("MainWindow", "Estoque"))
        self.lblMovEst.setText(_translate("MainWindow", "Movimentação de estoque"))
        item = self.gridMovEst.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridMovEst.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.gridMovEst.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Natureza"))
        item = self.gridMovEst.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CODITE"))
        item = self.gridMovEst.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Item"))
        item = self.gridMovEst.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Quantidade"))
        item = self.gridMovEst.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CODCLI"))
        item = self.gridMovEst.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.gridMovEst.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "CODFOR"))
        item = self.gridMovEst.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Fornecedor"))
        item = self.gridMovEst.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Complemento"))
        self.lblEst.setText(_translate("MainWindow", "Estoque"))
        item = self.gridEst.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridEst.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CODITE"))
        item = self.gridEst.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item"))
        item = self.gridEst.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantidade"))

        self.gridMovEst.setColumnHidden(3, True)  # Ocultando a coluna de Código do Item
        self.gridMovEst.setColumnWidth(4, 200)  # Redimencionando a coluna de Item
        self.gridMovEst.setColumnHidden(6, True)  # Ocultando a coluna de Código do Cliente
        self.gridMovEst.setColumnWidth(7, 200)  # Redimencionando a coluna de Cliente
        self.gridMovEst.setColumnHidden(8, True)  # Ocultando a coluna de Código do Fornecedor
        self.gridMovEst.setColumnWidth(9, 200)  # Redimencionando a coluna de Fornecedor
        self.gridMovEst.setColumnWidth(10, 300)  # Redimencionando a coluna de Fornecedor

        self.gridEst.setColumnWidth(0, 60) # Diminuindo o tamanho do campo de código na tabela de estoque
        self.gridEst.setColumnHidden(1, True) # Ocultando a coluna de código do item

        self.btnInserirEst.clicked.connect(self.inserirMovEst)
        self.btnEditarEst.clicked.connect(lambda event: self.editarMovEst(self.gridMovEst))
        self.btnExcluirEst.clicked.connect(lambda event: self.excluirMovEst(self.gridMovEst))

        self.buscarDados()
        self.gridMovEst.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get(self):
        return self.subEst

    def inserirMovEst(self):
        cadMovEst = MovEstoqueDialog(self.db, "Insert")
        cadMovEst.exec_()

    def editarMovEst(self, gridMovEst):
        selected_items = gridMovEst.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()

            # Obter os dados da linha selecionada
            codigo = gridMovEst.item(selected_row, 0).text()
            data_objeto = datetime.strptime(gridMovEst.item(selected_row, 1).text(), "%d/%m/%Y")
            data = data_objeto.strftime("%Y-%m-%d")  # Data do lançamento
            natureza = gridMovEst.item(selected_row, 2).text()  # Natureza (Venda ou Compra)
            codItem = gridMovEst.item(selected_row, 3).text() # Código do Item
            qntd = gridMovEst.item(selected_row, 5).text() # Quantidade
            codigoCliente = gridMovEst.item(selected_row, 6).text()  # Código do cliente
            codigoFornecedor = gridMovEst.item(selected_row, 8).text() # Código do fornecedor
            complemento = gridMovEst.item(selected_row, 10).text()

            cadMovEst = MovEstoqueDialog(self.db, "Edit", codigo)
            cadMovEst.setWindowTitle("Editar movimentação de estoque")
            cadMovEst.dteDataSaida.setDisabled(True)
            cadMovEst.dteDataEntrada.setDisabled(True)

            try:
                # Abrir a tela CadLanDialog com os dados preenchidos
                if natureza == 'Entrada':
                    cadMovEst.tabWidget.setCurrentIndex(0)  # Selecionar a tab de Entrada
                    cadMovEst.tabWidget.setTabEnabled(1, False)

                    cadMovEst.dteDataEntrada.setDate(QtCore.QDate.fromString(data, "yyyy-MM-dd"))
                    cadMovEst.selecionarFornecedorPorCodigo(codigoFornecedor)
                    cadMovEst.edtQntdEntrada.setText(qntd)
                    cadMovEst.selecionarItemPorCodigo(codItem, 'C')
                    cadMovEst.edtCompEntrada.setText(complemento)

                    cadMovEst.exec_()
                elif natureza == 'Saída':
                    cadMovEst.tabWidget.setCurrentIndex(1)  # Selecionar a tab de saídas
                    cadMovEst.tabWidget.setTabEnabled(0, False)

                    cadMovEst.dteDataEntrada.setDate(QtCore.QDate.fromString(data, "yyyy-MM-dd"))
                    cadMovEst.selecionarClientePorCodigo(codigoCliente)
                    cadMovEst.edtQntdEntrada.setText(qntd)
                    cadMovEst.selecionarItemPorCodigo(codItem, 'V')
                    cadMovEst.edtCompSaida.setText(complemento)

                    cadMovEst.exec_()
            except Exception as e:
                self.db.connection.rollback()  # Desfaz as alterações em caso de erro
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {str(e)}")

        self.buscarDados()

    def excluirMovEst(self, gridMovEst):
        try:
            selected_items = gridMovEst.selectedItems()

            if selected_items:
                selected_row = selected_items[0].row()

                result = CustomMessageBox("Confirmar Exclusão", "Deseja realmente excluir esta movimentação?").confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridMovEst.item(selected_row, 0).text())

                    delete_query = f"DELETE FROM TBLMOVEST M WHERE M.CODMOVEST = {codigo}"
                    self.db.execute_query(delete_query)

                    CustomMessageBox("Sucesso", "Movimentação excluída com sucesso.").information.exec_()

                    self.buscarDados()
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao excluir a movimentação: {str(e)}")

    def buscarDados(self):
        # Consulta à tabela TBLMOVEST usando a classe DatabaseManager
        query = "SELECT M.CODMOVEST, M.DTAMOV, IF(M.NATMOV = 'C', 'Entrada', 'Saída') AS NATUREZA, M.CODITE, I.DSCITE," \
                "M.QTD, M.CODCLI, C.DSCCLI, M.CODFOR, F.DSCFOR, M.COMMOV                                              " \
                "FROM TBLMOVEST M LEFT JOIN TBLITE I ON M.CODITE = I.CODITE                                           " \
                "                 LEFT JOIN TBLCLI C ON M.CODCLI = C.CODCLI                                           " \
                "                 LEFT JOIN TBLFOR F ON M.CODFOR = F.CODFOR                                           "
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        self.gridMovEst.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    self.gridMovEst.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    if col_num == 1:
                        data_objeto = datetime.strptime(str(value), "%Y-%m-%d")
                        data_formatada = data_objeto.strftime("%d/%m/%Y")
                        self.gridMovEst.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(data_formatada))
                    else:
                        self.gridMovEst.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))

        # Consulta à tabela TBLEST usando a classe DatabaseManager
        query = "SELECT E.CODEST, E.CODITE, I.DSCITE, E.QTD              " \
                "FROM TBLEST E LEFT JOIN TBLITE I ON E.CODITE = I.CODITE "
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        self.gridEst.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    self.gridEst.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    self.gridEst.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))