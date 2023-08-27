from PyQt5.QtWidgets import QDialog
from Modelos.MovEstoque import Ui_Dialog
from UDataBaseManager import DatabaseManager


class MovEstoqueDialog(QDialog, Ui_Dialog):
    def __init__(self, db:DatabaseManager, state: str, codigo=None):
        super().__init__()
        self.setupUi(self)

        self.db = db
        self.state = state
        self.codigo = codigo

        self.ClienteIndexMap = {}
        self.FornecedorIndexMap = {}

        self.buscarClientes()
        self.buscarFornecedores()

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
