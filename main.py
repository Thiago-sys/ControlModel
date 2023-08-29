import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from Modelos.Modelo import Ui_MainWindow
from SubWindows.USubLan import SubWindowLancamentos
from SubWindows.USubEst import SubWindowEstoque
from SubWindows.USubItens import SubWindowItens
from SubWindows.USubGrpItens import SubWindowGrupoItens
from UDataBaseManager import DatabaseManager


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
        subLan = SubWindowLancamentos(self.database_manager)
        sub_window_lancamentos = subLan.get()
        subLan.btnFecharLan.clicked.connect(self.fecharSubWindow)
        self.gridLan = subLan.gridLan
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
        subGrupo = SubWindowGrupoItens()
        sub_window_grupo = subGrupo.get()
        subGrupo.btnFecharGrupo.clicked.connect(self.fecharSubWindow)
        self.mdiArea.addSubWindow(sub_window_grupo)
        sub_window_grupo.showMaximized()

    def fecharSubWindow(self):
        for sub_window in self.mdiArea.subWindowList():
            sub_window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())