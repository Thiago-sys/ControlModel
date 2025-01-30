from PyQt6 import QtWidgets


class CustomMessageBox():
    def __init__(self, Title: str, Message: str):

        # Exibir um diálogo de confirmação
        self.confirmation = QtWidgets.QMessageBox()
        self.confirmation.setIcon(QtWidgets.QMessageBox.Question)
        self.confirmation.setWindowTitle(Title)
        self.confirmation.setText(Message)
        self.confirmation.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.confirmation.button(QtWidgets.QMessageBox.Yes).setText("Sim")
        self.confirmation.button(QtWidgets.QMessageBox.No).setText("Não")

        self.error = QtWidgets.QMessageBox()
        self.error.setIcon(QtWidgets.QMessageBox.Critical)
        self.error.setWindowTitle(Title)
        self.error.setText(Message)
        self.error.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.information = QtWidgets.QMessageBox()
        self.information.setIcon(QtWidgets.QMessageBox.Information)
        self.information.setWindowTitle(Title)
        self.information.setText(Message)
        self.information.setStandardButtons(QtWidgets.QMessageBox.Ok)

