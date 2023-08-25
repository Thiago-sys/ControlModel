from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class SubWindowEstoque(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.subEst = QtWidgets.QWidget()
        self.subEst.setObjectName("subEst")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.subEst)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridEst = QtWidgets.QTableWidget(self.subEst)
        self.gridEst.setObjectName("gridEst")
        self.gridEst.setColumnCount(3)
        self.gridEst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridEst.setHorizontalHeaderItem(2, item)
        self.gridEst.horizontalHeader().setMinimumSectionSize(50)
        self.verticalLayout_3.addWidget(self.gridEst)
        self.fraBotoesEst = QtWidgets.QFrame(self.subEst)
        self.fraBotoesEst.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBotoesEst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoesEst.setObjectName("fraBotoesEst")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraBotoesEst)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnInserirEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnInserirEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setMaximumSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnInserirEst.setText("")
        self.btnInserirEst.setIcon(QIcon("icons/2x/insert.png"))
        self.btnInserirEst.setIconSize(QtCore.QSize(48, 48))
        self.btnInserirEst.setObjectName("btnInserirEst")
        self.horizontalLayout_2.addWidget(self.btnInserirEst)
        self.btnEditarEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnEditarEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnEditarEst.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnEditarEst.setText("")
        self.btnEditarEst.setIcon(QIcon("icons/2x/edit.png"))
        self.btnEditarEst.setIconSize(QtCore.QSize(36, 36))
        self.btnEditarEst.setObjectName("btnEditarEst")
        self.horizontalLayout_2.addWidget(self.btnEditarEst)
        self.btnExcluirEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnExcluirEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnExcluirEst.setStyleSheet("background-color: transparent; \n"
                                         "border: none;")
        self.btnExcluirEst.setText("")
        self.btnExcluirEst.setIcon(QIcon("icons/2x/delete.png"))
        self.btnExcluirEst.setIconSize(QtCore.QSize(36, 36))
        self.btnExcluirEst.setObjectName("btnExcluirEst")
        self.horizontalLayout_2.addWidget(self.btnExcluirEst)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnFecharEst = QtWidgets.QPushButton(self.fraBotoesEst)
        self.btnFecharEst.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFecharEst.setMaximumSize(QtCore.QSize(48, 48))
        self.btnFecharEst.setStyleSheet("background-color: transparent; \n"
                                        "border: none;")
        self.btnFecharEst.setText("")
        self.btnFecharEst.setIcon(QIcon("icons/2x/close.png"))
        self.btnFecharEst.setIconSize(QtCore.QSize(40, 40))
        self.btnFecharEst.setObjectName("btnFecharEst")
        self.horizontalLayout_2.addWidget(self.btnFecharEst)
        self.verticalLayout_3.addWidget(self.fraBotoesEst)

        _translate = QtCore.QCoreApplication.translate
        self.subEst.setWindowTitle(_translate("MainWindow", "Estoque"))
        item = self.gridEst.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.gridEst.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.gridEst.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantidade"))

    def get(self):
        return self.subEst
