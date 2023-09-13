from PySide6.QtWidgets import QWidget
from interface.ui_login import Ui_window_login
from main_window import MainWindow
from mensagens import show_error_popup
from db.database import DataBase
from PySide6.QtGui import QIcon

# ***CLASSE LOGINWINDOW***
class loginWindow(QWidget, Ui_window_login):
    def __init__(self) -> None:
        super(loginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login - Sistema de Cadastro") #titulo da janela
        appIcon = QIcon('icone.ico') #icone da janela
        self.setWindowIcon(appIcon)

        #CONEXAO DO BOTAO COM A DEF
        self.bt_entrar_login.clicked.connect(self.checar_login) #botao entrar
        self.edt_senha_login.returnPressed.connect(self.checar_login) #permite entrar com a tecla 'enter'

    #funcao para abrir o sistema sem o database, se for necessario (usar no lugar de "checar_login")
    def abrir_sistema(self):
        senha = self.edt_senha_login.text()
        usuario = self.edt_user_login.text()

        if senha == '' or usuario == '': #verifica se todos os campos estao preenchidos
            show_error_popup("Por favor, preencha todos os campos.")
        elif senha == 'senha123' and usuario == 'admin': #libera o acesso a tela main se o login e a senha corresponderem a esses dados
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            show_error_popup("Senha e/ou usuário inválidos.") #mensagem de erro se o login e/ou a senha nao corresponderem

    #funcao para verificar credenciais de login com base no BD
    def checar_login(self):
        if self.edt_user_login.text() == "" or self.edt_senha_login.text() == "": #verifica se todos os campos estao preenchidos
            show_error_popup("Por favor, preencha todos os campos.")
            return

        #conexao com o BD
        self.usuarios = DataBase()
        self.usuarios.conecta()

        autenticado = self.usuarios.check_user(self.edt_user_login.text().upper(), self.edt_senha_login.text()) #retorna o tipo de usuario ***se o login e a senha corresponderem ao BD***

        print(autenticado) #imprime o tipo do usuario

        if autenticado == "Administrador" or autenticado == "Comum": #libera o acesso a tela main se houver o retorno do tipo de usuario
            self.w = MainWindow()
            self.w.show()

            #visibilidade do botao de cadastrar usuario (visivel só para adm)
            if autenticado == "Administrador":
                self.w.bt_usuarios_home.setVisible(True)
                self.w.bt_usuarios_sobre.setVisible(True)
                self.w.bt_usuarios_cadPet.setVisible(True)
                self.w.bt_usuarios_cadUser.setVisible(True)
            else:
                self.w.bt_usuarios_home.setVisible(False)
                self.w.bt_usuarios_sobre.setVisible(False)
                self.w.bt_usuarios_cadPet.setVisible(False)
                self.w.bt_usuarios_cadUser.setVisible(False)
            self.close()
        else:
            show_error_popup("Senha e/ou usuário inválidos.") #mensagem de erro se nao houver retorno do tipo de usuario