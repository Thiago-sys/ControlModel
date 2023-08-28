from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from Modelos.MovEstoque import Ui_Dialog
from UDataBaseManager import DatabaseManager
from UCustomMessageBox import CustomMessageBox


class MovEstoqueDialog(QDialog, Ui_Dialog):
    def __init__(self, db:DatabaseManager, state: str, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.btnGravar.clicked.connect(self.gravar)
        self.btnCancelar.clicked.connect(self.cancelar)

        self.ClienteIndexMap = {}
        self.FornecedorIndexMap = {}
        self.itemIndexMap = {}

        self.buscarClientes()
        self.buscarFornecedores()
        self.buscarItens()

    def gravar(self):
        try:
            if self.state == 'Insert':
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                result = CustomMessageBox("Confirmar Gravação",
                                          "Deseja realmente gravar essa movimentação?").confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:
                    if self.tabWidget.currentIndex() == 0: # Entrada
                        # Coletar dados da interface do usuário
                        data = self.dteDataEntrada.date().toPyDate()
                        natureza = 'C'
                        codFornecedor = int(self.obterCodFornecedorSelecionado())
                        complemento = self.edtCompEntrada.toPlainText()
                        codItem = self.obterCodItemSelecionado('C')
                        qntd = self.edtQntdEntrada.text()

                        # Preparar o SQL para inserção de uma movimentação
                        insert_query = "INSERT INTO TBLMOVEST (DTALAN, NATLAN, CODITE, QTD, CODFOR, COMLAN) " \
                                       "               VALUES (%s, %s, %s, %s, %s, %s)"

                        values = (data, natureza, codItem, qntd, codFornecedor, complemento)

                        # Executar a consulta SQL de inserção
                        self.db.execute_query(insert_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Movimentação gravada com sucesso.").information.exec_()
                        self.accept()
                    else:
                        # Coletar dados da interface do usuário
                        data = self.dteDataSaida.date().toPyDate()
                        natureza = 'V'
                        codCliente = int(self.obterCodClienteSelecionado())
                        complemento = self.edtCompSaida.toPlainText()
                        codItem = self.obterCodItemSelecionado('V')
                        qntd = self.edtQntdEntrada.text()

                        # Preparar a consulta SQL para inserção de um lançamento
                        insert_query = "INSERT INTO TBLMOVEST (DTALAN, NATLAN, CODITE, QTD, CODCLI, COMLAN) " \
                                       "               VALUES (%s, %s, %s, %s, %s, %s)"

                        # Preparar os valores para a inserção na TBLLAN
                        values = (data, natureza, codItem, qntd, codCliente, complemento)

                        # Executar a consulta SQL de inserção
                        self.db.execute_query(insert_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        CustomMessageBox("Sucesso", "Movimentação gravada com sucesso.").information.exec_()
                        self.accept()
            else:
                if self.db.connection.in_transaction:
                    self.db.connection.rollback()
                self.db.connection.start_transaction()

                confirmation = CustomMessageBox("Confirmar Gravação",
                                                "Deseja realmente gravar essa movimentação?").confirmation
                result = confirmation.exec_()
                if result == QtWidgets.QMessageBox.Yes:

                    if self.tabWidget.currentIndex() == 0:
                        # Coletar dados da interface do usuário
                        data = self.dteDataEntrada.date().toPyDate()
                        natureza = 'C'
                        codFornecedor = int(self.obterCodFornecedorSelecionado())
                        complemento = self.edtCompEntrada.toPlainText()
                        codItem = self.obterCodItemSelecionado('C')
                        qntd = self.edtQntdEntrada.text()

                        # Preparar a consulta SQL para inserção de um lançamento
                        update_query = "UPDATE TBLMOVEST SET NATLAN = %s, CODITE = %s, QTDITE = %s, CODFOR = %s, " \
                                       "COMLAN = %s WHERE CODMOVEST = %s AND DTAMOV = %s"

                        # Preparar os valores para a inserção na TBLLAN
                        values = (natureza, codItem, qntd, codFornecedor, complemento, self.codigo, data)

                        self.db.execute_query(update_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Movimentação gravada com sucesso.")
                        self.accept()
                    else:
                        # Coletar dados da interface do usuário
                        data = self.dteDataSaida.date().toPyDate()
                        natureza = 'V'
                        codCliente = int(self.obterCodClienteSelecionado())
                        complemento = self.edtCompSaida.toPlainText()
                        codItem = self.obterCodItemSelecionado('V')
                        qntd = self.edtQntdSaida.text()

                        # Preparar a consulta SQL para inserção de um lançamento
                        update_query = "UPDATE TBLMOVEST SET NATLAN = %s, CODITE = %s, QTDITE = %s, CODCLI = %s, " \
                                       "COMLAN = %s WHERE CODMOVEST = %s AND DTAMOV = %s"

                        # Preparar os valores para a inserção na TBLLAN
                        values = (natureza, codItem, qntd, codCliente, complemento, self.codigo, data)

                        self.db.execute_query(update_query, values)

                        self.db.connection.commit()
                        # Exibir mensagem de sucesso
                        QtWidgets.QMessageBox.information(self, "Sucesso", "Movimentação gravada com sucesso.")
                        self.accept()

        except Exception as e:
            self.db.connection.rollback()  # Desfaz as alterações em caso de erro
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao gravar lançamento(s): {str(e)}")
            self.reject()

    def cancelar(self):
        self.reject()

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

    def buscarItens(self):
        query = "SELECT I.CODITE, I.DSCITE FROM TBLITE I"
        data = self.db.fetch_data(query)

        for index, row in enumerate(data):
            item = str(row[1])
            self.cbxItemSaida.addItem(item)
            self.cbxItemEntrada.addItem(item)
            self.itemIndexMap[item] = int(row[0])

    def obterCodItemSelecionado(self, nat):
        if nat == 'V':
            item_selecionado = self.cbxItemSaida.currentText()
            if item_selecionado in self.itemIndexMap:
                return self.itemIndexMap[item_selecionado]
            return None
        else:
            item_selecionado = self.cbxItemEntrada.currentText()
            if item_selecionado in self.itemIndexMap:
                return self.itemIndexMap[item_selecionado]
            return None

    def selecionarItemPorCodigo(self, codigo_item, nat):
        if nat == 'V':
            for index in range(self.cbxItemSaida.count()):
                if self.itemIndexMap.get(self.cbxItemSaida.itemText(index)) == codigo_item:
                    self.cbxItemSaida.setCurrentIndex(index)
                    break
        else:
            for index in range(self.cbxItemEntrada.count()):
                if self.itemIndexMap.get(self.cbxItemEntrada.itemText(index)) == codigo_item:
                    self.cbxItemEntrada.setCurrentIndex(index)
                    break