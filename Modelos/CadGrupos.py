# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui\CadGrupo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 149)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fraDescricao = QtWidgets.QFrame(Dialog)
        self.fraDescricao.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraDescricao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraDescricao.setObjectName("fraDescricao")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraDescricao)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDescricao = QtWidgets.QLabel(self.fraDescricao)
        self.lblDescricao.setObjectName("lblDescricao")
        self.verticalLayout.addWidget(self.lblDescricao)
        self.edtDescricao = QtWidgets.QLineEdit(self.fraDescricao)
        self.edtDescricao.setObjectName("edtDescricao")
        self.verticalLayout.addWidget(self.edtDescricao)
        self.verticalLayout_2.addWidget(self.fraDescricao)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.fraBotoes)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblDescricao.setText(_translate("Dialog", "Descrição"))
