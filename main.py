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
import schedule
import os
import time
import shutil
from datetime import datetime
from UCustomMessageBox import CustomMessageBox
import threading


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

        self.agendar_backup()

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

    def backup(self):
        try:
            print("Iniciando backup")
            # Nome do arquivo de backup (inclui a data e hora atual)
            data_hora_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            arquivo_backup = f"backup_{data_hora_atual}.sql"

            # Caminho completo para o arquivo de backup
            caminho_backup = os.path.join(os.getcwd(), arquivo_backup)

            # Comando para fazer o backup usando o utilitário mysqldump
            comando_backup = fr'"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump" --host=localhost --user=root --password=masterkey control > {caminho_backup}'

            # Execute o comando de backup
            os.system(comando_backup)

            # Copie o arquivo de backup para a pasta de destino
            pasta_destino = r'C:\Users\thiag\Google Drive\Backup'
            shutil.copy(caminho_backup, os.path.join(pasta_destino, arquivo_backup))
        except Exception as e:
            CustomMessageBox("Erro", f"Ocorreu um erro durante o backup dos dados: \n {str(e)}").error.exec_()

    def agendar_backup(self):
        schedule.every().day.at("15:00").do(self.backup)
        threading.Thread(target=self.run_backup_thread).start()

    def run_backup_thread(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())