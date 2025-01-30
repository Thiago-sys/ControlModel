# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/MovEstoque.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(269, 345)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        Dialog.setWindowIcon(QtGui.QIcon("icons/painel-de-controle.png"))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(261, 265))
        self.tabWidget.setMaximumSize(QtCore.QSize(261, 265))
        self.tabWidget.setObjectName("tabWidget")
        self.tabEntrada = QtWidgets.QWidget()
        self.tabEntrada.setObjectName("tabEntrada")
        self.gridLayout = QtWidgets.QGridLayout(self.tabEntrada)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.fraDataEntrada = QtWidgets.QFrame(self.tabEntrada)
        self.fraDataEntrada.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraDataEntrada.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraDataEntrada.setObjectName("fraDataEntrada")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fraDataEntrada)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblDataEntrada = QtWidgets.QLabel(self.fraDataEntrada)
        self.lblDataEntrada.setObjectName("lblDataEntrada")
        self.verticalLayout_6.addWidget(self.lblDataEntrada)
        self.dteDataEntrada = QtWidgets.QDateEdit(self.fraDataEntrada)
        self.dteDataEntrada.setObjectName("dteDataEntrada")
        self.verticalLayout_6.addWidget(self.dteDataEntrada)
        self.gridLayout.addWidget(self.fraDataEntrada, 0, 0, 1, 1)
        self.fraFornecedor = QtWidgets.QFrame(self.tabEntrada)
        self.fraFornecedor.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraFornecedor.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraFornecedor.setObjectName("fraFornecedor")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fraFornecedor)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblFornecedor = QtWidgets.QLabel(self.fraFornecedor)
        self.lblFornecedor.setObjectName("lblFornecedor")
        self.verticalLayout_7.addWidget(self.lblFornecedor)
        self.cbxFornecedor = QtWidgets.QComboBox(self.fraFornecedor)
        self.cbxFornecedor.setObjectName("cbxFornecedor")
        self.verticalLayout_7.addWidget(self.cbxFornecedor)
        self.gridLayout.addWidget(self.fraFornecedor, 0, 1, 1, 2)
        self.fraItemEntrada = QtWidgets.QFrame(self.tabEntrada)
        self.fraItemEntrada.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraItemEntrada.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraItemEntrada.setObjectName("fraItemEntrada")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fraItemEntrada)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblItemEntrada = QtWidgets.QLabel(self.fraItemEntrada)
        self.lblItemEntrada.setObjectName("lblItemEntrada")
        self.verticalLayout_2.addWidget(self.lblItemEntrada)
        self.cbxItemEntrada = QtWidgets.QComboBox(self.fraItemEntrada)
        self.cbxItemEntrada.setMinimumSize(QtCore.QSize(120, 20))
        self.cbxItemEntrada.setObjectName("cbxItemEntrada")
        self.verticalLayout_2.addWidget(self.cbxItemEntrada)
        self.gridLayout.addWidget(self.fraItemEntrada, 1, 0, 1, 2)
        self.fraQntdEntrada = QtWidgets.QFrame(self.tabEntrada)
        self.fraQntdEntrada.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraQntdEntrada.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraQntdEntrada.setObjectName("fraQntdEntrada")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fraQntdEntrada)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblQntdEntrada = QtWidgets.QLabel(self.fraQntdEntrada)
        self.lblQntdEntrada.setObjectName("lblQntdEntrada")
        self.verticalLayout_3.addWidget(self.lblQntdEntrada)
        self.edtQntdEntrada = QtWidgets.QLineEdit(self.fraQntdEntrada)
        self.edtQntdEntrada.setMinimumSize(QtCore.QSize(70, 20))
        self.edtQntdEntrada.setObjectName("edtQntdEntrada")
        self.verticalLayout_3.addWidget(self.edtQntdEntrada)
        self.gridLayout.addWidget(self.fraQntdEntrada, 1, 2, 1, 1)
        self.fraCompEntrada = QtWidgets.QFrame(self.tabEntrada)
        self.fraCompEntrada.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraCompEntrada.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraCompEntrada.setLineWidth(1)
        self.fraCompEntrada.setObjectName("fraCompEntrada")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fraCompEntrada)
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lblCompEntrada = QtWidgets.QLabel(self.fraCompEntrada)
        self.lblCompEntrada.setObjectName("lblCompEntrada")
        self.verticalLayout_10.addWidget(self.lblCompEntrada)
        self.edtCompEntrada = QtWidgets.QTextEdit(self.fraCompEntrada)
        self.edtCompEntrada.setObjectName("edtCompEntrada")
        self.verticalLayout_10.addWidget(self.edtCompEntrada)
        self.gridLayout.addWidget(self.fraCompEntrada, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tabEntrada, "")
        self.tabSaida = QtWidgets.QWidget()
        self.tabSaida.setObjectName("tabSaida")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabSaida)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fraDataSaida = QtWidgets.QFrame(self.tabSaida)
        self.fraDataSaida.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraDataSaida.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraDataSaida.setObjectName("fraDataSaida")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fraDataSaida)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lblDataSaida = QtWidgets.QLabel(self.fraDataSaida)
        self.lblDataSaida.setObjectName("lblDataSaida")
        self.verticalLayout_9.addWidget(self.lblDataSaida)
        self.dteDataSaida = QtWidgets.QDateEdit(self.fraDataSaida)
        self.dteDataSaida.setObjectName("dteDataSaida")
        self.verticalLayout_9.addWidget(self.dteDataSaida)
        self.gridLayout_2.addWidget(self.fraDataSaida, 0, 0, 1, 1)
        self.fraCliente = QtWidgets.QFrame(self.tabSaida)
        self.fraCliente.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraCliente.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraCliente.setObjectName("fraCliente")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fraCliente)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblCliente = QtWidgets.QLabel(self.fraCliente)
        self.lblCliente.setObjectName("lblCliente")
        self.verticalLayout_8.addWidget(self.lblCliente)
        self.cbxCliente = QtWidgets.QComboBox(self.fraCliente)
        self.cbxCliente.setObjectName("cbxCliente")
        self.verticalLayout_8.addWidget(self.cbxCliente)
        self.gridLayout_2.addWidget(self.fraCliente, 0, 1, 1, 2)
        self.fraItemSaida = QtWidgets.QFrame(self.tabSaida)
        self.fraItemSaida.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraItemSaida.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraItemSaida.setObjectName("fraItemSaida")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fraItemSaida)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblItemSaida = QtWidgets.QLabel(self.fraItemSaida)
        self.lblItemSaida.setObjectName("lblItemSaida")
        self.verticalLayout_5.addWidget(self.lblItemSaida)
        self.cbxItemSaida = QtWidgets.QComboBox(self.fraItemSaida)
        self.cbxItemSaida.setMinimumSize(QtCore.QSize(120, 20))
        self.cbxItemSaida.setObjectName("cbxItemSaida")
        self.verticalLayout_5.addWidget(self.cbxItemSaida)
        self.gridLayout_2.addWidget(self.fraItemSaida, 1, 0, 1, 2)
        self.fraQntdSaida = QtWidgets.QFrame(self.tabSaida)
        self.fraQntdSaida.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraQntdSaida.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraQntdSaida.setObjectName("fraQntdSaida")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fraQntdSaida)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblQntdSaida = QtWidgets.QLabel(self.fraQntdSaida)
        self.lblQntdSaida.setObjectName("lblQntdSaida")
        self.verticalLayout_4.addWidget(self.lblQntdSaida)
        self.edtQntdSaida = QtWidgets.QLineEdit(self.fraQntdSaida)
        self.edtQntdSaida.setMinimumSize(QtCore.QSize(70, 20))
        self.edtQntdSaida.setObjectName("edtQntdSaida")
        self.verticalLayout_4.addWidget(self.edtQntdSaida)
        self.gridLayout_2.addWidget(self.fraQntdSaida, 1, 2, 1, 1)
        self.fraCompSaida = QtWidgets.QFrame(self.tabSaida)
        self.fraCompSaida.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraCompSaida.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraCompSaida.setObjectName("fraCompSaida")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.fraCompSaida)
        self.verticalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lblCompSaida = QtWidgets.QLabel(self.fraCompSaida)
        self.lblCompSaida.setObjectName("lblCompSaida")
        self.verticalLayout_11.addWidget(self.lblCompSaida)
        self.edtCompSaida = QtWidgets.QTextEdit(self.fraCompSaida)
        self.edtCompSaida.setObjectName("edtCompSaida")
        self.verticalLayout_11.addWidget(self.edtCompSaida)
        self.gridLayout_2.addWidget(self.fraCompSaida, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tabSaida, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.fraBotoes = QtWidgets.QFrame(Dialog)
        self.fraBotoes.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraBotoes.setObjectName("fraBotoes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraBotoes)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnGravar = QtWidgets.QPushButton(self.fraBotoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGravar.sizePolicy().hasHeightForWidth())
        self.btnGravar.setSizePolicy(sizePolicy)
        self.btnGravar.setStyleSheet("background:transparent\n"
"")
        self.btnGravar.setText("")
        self.btnGravar.setIcon(QtGui.QIcon("icons/2x/save.png"))
        self.btnGravar.setIconSize(QtCore.QSize(48, 48))
        self.btnGravar.setObjectName("btnGravar")
        self.horizontalLayout.addWidget(self.btnGravar)
        self.btnCancelar = QtWidgets.QPushButton(self.fraBotoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setStyleSheet("background:transparent\n"
"")
        self.btnCancelar.setText("")
        self.btnCancelar.setIcon(QtGui.QIcon("icons/2x/cancel.png"))
        self.btnCancelar.setIconSize(QtCore.QSize(48, 48))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.fraBotoes)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Movimentação de Estoque"))
        self.lblDataEntrada.setText(_translate("Dialog", "Data:"))
        self.lblFornecedor.setText(_translate("Dialog", "Fornecedor"))
        self.lblItemEntrada.setText(_translate("Dialog", "Item"))
        self.lblQntdEntrada.setText(_translate("Dialog", "Quantidade"))
        self.lblCompEntrada.setText(_translate("Dialog", "Complemento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEntrada), _translate("Dialog", "Entrada"))
        self.lblDataSaida.setText(_translate("Dialog", "Data:"))
        self.lblCliente.setText(_translate("Dialog", "Fornecedor"))
        self.lblItemSaida.setText(_translate("Dialog", "Item"))
        self.lblQntdSaida.setText(_translate("Dialog", "Quantidade"))
        self.lblCompSaida.setText(_translate("Dialog", "Complemento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSaida), _translate("Dialog", "Saída"))
