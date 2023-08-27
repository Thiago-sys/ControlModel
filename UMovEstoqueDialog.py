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

        self.btnGravar.clicked.connect()
        self.btnCancelar.clicked.connect()

        self.ClienteIndexMap = {}
        self.FornecedorIndexMap = {}
        self.itemIndexMap = {}

        self.buscarClientes()
        self.buscarFornecedores()
        self.buscarItens()

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