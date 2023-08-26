import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from Modelos.Modelo import Ui_MainWindow
from SubWindows.USubLan import SubWindowLancamentos
from SubWindows.USubEst import SubWindowEstoque
from SubWindows.USubItens import SubWindowItens
from SubWindows.USubGrpItens import SubWindowGrupoItens
from UCadLanDialog import CadLanDialog
from UDataBaseManager import DatabaseManager
from UCustomMessageBox import CustomMessageBox
from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnLan.setIcon(QIcon("icons/2x/btnLan.png"))
        self.btnLan.clicked.connect(self.mostrarSubLancamentos)

        self.btnEst.setIcon(QIcon("icons/2x/btnEst.png"))
        self.btnEst.clicked.connect(self.mostrarSubEstoque)

        self.btnItens.setIcon(QIcon("icons/2x/btnItens.png"))
        self.btnItens.clicked.connect(self.mostrarSubItens)

        self.btnGrpItens.setIcon(QIcon("icons/2x/btnGrpItens.png"))
        self.btnGrpItens.clicked.connect(self.mostrarSubGrupoItens)

        self.btnInserirLan.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirEst.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirItens.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirGrupo.setIcon(QIcon("icons/2x/insert.png"))

        self.btnEditarLan.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarEst.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarItens.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarGrupo.setIcon(QIcon("icons/2x/edit.png"))

        self.btnExcluirLan.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirEst.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirItens.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirGrupo.setIcon(QIcon("icons/2x/delete.png"))

        self.btnFecharLan.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharEst.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharItens.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharGrupo.setIcon(QIcon("icons/2x/close.png"))

        self.showMaximized()

        self.database_manager = DatabaseManager(
            host='localhost',
            user='root',
            password='masterkey',
            database='control'
        )

    def mostrarSubLancamentos(self):
        self.fecharSubWindow()
        subLan = SubWindowLancamentos()
        sub_window_lancamentos = subLan.get()
        subLan.btnFecharLan.clicked.connect(self.fecharSubWindow)
        subLan.btnInserirLan.clicked.connect(self.inserirLan)
        subLan.btnEditarLan.clicked.connect(lambda event: self.editarLan(subLan.gridLan))
        subLan.btnExcluirLan.clicked.connect(lambda event: self.excluirLan(subLan.gridLan))

        self.gridLan = subLan.gridLan

        self.buscarlancamentos(subLan.gridLan)
        subLan.gridLan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.mdiArea.addSubWindow(sub_window_lancamentos)
        sub_window_lancamentos.showMaximized()

    def mostrarSubEstoque(self):
        self.fecharSubWindow()
        subEst = SubWindowEstoque()
        sub_window_estoque = subEst.get()
        subEst.btnFecharEst.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_estoque)
        sub_window_estoque.showMaximized()

    def mostrarSubItens(self):
        self.fecharSubWindow()
        subItens = SubWindowItens()
        sub_window_itens = subItens.get()
        subItens.btnFecharItens.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_itens)
        sub_window_itens.showMaximized()

    def mostrarSubGrupoItens(self):
        self.fecharSubWindow()
        subGrupo = SubWindowGrupoItens()
        sub_window_grupo = subGrupo.get()
        subGrupo.btnFecharGrupo.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_grupo)
        sub_window_grupo.showMaximized()

    def fecharSubWindow(self):
        for sub_window in self.mdiArea.subWindowList():
            sub_window.close()

    def inserirLan(self):
        cadlan = CadLanDialog(self.database_manager, "Insert")
        cadlan.exec_()

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

            cadlan = CadLanDialog(self.database_manager, "Edit", codigo, grupo)
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
                    data_itens = self.database_manager.fetch_data(query_itens)

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
                    data_itens = self.database_manager.fetch_data(query_itens)

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

                MessageBox = CustomMessageBox("Confirmar Exclusão", "Deseja excluir esse grupo de lançamento? \n"
                                              "Ao realizar essa ação todos os lançamentos do grupo serão excluídos")
                confirmation = MessageBox.confirmation
                result = confirmation.exec_()

                if result == QtWidgets.QMessageBox.Yes:
                    codigo = int(gridLan.item(selected_row, 12).text())

                    delete_query = f"DELETE FROM TBLLAN L WHERE L.GRPLAN = {codigo}"
                    self.database_manager.execute_query(delete_query)

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
        data = self.database_manager.fetch_data(query)

        # Preencher a gridLan com os dados recuperados
        gridLan.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                if str(value) == 'None':
                    gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(''))
                else:
                    if col_num == 1:
                        data_objeto = datetime.strptime(str(value), "%Y-%m-%d")
                        data_formatada = data_objeto.strftime("%d/%m/%Y")
                        gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(data_formatada))
                    elif col_num == 3:
                        gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem('R$ {:,.2f}'.format(value).replace(',', '.').replace('.', ',')))
                    else:
                        gridLan.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))

    def buscarCodigos(self, data, grupo):
        query = "SELECT L.CODLAN FROM TBLLAN L WHERE L.DTALAN = %s AND L.GRPLAN = %s"
        cods = self.database_manager.fetch_data(query, (data, grupo))

        cods_list = [cod[0] for cod in cods]
        return cods_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())