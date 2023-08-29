from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from Modelos.CadLan import Ui_Dialog
from PyQt5.QtGui import QIcon
from UPartidaDialog import PartidaDialog
from UDataBaseManager import DatabaseManager
from datetime import date
from UCustomMessageBox import CustomMessageBox


class CadLanDialog(QDialog, Ui_Dialog):
    def __init__(self, db: DatabaseManager, state: str, codigo=None, grupo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigoLancamento = codigo
        self.grupo = grupo

        self.btnGravar.setIcon(QIcon("icons/2x/save.png"))
        self.btnGravar.clicked.connect(self.gravar)

        self.btnCancelar.setIcon(QIcon("icons/2x/cancel.png"))
        self.btnCancelar.clicked.connect(self.cancelar)

        self.btnInsertVendas.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInsertCompras.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInsertVendas.clicked.connect(self.inserirvenda)
        self.btnInsertCompras.clicked.connect(self.inserircompra)

        self.btnEditVendas.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditCompras.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditVendas.clicked.connect(self.editarvenda)
        self.btnEditCompras.clicked.connect(self.editarcompra)

        self.btnDeleteVendas.setIcon(QIcon("icons/2x/delete.png"))
        self.btnDeleteCompras.setIcon(QIcon("icons/2x/delete.png"))
        self.btnDeleteVendas.clicked.connect(self.deletarvenda)
        self.btnDeleteCompras.clicked.connect(self.deletarcompra)

        self.gridLanVendas.horizontalHeader().setMinimumSectionSize(30)
        self.gridLanVendas.setColumnWidth(0, 58)
        self.gridLanVendas.verticalHeader().setMinimumSectionSize(0)
        self.gridLanVendas.verticalHeader().setDefaultSectionSize(20)
        self.gridLanVendas.horizontalHeader().setMinimumSectionSize(30)
        self.gridLanCompras.setColumnWidth(0, 58)
        self.gridLanCompras.verticalHeader().setMinimumSectionSize(0)
        self.gridLanCompras.verticalHeader().setDefaultSectionSize(20)

        self.dteDtaCompras.setDate(date.today())
        self.dteDtaVendas.setDate(date.today())

        self.ClienteIndexMap = {}
        self.FornecedorIndexMap = {}

        self.buscarClientes()
        self.buscarFornecedores()

        self.gridLanVendas.setColumnHidden(4, True)  # Ocultando a coluna de Código do Item
        self.gridLanCompras.setColumnHidden(4, True)  # Ocultando a coluna de Código do Item

        self.codigoExcluido = []

        self.gridLanCompras.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridLanVendas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def gravar(self):
        try:
            if self.state == 'Insert':
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente gravar este lançamento?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    if self.tabWidget.currentIndex() == 0:
                        # Coletar dados da interface do usuário
                        data = self.dteDtaVendas.date().toPyDate()
                        natureza = 'V'
                        codCliente = int(self.obterCodClienteSelecionado())
                        complemento = self.edtCompVendas.toPlainText()
                        grupo = self.obtemGrupoLan()

                        # Preparar a consulta SQL para inserção de um lançamento
                        insert_query = "INSERT INTO TBLLAN (DTALAN, NATLAN, VLRLAN, CODCLI, CODITE, QTDITE, COMLAN, GRPLAN) " \
                                       "            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                        # Percorrendo a gridLanVendas
                        grid = self.gridLanVendas
                        for row in range(grid.rowCount()):
                            codItem = int(grid.item(row, 4).text())  # Obtém o código do item da coluna 0
                            quantidade = int(grid.item(row, 2).text())  # Obtém a quantidade da coluna 2
                            valor = float(grid.item(row, 3).text())  # Obtém o valor da coluna 3

                            # Preparar os valores para a inserção na TBLLAN
                            values = (data, natureza, valor, codCliente, codItem, quantidade, complemento, grupo)

                            # Executar a consulta SQL de inserção
                            self.db.execute_query(insert_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Lançamento(s) gravado(s) com sucesso.").information.exec_()
                        self.accept()
                    else:
                        # Coletar dados da interface do usuário
                        data = self.dteDtaCompras.date().toPyDate()
                        natureza = 'C'
                        codFornecedor = int(self.obterCodFornecedorSelecionado())
                        complemento = self.edtCompCompras.toPlainText()
                        grupo = self.obtemGrupoLan()

                        # Preparar a consulta SQL para inserção de um lançamento
                        insert_query = "INSERT INTO TBLLAN (DTALAN, NATLAN, VLRLAN, CODFOR, CODITE, QTDITE, COMLAN, GRPLAN) " \
                                       "            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                        # Percorrendo a gridLanVendas
                        grid = self.gridLanCompras
                        for row in range(grid.rowCount()):
                            codItem = int(grid.item(row, 4).text())  # Obtém o código do item da coluna 0
                            quantidade = int(grid.item(row, 2).text())  # Obtém a quantidade da coluna 2
                            valor = float(grid.item(row, 3).text())  # Obtém o valor da coluna 3

                            # Preparar os valores para a inserção na TBLLAN
                            values = (data, natureza, valor, codFornecedor, codItem, quantidade, complemento, grupo)

                            # Executar a consulta SQL de inserção
                            self.db.execute_query(insert_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Lançamento(s) gravado(s) com sucesso.").information.exec_()
                        self.accept()
            else:
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente gravar este lançamento?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:

                    if self.tabWidget.currentIndex() == 0:
                        # Coletar dados da interface do usuário
                        data = self.dteDtaVendas.date().toPyDate()
                        natureza = 'V'
                        codCliente = int(self.obterCodClienteSelecionado())
                        complemento = self.edtCompVendas.toPlainText()

                        # Percorrendo a gridLanVendas
                        grid = self.gridLanVendas
                        for row in range(grid.rowCount()):
                            codigo = int(grid.item(row, 0).text())  # Obtém o código do do lançamento da coluna 0
                            quantidade = int(grid.item(row, 2).text())  # Obtém a quantidade da coluna 2
                            valor = float(grid.item(row, 3).text())  # Obtém o valor da coluna 3
                            codItem = int(grid.item(row, 4).text())
                            if codigo != 0:
                                # Preparar a consulta SQL para inserção de um lançamento
                                update_query = "UPDATE TBLLAN SET NATLAN = %s, VLRLAN = %s, CODCLI = %s, CODITE = %s,   " \
                                               "QTDITE = %s, COMLAN = %s WHERE CODLAN = %s AND DTALAN = %s"

                                # Preparar os valores para a inserção na TBLLAN
                                values = (natureza, valor, codCliente, codItem, quantidade, complemento, self.codigoLancamento[row], data)

                                # Executar a consulta SQL de inserção
                                self.db.execute_query(update_query, values)
                            else:
                                # Preparar a consulta SQL para inserção de um lançamento
                                insert_query = "INSERT INTO TBLLAN (DTALAN, NATLAN, VLRLAN, CODCLI, CODITE, QTDITE, COMLAN, GRPLAN) " \
                                               "            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                                values = (data, natureza, valor, codCliente, codItem, quantidade, complemento, self.grupo)

                                self.db.execute_query(insert_query, values)

                        if len(self.codigoExcluído) > 0:
                            for i in self.codigoExcluído:
                                query_delete = f"DELETE FROM TBLLAN L WHERE L.CODLAN = {i}"
                                self.db.execute_query(query_delete)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Lançamento(s) gravado(s) com sucesso.").information.exec_()
                        self.accept()

                    else:
                        # Coletar dados da interface do usuário
                        data = self.dteDtaCompras.date().toPyDate()
                        natureza = 'C'
                        codFornecedor = int(self.obterCodFornecedorSelecionado())
                        complemento = self.edtCompCompras.toPlainText()

                        # Percorrendo a gridLanVendas
                        grid = self.gridLanCompras
                        for row in range(grid.rowCount()):
                            codigo = int(grid.item(row, 0).text())  # Obtém o código do item da coluna 0
                            quantidade = int(grid.item(row, 2).text())  # Obtém a quantidade da coluna 2
                            valor = float(grid.item(row, 3).text())  # Obtém o valor da coluna 3
                            codItem = int(grid.item(row, 4).text())  # Obtém o código do item da coluna 4

                            if codigo in self.codigoLancamento:
                                # Preparar a consulta SQL para inserção de um lançamento
                                update_query = "UPDATE TBLLAN SET NATLAN = %s, VLRLAN = %s, CODFOR = %s, CODITE = %s, " \
                                               "QTDITE = %s, COMLAN = %s WHERE CODLAN = %s AND DTALAN = %s"

                                # Preparar os valores para a inserção na TBLLAN
                                values = (natureza, valor, codFornecedor, codItem, quantidade, complemento, self.codigoLancamento[row], data)

                                # Executar a consulta SQL de inserção
                                self.db.execute_query(update_query, values)
                            else:
                                # Preparar a consulta SQL para inserção de um lançamento
                                insert_query = "INSERT INTO TBLLAN (DTALAN, NATLAN, VLRLAN, CODFOR, CODITE, QTDITE, COMLAN, GRPLAN) " \
                                               "            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                                values = (data, natureza, valor, codFornecedor, codItem, quantidade, complemento, self.grupo)

                                self.db.execute_query(insert_query, values)

                        if len(self.codigoExcluído) > 0:
                            for i in self.codigoExcluído:
                                query_delete = f"DELETE FROM TBLLAN L WHERE L.CODLAN = {i}"
                                self.db.execute_query(query_delete)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Lançamento(s) gravado(s) com sucesso.").information.exec_()
                        self.accept()

        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            CustomMessageBox("Erro", f"Erro ao gravar lançamento(s): {str(e)}").error.exec_()
            self.reject()

    def cancelar(self):
        self.reject()

    def inserirvenda(self):
        partida = PartidaDialog(self.db, self.gridLanVendas, 'Insert')
        partida.exec_()
        self.calcularSaldoTotal(self.gridLanVendas, self.dblValorTotVendas)

    def inserircompra(self):
        partida = PartidaDialog(self.db, self.gridLanCompras, 'Insert')
        partida.exec_()
        self.calcularSaldoTotal(self.gridLanCompras, self.dblValorTotCompras)

    def editarvenda(self):
        selected_items = self.gridLanVendas.selectedItems()

        if selected_items:
            selected_row = selected_items[0].row()

            codigo = self.gridLanVendas.item(selected_row, 0).text()
            partida = self.gridLanVendas.item(selected_row, 1).text()  # Obtém o nome do item da coluna 1
            quantidade = self.gridLanVendas.item(selected_row, 2).text()  # Obtém a quantidade da coluna 2
            valor = self.gridLanVendas.item(selected_row, 3).text()  # Obtém o valor da coluna 3

            dialog = PartidaDialog(self.db, self.gridLanVendas, 'Edit', codigo)
            dialog.setWindowTitle("Editar Partida")
            dialog.cbxProduto.setCurrentText(partida)
            dialog.edtQntd.setText(str(quantidade))
            dialog.dblValor.setValue(float(valor))

            dialog.exec_()
            self.calcularSaldoTotal(self.gridLanVendas, self.dblValorTotVendas)

    def editarcompra(self):
        selected_items = self.gridLanCompras.selectedItems()

        if selected_items:
            selected_row = selected_items[0].row()

            codigo = self.gridLanVendas.item(selected_row, 0).text()
            partida = self.gridLanCompras.item(selected_row, 1).text()  # Obtém o nome do item da coluna 1
            quantidade = self.gridLanCompras.item(selected_row, 2).text()  # Obtém a quantidade da coluna 2
            valor = self.gridLanCompras.item(selected_row, 3).text()  # Obtém o valor da coluna 3

            dialog = PartidaDialog(self.db, self.gridLanCompras, 'Edit', codigo)
            dialog.setWindowTitle("Editar Partida")
            dialog.cbxProduto.setCurrentText(partida)
            dialog.edtQntd.setText(str(quantidade))
            dialog.dblValor.setValue(float(valor))

            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                # Atualizar os valores na gridLan após a edição
                self.gridLanCompras.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(dialog.cbxProduto.currentText()))
                self.gridLanCompras.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(str(dialog.edtQntd.text())))
                self.gridLanCompras.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(str(dialog.dblValor.value())))
                self.calcularSaldoTotal(self.gridLanCompras, self.dblValorTotCompras)

    def deletarvenda(self):
        selected_items = self.gridLanVendas.selectedItems()

        if selected_items:
            selected_row = selected_items[0].row()

            result = CustomMessageBox("Confirmar Exclusão", "Deseja realmente excluir esta partida?").confirmation.exec_()

            if result == QtWidgets.QMessageBox.Yes:
                self.codigoExcluído.append(int(self.gridLanVendas.item(selected_row, 0).text()))
                # Remover a linha selecionada da grid
                self.gridLanVendas.removeRow(selected_row)

    def deletarcompra(self):
        selected_items = self.gridLanCompras.selectedItems()

        if selected_items:
            selected_row = selected_items[0].row()

            result = CustomMessageBox("Confirmar Exclusão", "Deseja realmente excluir esta partida?").confirmation.exec_()

            if result == QtWidgets.QMessageBox.Yes:
                self.codigoExcluído.append(int(self.gridLanCompras.item(selected_row, 0).text()))
                # Remover a linha selecionada da grid
                self.gridLanCompras.removeRow(selected_row)

    def buscarClientes(self):
        query = "SELECT C.CODCLI, C.DSCCLI FROM TBLCLI C"
        data = self.db.fetch_data(query)

        for index, row in enumerate(data):
            cliente = str(row[1])
            self.cbxCliente.addItem(cliente)
            self.ClienteIndexMap[cliente] = int(row[0])

    def obterCodClienteSelecionado(self):
        cliente_selecionado = self.cbxCliente.currentText()
        if cliente_selecionado in self.ClienteIndexMap:
            return self.ClienteIndexMap[cliente_selecionado]
        return None

    def selecionarClientePorCodigo(self, codigo_cliente):
        for index in range(self.cbxCliente.count()):
            if self.ClienteIndexMap.get(self.cbxCliente.itemText(index)) == codigo_cliente:
                self.cbxCliente.setCurrentIndex(index)
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

    def calcularSaldoTotal(self, grid, dblValor):
        valor = 0
        for row in range(grid.rowCount()):
            valor += float(grid.item(row, 3).text())

        dblValor.setValue(valor)

    def obtemGrupoLan(self):
        query = "SELECT (MAX(L.GRPLAN)+1) FROM TBLLAN L"
        data = self.db.fetch_data(query)
        return data[0][0]