from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon
from UCadClienteDialog import CadClienteDialog
from UCustomMessageBox import CustomMessageBox


class SubWindowClientes(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.subClientes = QtWidgets.QWidget()
        self.subClientes.setObjectName("subClientes")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.subClientes)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridClientes = QtWidgets.QTableWidget(self.subClientes)
        self.gridClientes.setObjectName("gridClientes")
        self.gridClientes.setColumnCount(6)
        self.gridClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridClientes.setHorizontalHeaderItem(5, item)
        self.gridClientes.horizontalHeader().setDefaultSectionSize(120)
        self.gridClientes.horizontalHeader().setMinimumSectionSize(100)
        self.gridClientes.verticalHeader().setDefaultSectionSize(13)
        self.gridClientes.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_7.addWidget(self.gridClientes)
        self.fraBotoesClientes = QtWidgets.QFrame(self.subClientes)
        self.fraBotoesClientes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesClientes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraBotoesClientes.setObjectName("fraBotoesClientes")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fraBotoesClientes)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnInserirClientes = QtWidgets.QPushButton(self.fraBotoesClientes)
        self.btnInserirClientes.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirClientes.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirClientes.setStyleSheet("background-color: transparent; \n"
                                              "border: none;")
        self.btnInserirClientes.setText("")
        self.btnInserirClientes.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirClientes.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirClientes.setObjectName("btnInserirClientes")
        self.horizontalLayout_7.addWidget(self.btnInserirClientes)
        self.btnEditarClientes = QtWidgets.QPushButton(self.fraBotoesClientes)
        self.btnEditarClientes.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarClientes.setStyleSheet("background-color: transparent; \n"
                                             "border: none;")
        self.btnEditarClientes.setText("")
        self.btnEditarClientes.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarClientes.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarClientes.setObjectName("btnEditarClientes")
        self.horizontalLayout_7.addWidget(self.btnEditarClientes)
        self.btnExcluirClientes = QtWidgets.QPushButton(self.fraBotoesClientes)
        self.btnExcluirClientes.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirClientes.setStyleSheet("background-color: transparent; \n"
                                              "border: none;")
        self.btnExcluirClientes.setText("")
        self.btnExcluirClientes.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirClientes.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirClientes.setObjectName("btnExcluirClientes")
        self.horizontalLayout_7.addWidget(self.btnExcluirClientes)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.btnFecharClientes = QtWidgets.QPushButton(self.fraBotoesClientes)
        self.btnFecharClientes.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharClientes.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharClientes.setStyleSheet("background-color: transparent; \n"
                                             "border: none;")
        self.btnFecharClientes.setText("")
        self.btnFecharClientes.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharClientes.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharClientes.setObjectName("btnFecharClientes")
        self.horizontalLayout_7.addWidget(self.btnFecharClientes)
        self.verticalLayout_7.addWidget(self.fraBotoesClientes)

        _translate = QtCore.QCoreApplication.translate
        self.subClientes.setWindowTitle(_translate("MainWindow", "Clientes"))
        item = self.gridClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.gridClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Inscrição"))
        item = self.gridClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.gridClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.gridClientes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Endereço"))

        self.gridClientes.setColumnWidth(4, 250)
        self.gridClientes.setColumnWidth(5, 500)

        self.btnInserirClientes.clicked.connect(self.inserirClientes)
        self.btnEditarClientes.clicked.connect(lambda event: self.editarClientes(self.gridClientes))
        self.btnExcluirClientes.clicked.connect(lambda event: self.excluirClientes(self.gridClientes))

        self.buscarClientes(self.gridClientes)
        self.gridClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def get(self):
        return self.subClientes

    def inserirClientes(self):
        cadCliente = CadClienteDialog(self.db, "Insert")
        cadCliente.exec_()

        self.buscarClientes(self.gridClientes)

    def editarClientes(self, gridClientes):
        selected_items = gridClientes.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()

            codigo = gridClientes.item(selected_row, 0).text()
            nome = gridClientes.item(selected_row, 1).text()
            inscricao = gridClientes.item(selected_row, 2).text()
            telefone = gridClientes.item(selected_row, 3).text()
            email = gridClientes.item(selected_row, 4).text()
            endereco = gridClientes.item(selected_row, 5).text()

            cadCliente = CadClienteDialog(self.db, "Edit", codigo)
            cadCliente.setWindowTitle("Editar cliente")

            cadCliente.edtNome.setText(nome)
            cadCliente.edtCpf.setText(inscricao)
            cadCliente.edtTelefone.setText(telefone)
            cadCliente.edtEmail.setText(email)
            cadCliente.edtEnd.setText(endereco)

            cadCliente.exec_()

            self.buscarClientes(gridClientes)

    def excluirClientes(self, gridClientes):
        try:
            selected_items = gridClientes.selectedItems()

            if selected_items:
                selected_row = selected_items[0].row()

                result = CustomMessageBox("Confirmar Exclusão", "Deseja excluir esse cliente?").confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridClientes.item(selected_row, 0).text())

                    delete_query = f"DELETE FROM TBLCLI C WHERE C.CODCLI = {codigo}"
                    self.db.execute_query(delete_query)

                    self.buscarClientes(gridClientes)
        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao excluir o cliente: {str(e)}")

    def buscarClientes(self, gridClientes):
        # Consulta à tabela TBLLAN usando a classe DatabaseManager
        query = "SELECT * FROM TBLCLI"
        data = self.db.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        gridClientes.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    gridClientes.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    if col_num == 0:
                        item = QtWidgets.QTableWidgetItem(str(value))
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                        gridClientes.setItem(row_num, col_num, item)
                    else:
                        gridClientes.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))