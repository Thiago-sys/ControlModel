from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class SubWindowGrupoItens(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.subGrupo = QtWidgets.QWidget()
        self.subGrupo.setAutoFillBackground(False)
        self.subGrupo.setObjectName("subGrupo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.subGrupo)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridGrupoItens = QtWidgets.QTableWidget(self.subGrupo)
        self.gridGrupoItens.setObjectName("gridGrupoItens")
        self.gridGrupoItens.setColumnCount(2)
        self.gridGrupoItens.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridGrupoItens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridGrupoItens.setHorizontalHeaderItem(1, item)
        self.gridGrupoItens.horizontalHeader().setDefaultSectionSize(120)
        self.gridGrupoItens.horizontalHeader().setMinimumSectionSize(100)
        self.verticalLayout_5.addWidget(self.gridGrupoItens)
        self.fraBotoesGrupo = QtWidgets.QFrame(self.subGrupo)
        self.fraBotoesGrupo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesGrupo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesGrupo.setObjectName("fraBotoesGrupo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fraBotoesGrupo)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnInserirGrupo = QtWidgets.QPushButton(self.fraBotoesGrupo)
        self.btnInserirGrupo.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirGrupo.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirGrupo.setStyleSheet("background-color: transparent; \n"
                                           "border: none;")
        self.btnInserirGrupo.setText("")
        self.btnInserirGrupo.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirGrupo.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirGrupo.setObjectName("btnInserirGrupo")
        self.horizontalLayout_5.addWidget(self.btnInserirGrupo)
        self.btnEditarGrupo = QtWidgets.QPushButton(self.fraBotoesGrupo)
        self.btnEditarGrupo.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarGrupo.setStyleSheet("background-color: transparent; \n"
                                          "border: none;")
        self.btnEditarGrupo.setText("")
        self.btnEditarGrupo.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarGrupo.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarGrupo.setObjectName("btnEditarGrupo")
        self.horizontalLayout_5.addWidget(self.btnEditarGrupo)
        self.btnExcluirGrupo = QtWidgets.QPushButton(self.fraBotoesGrupo)
        self.btnExcluirGrupo.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirGrupo.setStyleSheet("background-color: transparent; \n"
                                           "border: none;")
        self.btnExcluirGrupo.setText("")
        self.btnExcluirGrupo.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirGrupo.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirGrupo.setObjectName("btnExcluirGrupo")
        self.horizontalLayout_5.addWidget(self.btnExcluirGrupo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.btnFecharGrupo = QtWidgets.QPushButton(self.fraBotoesGrupo)
        self.btnFecharGrupo.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharGrupo.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharGrupo.setStyleSheet("background-color: transparent; \n"
                                          "border: none;")
        self.btnFecharGrupo.setText("")
        self.btnFecharGrupo.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharGrupo.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharGrupo.setObjectName("btnFecharGrupo")
        self.horizontalLayout_5.addWidget(self.btnFecharGrupo)
        self.verticalLayout_5.addWidget(self.fraBotoesGrupo)

        _translate = QtCore.QCoreApplication.translate
        self.subGrupo.setWindowTitle(_translate("MainWindow", "Grupo de itens"))
        item = self.gridGrupoItens.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridGrupoItens.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descrição"))

    def get(self):
        return self.subGrupo
