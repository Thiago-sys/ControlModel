# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/CadCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 354)
        Dialog.setMinimumSize(QtCore.QSize(336, 354))
        Dialog.setMaximumSize(QtCore.QSize(336, 354))
        Dialog.setWindowIcon(QtGui.QIcon("icons/painel-de-controle.png"))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fraNome = QtWidgets.QFrame(Dialog)
        self.fraNome.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraNome.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraNome.setObjectName("fraNome")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraNome)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblNome = QtWidgets.QLabel(self.fraNome)
        self.lblNome.setObjectName("lblNome")
        self.verticalLayout.addWidget(self.lblNome)
        self.edtNome = QtWidgets.QLineEdit(self.fraNome)
        self.edtNome.setMaxLength(200)
        self.edtNome.setProperty("Required", True)
        self.edtNome.setObjectName("edtNome")
        self.verticalLayout.addWidget(self.edtNome)
        self.gridLayout.addWidget(self.fraNome, 0, 0, 1, 2)
        self.fraCpf = QtWidgets.QFrame(Dialog)
        self.fraCpf.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraCpf.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraCpf.setObjectName("fraCpf")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fraCpf)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblCpf = QtWidgets.QLabel(self.fraCpf)
        self.lblCpf.setObjectName("lblCpf")
        self.verticalLayout_2.addWidget(self.lblCpf)
        self.edtCpf = QtWidgets.QLineEdit(self.fraCpf)
        self.edtCpf.setProperty("required", True)
        self.edtCpf.setObjectName("edtCpf")
        self.verticalLayout_2.addWidget(self.edtCpf)
        self.gridLayout.addWidget(self.fraCpf, 1, 0, 1, 1)
        self.fraTelefone = QtWidgets.QFrame(Dialog)
        self.fraTelefone.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraTelefone.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraTelefone.setObjectName("fraTelefone")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fraTelefone)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTelefone = QtWidgets.QLabel(self.fraTelefone)
        self.lblTelefone.setObjectName("lblTelefone")
        self.verticalLayout_3.addWidget(self.lblTelefone)
        self.edtTelefone = QtWidgets.QLineEdit(self.fraTelefone)
        self.edtTelefone.setObjectName("edtTelefone")
        self.verticalLayout_3.addWidget(self.edtTelefone)
        self.gridLayout.addWidget(self.fraTelefone, 1, 1, 1, 1)
        self.fraEmail = QtWidgets.QFrame(Dialog)
        self.fraEmail.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraEmail.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraEmail.setObjectName("fraEmail")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fraEmail)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblEmail = QtWidgets.QLabel(self.fraEmail)
        self.lblEmail.setObjectName("lblEmail")
        self.verticalLayout_4.addWidget(self.lblEmail)
        self.edtEmail = QtWidgets.QLineEdit(self.fraEmail)
        self.edtEmail.setMaxLength(200)
        self.edtEmail.setObjectName("edtEmail")
        self.verticalLayout_4.addWidget(self.edtEmail)
        self.gridLayout.addWidget(self.fraEmail, 2, 0, 1, 2)
        self.fraEnd = QtWidgets.QFrame(Dialog)
        self.fraEnd.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.fraEnd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraEnd.setObjectName("fraEnd")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fraEnd)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblEnd = QtWidgets.QLabel(self.fraEnd)
        self.lblEnd.setObjectName("lblEnd")
        self.verticalLayout_5.addWidget(self.lblEnd)
        self.edtEnd = QtWidgets.QLineEdit(self.fraEnd)
        self.edtEnd.setMaxLength(200)
        self.edtEnd.setObjectName("edtEnd")
        self.verticalLayout_5.addWidget(self.edtEnd)
        self.gridLayout.addWidget(self.fraEnd, 3, 0, 1, 2)
        self.fraBotoes = QtWidgets.QFrame(Dialog)
        self.fraBotoes.setMinimumSize(QtCore.QSize(0, 0))
        self.fraBotoes.setMaximumSize(QtCore.QSize(10000, 10000))
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
        self.gridLayout.addWidget(self.fraBotoes, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro de Cliente"))
        self.lblNome.setText(_translate("Dialog", "Nome"))
        self.lblCpf.setText(_translate("Dialog", "CPF"))
        self.edtCpf.setInputMask(_translate("Dialog", "999.999.999-99"))
        self.edtCpf.setText(_translate("Dialog", "..-"))
        self.lblTelefone.setText(_translate("Dialog", "Telefone"))
        self.edtTelefone.setInputMask(_translate("Dialog", "(99) 99999-9999"))
        self.lblEmail.setText(_translate("Dialog", "Email"))
        self.lblEnd.setText(_translate("Dialog", "Endereço"))
