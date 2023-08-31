from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from UCustomMessageBox import CustomMessageBox
from UCadFornecedorDialog import CadFornecedorDialog


class SubWindowFornecedores(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.subFornecedores = QtWidgets.QWidget()
        self.subFornecedores.setObjectName("subFornecedores")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.subFornecedores)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridFornecedores = QtWidgets.QTableWidget(self.subFornecedores)
        self.gridFornecedores.setObjectName("gridFornecedores")
        self.gridFornecedores.setColumnCount(7)
        self.gridFornecedores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridFornecedores.setHorizontalHeaderItem(6, item)
        self.gridFornecedores.horizontalHeader().setDefaultSectionSize(120)
        self.gridFornecedores.horizontalHeader().setMinimumSectionSize(100)
        self.verticalLayout_8.addWidget(self.gridFornecedores)
        self.fraBotoesFornecedores = QtWidgets.QFrame(self.subFornecedores)
        self.fraBotoesFornecedores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesFornecedores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesFornecedores.setObjectName("fraBotoesFornecedores")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.fraBotoesFornecedores)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnInserirFornecedores = QtWidgets.QPushButton(self.fraBotoesFornecedores)
        self.btnInserirFornecedores.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirFornecedores.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirFornecedores.setStyleSheet("background-color: transparent; \n"
                                                  "border: none;")
        self.btnInserirFornecedores.setText("")
        self.btnInserirFornecedores.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirFornecedores.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirFornecedores.setObjectName("btnInserirFornecedores")
        self.horizontalLayout_8.addWidget(self.btnInserirFornecedores)
        self.btnEditarFornecedores = QtWidgets.QPushButton(self.fraBotoesFornecedores)
        self.btnEditarFornecedores.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarFornecedores.setStyleSheet("background-color: transparent; \n"
                                                 "border: none;")
        self.btnEditarFornecedores.setText("")
        self.btnEditarFornecedores.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarFornecedores.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarFornecedores.setObjectName("btnEditarFornecedores")
        self.horizontalLayout_8.addWidget(self.btnEditarFornecedores)
        self.btnExcluirFornecedores = QtWidgets.QPushButton(self.fraBotoesFornecedores)
        self.btnExcluirFornecedores.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirFornecedores.setStyleSheet("background-color: transparent; \n"
                                                  "border: none;")
        self.btnExcluirFornecedores.setText("")
        self.btnExcluirFornecedores.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirFornecedores.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirFornecedores.setObjectName("btnExcluirFornecedores")
        self.horizontalLayout_8.addWidget(self.btnExcluirFornecedores)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.btnFecharFornecedores = QtWidgets.QPushButton(self.fraBotoesFornecedores)
        self.btnFecharFornecedores.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharFornecedores.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharFornecedores.setStyleSheet("background-color: transparent; \n"
                                                 "border: none;")
        self.btnFecharFornecedores.setText("")
        self.btnFecharFornecedores.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharFornecedores.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharFornecedores.setObjectName("btnFecharFornecedores")
        self.horizontalLayout_8.addWidget(self.btnFecharFornecedores)
        self.verticalLayout_8.addWidget(self.fraBotoesFornecedores)

        _translate = QtCore.QCoreApplication.translate
        self.subFornecedores.setWindowTitle(_translate("MainWindow", "Fornecedores"))
        item = self.gridFornecedores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridFornecedores.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.gridFornecedores.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIPINS"))
        item = self.gridFornecedores.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Inscrição"))
        item = self.gridFornecedores.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.gridFornecedores.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email"))
        item = self.gridFornecedores.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Endereço"))

        self.gridFornecedores.setColumnHidden(2, True)
        self.gridFornecedores.setColumnWidth(5, 250)
        self.gridFornecedores.setColumnWidth(6, 500)

        self.btnInserirFornecedores.clicked.connect(self.inserirFornecedores)
        self.btnEditarFornecedores.clicked.connect(lambda event: self.editarFornecedores(self.gridFornecedores))
        self.btnExcluirFornecedores.clicked.connect(lambda event: self.excluirFornecedores(self.gridFornecedores))

        self.buscarFornecedores(self.gridFornecedores)
        self.gridFornecedores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get(self):
        return self.subFornecedores

    def inserirFornecedores(self):
        cadFornecedor = CadFornecedorDialog(self.db, "Insert")
        cadFornecedor.exec_()

        self.buscarFornecedores(self.gridFornecedores)

    def editarFornecedores(self, gridFornecedores):
        selected_items = gridFornecedores.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()

            codigo = gridFornecedores.item(selected_row, 0).text()
            nome = gridFornecedores.item(selected_row, 1).text()
            tipoInsc = gridFornecedores.item(selected_row, 2).text()
            inscricao = gridFornecedores.item(selected_row, 3).text()
            telefone = gridFornecedores.item(selected_row, 4).text()
            email = gridFornecedores.item(selected_row, 5).text()
            endereco = gridFornecedores.item(selected_row, 6).text()

            cadFornecedor = CadFornecedorDialog(self.db, "Edit", codigo)
            cadFornecedor.setWindowTitle("Editar fornecedor")

            cadFornecedor.edtNome.setText(nome)
            if tipoInsc == 'PF':
                cadFornecedor.rdgCPF.setChecked(True)
                cadFornecedor.edtIns.setText(inscricao)
            else:
                cadFornecedor.rdgCNPJ.setChecked(True)
                cadFornecedor.edtIns.setInputMask("99.999.999/9999-99")
                cadFornecedor.edtIns.setMaxLength(18)
                cadFornecedor.edtIns.setText(inscricao)
                cadFornecedor.lblIns.setText("CNPJ")
            cadFornecedor.edtTelefone.setText(telefone)
            cadFornecedor.edtEmail.setText(email)
            cadFornecedor.edtEnd.setText(endereco)

            cadFornecedor.exec_()

            self.buscarFornecedores(gridFornecedores)

    def excluirFornecedores(self, gridFornecedores):
        try:
            selected_items = gridFornecedores.selectedItems()

            if selected_items:
                selected_row = selected_items[0].row()

                result = CustomMessageBox("Confirmar Exclusão", "Deseja excluir esse fornecedor?").confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridFornecedores.item(selected_row, 0).text())

                    delete_query = f"DELETE FROM TBLFOR F WHERE C.CODFOR = {codigo}"
                    self.db.execute_query(delete_query)

                    self.buscarClientes(gridFornecedores)
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao excluir o fornecedor: {str(e)}")

    def buscarFornecedores(self, gridFornecedores):
        # Consulta à tabela TBLLAN usando a classe DatabaseManager
        query = "SELECT * FROM TBLFOR"
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        gridFornecedores.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    gridFornecedores.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    gridFornecedores.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))