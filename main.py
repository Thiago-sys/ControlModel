import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt
from Modelos.Modelo import Ui_MainWindow
from SubWindows.USubLan import SubWindowLancamentos
from SubWindows.USubEst import SubWindowEstoque
from SubWindows.USubItens import SubWindowItens
from SubWindows.USubGrpItens import SubWindowGrupoItens
from SubWindows.USubClientes import SubWindowClientes
from SubWindows.USubFornecedores import SubWindowFornecedores
from UDataBaseManager import DatabaseManager


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnLan.clicked.connect(self.mostrarSubLancamentos)
        self.btnEst.clicked.connect(self.mostrarSubEstoque)
        self.btnItens.clicked.connect(self.mostrarSubItens)
        self.btnGrpItens.clicked.connect(self.mostrarSubGrupoItens)
        self.btnClientes.clicked.connect(self.mostrarSubClientes)
        self.btnFornecedores.clicked.connect(self.mostrarSubFornecedores)

        self.showMaximized()

        self.database_manager = DatabaseManager(
            host='localhost',
            user='root',
            password='masterkey',
            database='control'
        )

        self.data = QLabel()
        self.data.setStyleSheet("font-size: 13px; padding-left: 20px;")
        self.statusbar.addWidget(self.data)

        self.update_date_time()  # Update the label initially

        # Set up a timer to update the date and time label
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every 1 second

    def mostrarSubLancamentos(self):
        self.fecharSubWindow()
        subLan = SubWindowLancamentos(self.database_manager)
        sub_window_lancamentos = subLan.get()
        subLan.btnFecharLan.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_lancamentos)
        sub_window_lancamentos.showMaximized()

    def mostrarSubEstoque(self):
        self.fecharSubWindow()
        subEst = SubWindowEstoque(self.database_manager)
        sub_window_estoque = subEst.get()
        subEst.btnFecharEst.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_estoque)
        sub_window_estoque.showMaximized()

    def mostrarSubItens(self):
        self.fecharSubWindow()
        subItens = SubWindowItens(self.database_manager)
        sub_window_itens = subItens.get()
        subItens.btnFecharItens.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_itens)
        sub_window_itens.showMaximized()

    def mostrarSubGrupoItens(self):
        self.fecharSubWindow()
        subGrupo = SubWindowGrupoItens(self.database_manager)
        sub_window_grupo = subGrupo.get()
        subGrupo.btnFecharGrupo.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_grupo)
        sub_window_grupo.showMaximized()

    def mostrarSubClientes(self):
        self.fecharSubWindow()
        subClientes = SubWindowClientes(self.database_manager)
        sub_window_clientes = subClientes.get()
        subClientes.btnFecharClientes.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_clientes)
        sub_window_clientes.showMaximized()

    def mostrarSubFornecedores(self):
        self.fecharSubWindow()
        subFornecedores = SubWindowFornecedores(self.database_manager)
        sub_window_fornecedores = subFornecedores.get()
        subFornecedores.btnFecharFornecedores.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_fornecedores)
        sub_window_fornecedores.showMaximized()

    def fecharSubWindow(self):
        for sub_window in self.mdiArea.subWindowList():
            sub_window.close()

    def update_date_time(self):
        current_date_time = QDateTime.currentDateTime()
        formatted_date_time = current_date_time.toString("dd/MM/yyyy hh:mm:ss")
        self.data.setText("Data: " + formatted_date_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())