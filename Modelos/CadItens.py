# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/CadItens.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 214)
        Dialog.setMinimumSize(QtCore.QSize(402, 214))
        Dialog.setMaximumSize(QtCore.QSize(402, 214))
        Dialog.setWindowIcon(QtGui.QIcon("icons/painel-de-controle.png"))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.fraDescricao = QtWidgets.QFrame(Dialog)
        self.fraDescricao.setMinimumSize(QtCore.QSize(195, 59))
        self.fraDescricao.setMaximumSize(QtCore.QSize(195, 59))
        self.fraDescricao.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraDescricao.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraDescricao.setObjectName("fraDescricao")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraDescricao)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDescricao = QtWidgets.QLabel(self.fraDescricao)
        self.lblDescricao.setObjectName("lblDescricao")
        self.verticalLayout.addWidget(self.lblDescricao)
        self.edtDescricao = QtWidgets.QLineEdit(self.fraDescricao)
        self.edtDescricao.setMaxLength(100)
        self.edtDescricao.setProperty("required", True)
        self.edtDescricao.setObjectName("edtDescricao")
        self.verticalLayout.addWidget(self.edtDescricao)
        self.gridLayout.addWidget(self.fraDescricao, 0, 0, 1, 1)
        self.fraData = QtWidgets.QFrame(Dialog)
        self.fraData.setMinimumSize(QtCore.QSize(101, 59))
        self.fraData.setMaximumSize(QtCore.QSize(101, 59))
        self.fraData.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraData.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraData.setObjectName("fraData")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fraData)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblData = QtWidgets.QLabel(self.fraData)
        self.lblData.setObjectName("lblData")
        self.verticalLayout_2.addWidget(self.lblData)
        self.dteData = QtWidgets.QDateEdit(self.fraData)
        self.dteData.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dteData.setCalendarPopup(True)
        self.dteData.setObjectName("dteData")
        self.verticalLayout_2.addWidget(self.dteData)
        self.gridLayout.addWidget(self.fraData, 0, 1, 1, 1)
        self.fraValor = QtWidgets.QFrame(Dialog)
        self.fraValor.setMinimumSize(QtCore.QSize(90, 59))
        self.fraValor.setMaximumSize(QtCore.QSize(90, 59))
        self.fraValor.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraValor.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraValor.setObjectName("fraValor")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fraValor)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblValor = QtWidgets.QLabel(self.fraValor)
        self.lblValor.setObjectName("lblValor")
        self.verticalLayout_3.addWidget(self.lblValor)
        self.dblValor = QtWidgets.QDoubleSpinBox(self.fraValor)
        self.dblValor.setMinimumSize(QtCore.QSize(0, 0))
        self.dblValor.setFrame(True)
        self.dblValor.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dblValor.setProperty("showGroupSeparator", True)
        self.dblValor.setDecimals(2)
        self.dblValor.setMaximum(999999.99)
        self.dblValor.setProperty("required", True)
        self.dblValor.setObjectName("dblValor")
        self.verticalLayout_3.addWidget(self.dblValor)
        self.gridLayout.addWidget(self.fraValor, 0, 2, 1, 1)
        self.fraFornecedor = QtWidgets.QFrame(Dialog)
        self.fraFornecedor.setMinimumSize(QtCore.QSize(195, 59))
        self.fraFornecedor.setMaximumSize(QtCore.QSize(195, 59))
        self.fraFornecedor.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraFornecedor.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraFornecedor.setObjectName("fraFornecedor")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fraFornecedor)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblFornecedor = QtWidgets.QLabel(self.fraFornecedor)
        self.lblFornecedor.setMinimumSize(QtCore.QSize(0, 0))
        self.lblFornecedor.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lblFornecedor.setObjectName("lblFornecedor")
        self.verticalLayout_5.addWidget(self.lblFornecedor)
        self.cbxFornecedor = QtWidgets.QComboBox(self.fraFornecedor)
        self.cbxFornecedor.setMinimumSize(QtCore.QSize(0, 0))
        self.cbxFornecedor.setMaximumSize(QtCore.QSize(1000, 1000))
        self.cbxFornecedor.setObjectName("cbxFornecedor")
        self.verticalLayout_5.addWidget(self.cbxFornecedor)
        self.gridLayout.addWidget(self.fraFornecedor, 1, 0, 1, 1)
        self.fraBotoes = QtWidgets.QFrame(Dialog)
        self.fraBotoes.setMinimumSize(QtCore.QSize(394, 76))
        self.fraBotoes.setMaximumSize(QtCore.QSize(394, 94))
        self.fraBotoes.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraBotoes.setObjectName("fraBotoes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraBotoes)
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
        self.gridLayout.addWidget(self.fraBotoes, 2, 0, 1, 3)
        self.fraGrupo = QtWidgets.QFrame(Dialog)
        self.fraGrupo.setMinimumSize(QtCore.QSize(195, 59))
        self.fraGrupo.setMaximumSize(QtCore.QSize(195, 59))
        self.fraGrupo.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraGrupo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraGrupo.setObjectName("fraGrupo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fraGrupo)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblGrupo = QtWidgets.QLabel(self.fraGrupo)
        self.lblGrupo.setObjectName("lblGrupo")
        self.verticalLayout_4.addWidget(self.lblGrupo)
        self.cbxGrupo = QtWidgets.QComboBox(self.fraGrupo)
        self.cbxGrupo.setObjectName("cbxGrupo")
        self.verticalLayout_4.addWidget(self.cbxGrupo)
        self.gridLayout.addWidget(self.fraGrupo, 1, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro de Item"))
        self.lblDescricao.setText(_translate("Dialog", "Descrição"))
        self.lblData.setText(_translate("Dialog", "Data da compra"))
        self.lblValor.setText(_translate("Dialog", "Valor"))
        self.dblValor.setPrefix(_translate("Dialog", "R$ "))
        self.lblFornecedor.setText(_translate("Dialog", "Fornecedor"))
        self.lblGrupo.setText(_translate("Dialog", "Grupo do item"))