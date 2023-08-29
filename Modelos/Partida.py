# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/Partida.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 196)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fraQntd = QtWidgets.QFrame(Dialog)
        self.fraQntd.setMaximumSize(QtCore.QSize(140, 140))
        self.fraQntd.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraQntd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraQntd.setObjectName("fraQntd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fraQntd)
        self.verticalLayout_2.setContentsMargins(9, 2, 9, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblQntd = QtWidgets.QLabel(self.fraQntd)
        self.lblQntd.setObjectName("lblQntd")
        self.verticalLayout_2.addWidget(self.lblQntd)
        self.edtQntd = QtWidgets.QLineEdit(self.fraQntd)
        self.edtQntd.setObjectName("edtQntd")
        self.verticalLayout_2.addWidget(self.edtQntd)
        self.gridLayout.addWidget(self.fraQntd, 1, 0, 1, 1)
        self.fraVlr = QtWidgets.QFrame(Dialog)
        self.fraVlr.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraVlr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraVlr.setObjectName("fraVlr")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fraVlr)
        self.verticalLayout_3.setContentsMargins(9, 2, 9, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblVlr = QtWidgets.QLabel(self.fraVlr)
        self.lblVlr.setObjectName("lblVlr")
        self.verticalLayout_3.addWidget(self.lblVlr)
        self.dblValor = QtWidgets.QDoubleSpinBox(self.fraVlr)
        self.dblValor.setMinimumSize(QtCore.QSize(120, 20))
        self.dblValor.setFrame(True)
        self.dblValor.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dblValor.setProperty("showGroupSeparator", True)
        self.dblValor.setDecimals(2)
        self.dblValor.setMaximum(999999.99)
        self.dblValor.setObjectName("dblValor")
        self.verticalLayout_3.addWidget(self.dblValor)
        self.gridLayout.addWidget(self.fraVlr, 1, 1, 1, 1)
        self.fraBotoes = QtWidgets.QFrame(Dialog)
        self.fraBotoes.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraBotoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBotoes.setObjectName("fraBotoes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraBotoes)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/2x/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGravar.setIcon(icon)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/2x/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setIconSize(QtCore.QSize(48, 48))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.fraBotoes, 2, 0, 1, 2)
        self.fraProduto = QtWidgets.QFrame(Dialog)
        self.fraProduto.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraProduto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraProduto.setObjectName("fraProduto")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraProduto)
        self.verticalLayout.setContentsMargins(9, 2, 9, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblProduto = QtWidgets.QLabel(self.fraProduto)
        self.lblProduto.setObjectName("lblProduto")
        self.verticalLayout.addWidget(self.lblProduto)
        self.cbxProduto = QtWidgets.QComboBox(self.fraProduto)
        self.cbxProduto.setObjectName("cbxProduto")
        self.verticalLayout.addWidget(self.cbxProduto)
        self.gridLayout.addWidget(self.fraProduto, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblQntd.setText(_translate("Dialog", "Quantidade"))
        self.lblVlr.setText(_translate("Dialog", "Valor"))
        self.dblValor.setPrefix(_translate("Dialog", "R$ "))
        self.lblProduto.setText(_translate("Dialog", "Produto"))
