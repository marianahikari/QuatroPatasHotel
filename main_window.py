import sqlite3
import sys
import os
import re
import pandas as pd
from passlib.hash import bcrypt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


#imports dos outros arquivos
from interface.ui_main import Ui_MainWindow
from mensagens import *
from db.database import DataBase

#imports do Pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QFileDialog, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtGui import QIcon

# ***CLASSE MAINWINDOW***
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro - Quatro Patas Hotel") #titulo da janela
        appIcon = QIcon('icone.ico') #icone da janela
        self.setWindowIcon(appIcon)
        

    #CONEXAO DOS ELEMENTOS COM AS DEFS

        #botoes do menu nas telas home, cad pets, sobre e cad usuario
        #botao home:
        self.bt_home_home.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_home)) 
        self.bt_home_cadPet.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_home)) 
        self.bt_home_sobre.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_home)) 
        self.bt_home_cadUser.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_home))
        #botao pets:
        self.bt_pets_home.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadPet))
        self.bt_pets_cadUser.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadPet))
        self.bt_pets_cadPet.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadPet))
        self.bt_pets_sobre.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadPet))
        #botao sair:
        self.bt_sair_home.clicked.connect(lambda: self.logout())
        self.bt_sair_sobre.clicked.connect(lambda: self.logout())
        self.bt_sair_cadPet.clicked.connect(lambda: self.logout())
        self.bt_sair_cadUser.clicked.connect(lambda: self.logout())
        #botao usuarios
        self.bt_usuarios_home.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadUser))
        self.bt_usuarios_sobre.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadUser)) 
        self.bt_usuarios_cadUser.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadUser)) 
        self.bt_usuarios_cadPet.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_cadUser)) 
 
        #botoes exclusivos da tela home
        self.bt_sobre_home.clicked.connect(lambda: self.telas.setCurrentWidget(self.win_sobre)) #botao sobre

        #elementos exclusivos da tela usuarios
        #cadastro usuarios
        self.bt_cad_cadUser.clicked.connect(self.user_cad) #botao cadastrar novo usuario
        self.bt_edit_cadUser.clicked.connect(self.user_edt) #botao editar cadastro
        self.bt_salvar_cadUser.clicked.connect(self.user_save) #botao salvar edicao
        self.bt_cancelar_cadUser.clicked.connect(self.user_cancel_actions) #botao cancelar cadastro, edicao e/ou selecao
        self.bt_remover_cadUser.clicked.connect(self.user_remove) #botao remover cadastro
        self.bt_exportarExcel_cadUser.clicked.connect(self.user_excel) #botao exportar excel da tabela
        self.bt_pdf_cadUser.clicked.connect(self.user_pdf) #botao gerar pdf do cadastro
        self.edt_filtro_cadUser.textChanged.connect(self.user_filtro) #barra de pesquisa
        #tabela cad usuarios - configuracoes
        self.user_tab() #chama a tabela
        self.tab_cadUser.doubleClicked.connect(self.user_select_info) #mostra o pop up com todas as infos
        #elementos - config de visibilidade e disponibilidade
        self.user_config_elementos() #chama a def da config dos elementos no geral
        self.selected_user_id = None #impede a selecao de registros na tabela ao iniciar a aplicacao
        #formatacao de campos
        self.edt_cpf_cadUser.setInputMask('999.999.999-99') #define o formato do CPF

        #elementos exclusivos da tela pets
        #cadastro pets
        self.bt_cad_cadPet.clicked.connect(self.pet_cad) #botao cadastrar novo pet
        self.bt_edit_cadPet.clicked.connect(self.pet_edt) #botao editar cadastro
        self.bt_salvar_cadPet.clicked.connect(self.pet_save) #botao salvar edicao
        self.bt_cancelar_cadPet.clicked.connect(self.pet_cancel_actions) #botao cancelar cadastro, edicao e/ou selecao
        self.bt_remover_cadPet.clicked.connect(self.pet_remove) #botao remover cadastro
        self.bt_excel_cadPet.clicked.connect(self.pet_excel) #botao exportar excel da tabela
        self.bt_pdf_cadPet.clicked.connect(self.pet_pdf) #botao gerar pdf do cadastro
        self.edt_filtro_cadPet.textChanged.connect(self.pet_filtro) #barra de pesquisa
        #tabela cad usuarios - configuracoes
        self.pet_tab() #chama a tabela
        self.tab_cadPet.doubleClicked.connect(self.pet_select_info) #mostra o pop up com todas as infos
        #elementos - config de visibilidade e disponibilidade
        self.pet_config_elementos() #chama a def da config dos elementos no geral
        self.selected_pet_id = None #impede a selecao de registros na tabela ao iniciar a aplicacao
        #formatacao de campos
        self.edt_telTutor_cadPet.setInputMask('(99)99999-9999') #define o formato do telefone
        self.edt_telEmerg_cadPet.setInputMask('(99)99999-9999')

    #DEFS

    #geral - logout - reinicia a aplicacao
    def logout(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    #usuarios - cadastrar
    def user_cad(self):

        #define as variaveis conforme o preenchimento dos campos
        nome = self.edt_nome_cadUser.text()
        cpf = self.edt_cpf_cadUser.text()
        cargo = self.box_cargo_cadUser.currentText()
        email = self.edt_email_cadUser.text()
        tipo_usuario = self.box_tipoUser_cadUser.currentText()
        login = self.edt_login_cadUser.text()
        senha = self.edt_senha_cadUser.text()
        senha_criptografada = self.cript_senhas(senha) #criptografa a senha

        #verifica erros
        #campos vazios
        if (
            self.edt_nome_cadUser.text() == ""
            or self.edt_cpf_cadUser.text() == ""
            or self.box_cargo_cadUser.currentText() == ""
            or self.edt_email_cadUser.text() == ""
            or self.box_tipoUser_cadUser.currentText() == ""
            or self.edt_login_cadUser.text() == ""
            or self.edt_senha_cadUser.text() == ""
            or self.edt_senhaConfirm_cadUser.text() == ""
        ):
            show_error_popup("Preencha todos os campos!")
            return
        #senhas divergentes
        if self.edt_senha_cadUser.text() != self.edt_senhaConfirm_cadUser.text():
            show_error_popup("Senhas divergentes! Verifique se as senhas foram digitadas corretamente.")
            return None
        #cpf invalido
        if len(cpf) != 14:
            show_error_popup("CPF inválido. Preencha os 11 dígitos!")
            return None

        #registra dos dados das variaveis no BD
        try:
            db = DataBase()
            db.conecta()
            db.insert_usuario(nome, cpf, cargo, email, tipo_usuario, login, senha_criptografada)
            db.close_connection()
        except sqlite3.IntegrityError as e: #erro se o nome de login já for utilizado
            show_error_popup("Nome de login já utilizado. Por favor, escolha outro nome de login.")
            return

        #após cadastrar:
        show_success_popup("Usuário cadastrado! :D") #mensagem de sucesso
        self.user_limpar_campos() #limpa campos
        self.user_tab() #atualiza tabela
        self.selected_user_id = None #limpa selecao de quaisquer registros
        self.user_config_elementos() #redefine visibilidade dos botoes

    #pets - cadastrar
    def pet_cad(self):

        #define as variaveis conforme o preenchimento dos campos
        nome_pet = self.edt_nomePet_cadPet.text()
        raca = self.box_raca_cadPet.currentText()
        cor = self.box_cor_cadPet.currentText()
        peso = self.box_peso_cadPet.currentText()
        sexo = self.box_sexo_cadPet.currentText()
        idade = self.box_idade_cadPet.currentText()
        observacoes = self.edt_obs_cadPet.toPlainText()
        nome_tutor = self.edt_nomeTutor_cadPet.text()
        telefone1 = self.edt_telTutor_cadPet.text()
        endereco = self.edt_end_cadPet.text()
        email = self.edt_email_cadPet.text()
        nome_tutor2 = self.edt_nomeEmerg_cadPet.text()
        telefone2 = self.edt_telEmerg_cadPet.text()

        #verifica erros
        #campos vazios
        if (
            self.edt_nomePet_cadPet.text() == ""
            or self.box_raca_cadPet.currentText() == ""
            or self.box_cor_cadPet.currentText() == ""
            or self.box_peso_cadPet.currentText() == ""
            or self.box_sexo_cadPet.currentText() == ""
            or self.box_idade_cadPet.currentText() == ""
            or self.edt_obs_cadPet.toPlainText() == ""
            or self.edt_nomeTutor_cadPet.text() == ""
            or self.edt_telTutor_cadPet.text() == ""
            or self.edt_end_cadPet.text() == ""
        ):
            show_error_popup("Preencha todos os campos!")
            return
        #tel1 invalido
        if len(telefone1) != 14:
            show_error_popup("Número de telefone do Tutor inválido.")
            return None
        #tel2 invalido
        if len(telefone2) != 14:
            show_error_popup("Número de telefone do contato de emergência inválido.")
            return None

        #registra dos dados das variaveis no BD
        try:
            db = DataBase()
            db.conecta()
            db.insert_pet(nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2)
            db.close_connection()
        except sqlite3.IntegrityError as e:
            show_error_popup("Erro ao inserir o pet: " + str(e))
            return

        #após cadastrar:
        show_success_popup("Pet cadastrado! :D") #mensagem de sucesso
        self.pet_limpar_campos() #limpa campos
        self.pet_tab() #atualiza tabela
        self.selected_pet_id = None #limpa selecao de quaisquer registros
        self.pet_config_elementos() #redefine visibilidade dos botoes

    #usuarios - editar cadastro
    def user_edt(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_user_id is None:
            show_error_popup("Nenhum usuário selecionado.")
            return

        #obtem o id do registro
        id_usuario = self.selected_user_id

        #recupera dados do usuario selecionado
        db = DataBase()
        db.conecta()
        usuario = db.get_usuario(id_usuario)
        db.close_connection()

        if usuario is None:
            show_error_popup("Usuário não encontrado.")
            return

        #preenche os campos com os dados do usuário selecionado
        self.edt_nome_cadUser.setText(usuario["nome"])
        self.edt_cpf_cadUser.setText(usuario["cpf"])
        self.box_cargo_cadUser.setCurrentText(usuario["cargo"])
        self.edt_email_cadUser.setText(usuario["email"])
        self.box_tipoUser_cadUser.setCurrentText(usuario["tipo_usuario"])
        self.edt_login_cadUser.setText(usuario["login"])
        self.edt_senha_cadUser.setText(usuario["senha"])
        self.edt_senhaConfirm_cadUser.setText(usuario["senha"])

        #definicao da visibilidade e disponibilidade dos elementos quando clica em 'editar'
        self.user_habilitar_campos(True) #permite o preenchimento dos campos
        self.bt_salvar_cadUser.setVisible(True) #botao salvar visivel
        self.bt_salvar_cadUser.setEnabled(True)
        self.bt_cancelar_cadUser.setVisible(True) #botao cancelar visivel
        self.bt_cancelar_cadUser.setEnabled(True)
        self.bt_edit_cadUser.setVisible(False) #oculta botao editar
        self.bt_pdf_cadUser.setVisible(False) #oculta botao pdf
        self.bt_exportarExcel_cadUser.setVisible(False) #oculta botao excel
        self.bt_cad_cadUser.setVisible(False) #oculta botao cadastrar
        self.tab_cadUser.setEnabled(False) #bloqueia a tabela

    #pets - editar cadastro
    def pet_edt(self):
        # verifica se algum registro da tabela está selecionado
        if self.selected_pet_id is None:
            show_error_popup("Nenhum pet selecionado.")
            return

        # obtém o id do registro
        id_pet = self.selected_pet_id

        # recupera dados do pet selecionado
        db = DataBase()
        db.conecta()
        pet = db.get_pet(id_pet)
        db.close_connection()

        if pet is None:
            show_error_popup("Pet não encontrado.")
            return

        # preenche os campos com os dados do pet selecionado
        self.edt_nomePet_cadPet.setText(pet["nome_pet"])
        self.box_raca_cadPet.setCurrentText(pet["raca"])
        self.box_cor_cadPet.setCurrentText(pet["cor"])
        self.box_peso_cadPet.setCurrentText(pet["peso"])
        self.box_sexo_cadPet.setCurrentText(pet["sexo"])
        self.box_idade_cadPet.setCurrentText(pet["idade"])
        self.edt_obs_cadPet.setPlainText(pet["observacoes"])
        self.edt_nomeTutor_cadPet.setText(pet["nome_tutor"])
        self.edt_telTutor_cadPet.setText(pet["telefone1"])
        self.edt_end_cadPet.setText(pet["endereco"])
        self.edt_email_cadPet.setText(pet["email"])
        self.edt_nomeEmerg_cadPet.setText(pet["nome_tutor2"])
        self.edt_telEmerg_cadPet.setText(pet["telefone2"])

        # definição da visibilidade e disponibilidade dos elementos quando clica em 'editar'
        self.pet_habilitar_campos(True)  # permite o preenchimento dos campos
        self.bt_salvar_cadPet.setVisible(True)  # botao salvar visível
        self.bt_salvar_cadPet.setEnabled(True)
        self.bt_cancelar_cadPet.setVisible(True)  # botao cancelar visível
        self.bt_cancelar_cadPet.setEnabled(True)
        self.bt_edit_cadPet.setVisible(False)  # oculta botão editar
        self.bt_pdf_cadPet.setVisible(False)  # oculta botão pdf
        self.bt_excel_cadPet.setVisible(False)  # oculta botão excel
        self.bt_cad_cadPet.setVisible(False)  # oculta botão cadastrar
        self.tab_cadPet.setEnabled(False)  # bloqueia a tabela

    #usuarios - salvar edicao do cadastro
    def user_save(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_user_id is None:
            show_error_popup("Nenhum usuário selecionado.")
            return

        #obtem o id do registro
        id_usuario = self.selected_user_id

        #obtem os valores dos campos
        nome = self.edt_nome_cadUser.text()
        cpf = self.edt_cpf_cadUser.text()
        cargo = self.box_cargo_cadUser.currentText()
        email = self.edt_email_cadUser.text()
        tipo_usuario = self.box_tipoUser_cadUser.currentText()
        login = self.edt_login_cadUser.text()
        senha = self.edt_senha_cadUser.text()
        senha_criptografada = self.cript_senhas(senha)  #criptografa a senha

        #verifica erros
        #campos vazios
        if (
            self.edt_nome_cadUser.text() == ""
            or self.edt_cpf_cadUser.text() == ""
            or self.box_cargo_cadUser.currentText() == ""
            or self.edt_email_cadUser.text() == ""
            or self.box_tipoUser_cadUser.currentText() == ""
            or self.edt_login_cadUser.text() == ""
            or self.edt_senha_cadUser.text() == ""
            or self.edt_senhaConfirm_cadUser.text() == ""
        ):
            show_error_popup("Preencha todos os campos!")
            return
        #senhas divergentes
        if self.edt_senha_cadUser.text() != self.edt_senhaConfirm_cadUser.text():
            show_error_popup("Senhas divergentes! Verifique se as senhas foram digitadas corretamente.")
            return None
        #cpf invalido
        if len(cpf) != 14:
            show_error_popup("CPF inválido. Preencha os 11 dígitos!")
            return None
        
        #verifica se o nome de login já está sendo utilizado por outro usuário (exceto o usuário atual)
        db = DataBase()
        db.conecta()
        usuario_atual = db.get_usuario(id_usuario)

        if usuario_atual is not None and usuario_atual["login"] != login:
            if db.is_login_used(login):
                show_error_popup("Nome de login já utilizado. Por favor, escolha outro nome de login.")
                db.close_connection()
                return

        #atualiza os dados do usuário no banco de dados
        try:
            db.update_usuario(id_usuario, nome, cpf, cargo, email, tipo_usuario, login, senha_criptografada)
            db.close_connection()
        except Exception as e:
            show_error_popup("Erro ao atualizar o usuário: " + str(e))
            return

        #após salvar
        show_success_popup("Usuário alterado! :D")  #mensagem de sucesso
        self.user_limpar_campos()  #limpa campos
        self.user_tab()  #atualiza tabela
        self.selected_user_id = None  #limpa seleção de quaisquer registros
        self.user_config_elementos()  #redefine visibilidade dos botões

    def pet_save(self):
        #verifica se algum registro na tabela está selecionado
        if self.selected_pet_id is None:
            show_error_popup("Nenhum pet selecionado.")
            return

        #obtem o ID do registro
        id_pet = self.selected_pet_id

        #obtem os valores dos campos
        nome_pet = self.edt_nomePet_cadPet.text()
        raca = self.box_raca_cadPet.currentText()
        cor = self.box_cor_cadPet.currentText()
        peso = self.box_peso_cadPet.currentText()
        sexo = self.box_sexo_cadPet.currentText()
        idade = self.box_idade_cadPet.currentText()
        observacoes = self.edt_obs_cadPet.toPlainText()
        nome_tutor = self.edt_nomeTutor_cadPet.text()
        telefone1 = self.edt_telTutor_cadPet.text()
        endereco = self.edt_end_cadPet.text()
        email = self.edt_email_cadPet.text()
        nome_tutor2 = self.edt_nomeEmerg_cadPet.text()
        telefone2 = self.edt_telEmerg_cadPet.text()

        #verifica erros
        #campos vazios
        if (
            self.edt_nomePet_cadPet.text() == ""
            or self.box_raca_cadPet.currentText() == ""
            or self.box_cor_cadPet.currentText() == ""
            or self.box_peso_cadPet.currentText() == ""
            or self.box_sexo_cadPet.currentText() == ""
            or self.box_idade_cadPet.currentText() == ""
            or self.edt_obs_cadPet.toPlainText() == ""
            or self.edt_nomeTutor_cadPet.text() == ""
            or self.edt_telTutor_cadPet.text() == ""
            or self.edt_end_cadPet.text() == ""
        ):
            show_error_popup("Preencha todos os campos!")
            return
        #tel1 invalido
        if len(telefone1) != 14:
            show_error_popup("Número de telefone do Tutor inválido.")
            return None
        #tel2 invalido
        if len(telefone2) != 14:
            show_error_popup("Número de telefone do contato de emergência inválido.")
            return None

        # Salva as informações do pet no banco de dados
        try:
            db = DataBase()
            db.conecta()
            db.update_pet(
                id_pet, nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2
            )
            db.close_connection()
        except Exception as e:
            show_error_popup("Erro ao atualizar o pet: " + str(e))
            return

        # Após salvar
        show_success_popup("Pet alterado! :D")  # Mostrar mensagem de sucesso
        self.pet_limpar_campos()  # Limpar campos
        self.pet_tab()  # Atualizar a tabela
        self.selected_pet_id = None  # Limpar seleção de quaisquer registros
        self.pet_config_elementos()  # Redefinir visibilidade dos botões

    #usuarios - remover cadastro
    def user_remove(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_user_id is None:
            show_error_popup("Nenhum usuário selecionado.")
            return
        
        #obtem o id do registro
        id_usuario = self.selected_user_id

        #confirma a exclusão com o usuário
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Remover Usuário")
        msg_box.setText("Tem certeza de que deseja remover este usuário?")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        reply = msg_box.exec()
        if reply == QMessageBox.Yes: #remove o cadastro
            db = DataBase()
            db.conecta()
            db.remover_usuario(id_usuario)
            db.close_connection()

            show_success_popup("Usuário removido! :D")

        #após remover usuario
        self.user_tab()  #atualiza tabela
        self.user_limpar_campos() #limpa campos
        self.selected_user_id = None  #limpa seleção de quaisquer registros
        self.user_config_elementos()  #redefine visibilidade dos botões

    #pets - remover cadastro
    def pet_remove(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_pet_id is None:
            show_error_popup("Nenhum pet selecionado.")
            return
        
        #obtem o id do registro
        id_pet = self.selected_pet_id

        #confirma a exclusão com o usuário
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Remover pet")
        msg_box.setText("Tem certeza de que deseja remover este pet?")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        reply = msg_box.exec()
        if reply == QMessageBox.Yes: #remove o cadastro
            db = DataBase()
            db.conecta()
            db.remover_pet(id_pet)
            db.close_connection()

            show_success_popup("Pet removido! :D")

        #após remover pet
        self.pet_tab()  #atualiza tabela
        self.pet_limpar_campos() #limpa campos
        self.selected_pet_id = None  #limpa seleção de quaisquer registros
        self.pet_config_elementos()  #redefine visibilidade dos botões

    #usuarios - cancela ações
    def user_cancel_actions(self):
        #limpa os campos
        self.user_limpar_campos()

        #deseleciona o registro selecionado, se houver
        self.tab_cadUser.clearSelection()

        #atualiza a seleção e visibilidade dos botões
        self.selected_user_id = None
        self.user_config_elementos()

    #pets - cancela ações
    def pet_cancel_actions(self):
        #limpa campos
        self.pet_limpar_campos()

        #deseleciona o registro selecionado, se houver
        self.tab_cadPet.clearSelection()

        #atualiza a selecao e a visibilidade dos botoes
        self.selected_pet_id = None
        self.pet_config_elementos()

    #usuarios - gerar excel da tabela
    def user_excel(self):
        #conecta ao DB
        db_folder = "db"
        db_file = "system.db"
        db_path = os.path.join(db_folder, db_file)
        cnx = sqlite3.connect(db_path)
        query = "SELECT * FROM usuarios" #obtem dados da tabela 'usuarios'
        result = pd.read_sql_query(query, cnx)
        result = result.drop("senha", axis=1) #remove a coluna 'senha'

        #fecha a conexão com o DB
        cnx.close()

        #permite escolher o local para salvar o arquivo
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        #verifica se um local foi selecionado e salva o arquivo em Excel
        if file_name:
            result.to_excel(file_name, sheet_name="usuarios", index=False)
            show_success_popup("Relatório Excel gerado e salvo! :D")

    #pets - gerar excel da tabela
    def pet_excel(self):
        #conecta ao DB
        db_folder = "db"
        db_file = "system.db"
        db_path = os.path.join(db_folder, db_file)
        cnx = sqlite3.connect(db_path)
        query = "SELECT * FROM pets" #obtem dados da tabela 'pets'
        result = pd.read_sql_query(query, cnx)

        #fecha a conexão com o DB
        cnx.close()

        #permite escolher o local para salvar o arquivo
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        #verifica se um local foi selecionado e salva o arquivo em Excel
        if file_name:
            result.to_excel(file_name, sheet_name="pets", index=False)
            show_success_popup("Relatório Excel gerado e salvo! :D")

    #usuarios - gerar pdf do cadastro
    def user_pdf(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_user_id is None:
            show_error_popup("Nenhum usuário selecionado.")
            return

        #obtem o id do registro
        id_usuario = self.selected_user_id

        #permite escolher o local para salvar o arquivo
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            self, "Salvar PDF", "", "PDF Files (*.pdf)"
        )

        if file_path:
            #gera pdf e salva no caminho especificado
            try:
                #inicializa canvas
                c = canvas.Canvas(file_path)
                #obtem dados do usuario
                db = DataBase()
                db.conecta()
                usuario = db.get_usuario(id_usuario)
                db.close_connection()

                #escreve dados no pdf
                pdf_width, pdf_height = letter
                left_margin = 0

                c.setFont("Helvetica", 18)
                text = "QUATRO PATAS HOTEL"
                text_width = c.stringWidth(text, "Helvetica", 18)
                text_x = (pdf_width - text_width) / 2
                text_y = 800
                c.drawString(text_x, text_y, text)

                line_y = text_y - 20 
                c.line(left_margin, line_y, pdf_width - left_margin, line_y)

                c.setFont("Helvetica", 15)
                c.drawString(100, text_y - 60, "Informações do usuário")

                text_y -= 80

                c.setFont("Helvetica", 12)
                c.drawString(100, text_y - 20, "ID: " + str(usuario["id"]))
                c.drawString(100, text_y - 40, "Nome: " + usuario["nome"])
                c.drawString(100, text_y - 60, "CPF: " + usuario["cpf"])
                c.drawString(100, text_y - 80, "Cargo: " + usuario["cargo"])
                c.drawString(100, text_y - 100, "Email: " + usuario["email"])
                c.drawString(100, text_y - 120, "Tipo de Usuário: " + usuario["tipo_usuario"])

                #salva o pdf
                c.save()

                show_success_popup("PDF gerado e salvo! :D")
            except Exception as e:
                show_error_popup("Erro ao gerar o PDF: " + str(e))
        else:
            show_error_popup("Nenhum caminho de arquivo selecionado.")

    #pets - gerar pdf do cadastro
    def pet_pdf(self):
        #verifica se algum registro da tabela está selecionado
        if self.selected_pet_id is None:
            show_error_popup("Nenhum pet selecionado.")
            return

        #obtem o id do registro
        id_pet = self.selected_pet_id

        #permite escolher o local para salvar o arquivo
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            self, "Salvar PDF", "", "PDF Files (*.pdf)"
        )

        if file_path:
            #gera pdf e salva no caminho especificado
            try:
                #inicializa canvas
                c = canvas.Canvas(file_path)
                #obtem dados do pet
                db = DataBase()
                db.conecta()
                pet = db.get_pet(id_pet)
                db.close_connection()

                #escreve dados no pdf
                pdf_width, pdf_height = letter
                left_margin = 0

                c.setFont("Helvetica", 18)
                text = "QUATRO PATAS HOTEL"
                text_width = c.stringWidth(text, "Helvetica", 18)
                text_x = (pdf_width - text_width) / 2
                text_y = 800
                c.drawString(text_x, text_y, text)

                line_y = text_y - 20 
                c.line(left_margin, line_y, pdf_width - left_margin, line_y)

                c.setFont("Helvetica", 15)
                c.drawString(100, text_y - 60, "Informações do pet")

                text_y -= 80

                c.setFont("Helvetica", 12)
                c.drawString(100, text_y - 20, "Nome do Pet: " + pet["nome_pet"])
                c.drawString(100, text_y - 40, "Raça: " + pet["raca"])
                c.drawString(100, text_y - 60, "Cor: " + pet["cor"])
                c.drawString(100, text_y - 80, "Peso: " + pet["peso"])
                c.drawString(100, text_y - 100, "Sexo: " + pet["sexo"])
                c.drawString(100, text_y - 120, "Idade: " + pet["idade"])
                c.drawString(100, text_y - 140, "Observações: " + pet["observacoes"])
                c.drawString(100, text_y - 165, "-")
                c.drawString(100, text_y - 190, "Nome do Tutor: " + pet["nome_tutor"])
                c.drawString(100, text_y - 210, "Telefone do Tutor: " + pet["telefone1"])
                c.drawString(100, text_y - 230, "Endereço: " + pet["endereco"])
                c.drawString(100, text_y - 250, "Email: " + pet["email"])
                c.drawString(100, text_y - 270, "Nome - Contato de Emergência: " + pet["nome_tutor2"])
                c.drawString(100, text_y - 290, "Tel. - Contato de Emergência: " + pet["telefone2"])

                #salva o pdf
                c.save()

                show_success_popup("PDF gerado e salvo! :D")
            except Exception as e:
                show_error_popup("Erro ao gerar o PDF: " + str(e))
        else:
            show_error_popup("Nenhum caminho de arquivo selecionado.")

    #usuarios - criptografar senhas
    def cript_senhas(self, password):
        return bcrypt.hash(password)

    #usuarios - definicao tabela
    def user_tab(self):
        self.tab_cadUser.setStyleSheet("QTableView { background-color: white; selection-background-color: lightblue;} QHeaderView { color: black; font-size: 11px; }") #definicoes style da tabela

        #conexao com o BD
        db_folder = "db"
        db_file = "system.db"
        db_path = os.path.join(db_folder, db_file)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(db_path)
        db.open()

        #configuracao do modelo da tabela com a tabela do BD
        self.user_model = QSqlTableModel(db=db)
        self.tab_cadUser.setModel(self.user_model)
        self.user_model.setTable("usuarios")
        self.user_model.select()

        #config adicionais
        self.tab_cadUser.setSelectionMode(QAbstractItemView.SingleSelection) #permite selecao de apenas uma linha por vez
        self.tab_cadUser.setSelectionBehavior(QAbstractItemView.SelectRows) #define a selecao da linha por completo
        self.tab_cadUser.setEditTriggers(QAbstractItemView.NoEditTriggers) #impede a edicao direto na tabela
        self.tab_cadUser.selectionModel().selectionChanged.connect(self.user_config_elementos) #atualiza a visibilidade dos botoes (registro selecionado/desselecionado)
        self.tab_cadUser.resizeColumnsToContents() #ajusta o tamanho de cada coluna com base no conteúdo exibido
        self.tab_cadUser.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #preenche a largura total da tabela
        self.tab_cadUser.hideColumn(7) #oculta a coluna senha
        self.tab_cadUser.clicked.connect(self.user_select) #registro é selecionado ao clicar na tabela

    #pets - definicao tabela
    def pet_tab(self):
        self.tab_cadPet.setStyleSheet("QTableView { background-color: white; selection-background-color: lightblue;} QHeaderView { color: black; font-size: 11px; }") #definicoes style da tabela

        #conexao com o BD
        db_folder = "db"
        db_file = "system.db"
        db_path = os.path.join(db_folder, db_file)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(db_path)
        db.open()

        #configuracao do modelo da tabela com a tabela do BD
        self.pet_model = QSqlTableModel(db=db)
        self.tab_cadPet.setModel(self.pet_model)
        self.pet_model.setTable("pets")
        self.pet_model.select()

        #config adicionais
        self.tab_cadPet.setSelectionMode(QAbstractItemView.SingleSelection) #permite selecao de apenas uma linha por vez
        self.tab_cadPet.setSelectionBehavior(QAbstractItemView.SelectRows) #define a selecao da linha por completo
        self.tab_cadPet.setEditTriggers(QAbstractItemView.NoEditTriggers) #impede a edicao direto na tabela
        self.tab_cadPet.selectionModel().selectionChanged.connect(self.user_config_elementos) #atualiza a visibilidade dos botoes (registro selecionado/desselecionado)
        self.tab_cadPet.resizeColumnsToContents() #ajusta o tamanho de cada coluna com base no conteúdo exibido,
        self.tab_cadPet.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #preenche a largura total da tabela
        self.tab_cadPet.clicked.connect(self.pet_select) #registro é selecionado ao clicar na tabela

    #usuarios - selecao de registro
    def user_select(self, index):
        row = index.row() #obtem o indice da linha selecionada
        if row >= 0:
            self.selected_user_id = self.user_model.data(self.user_model.index(row, 0)) #obtem o id do registro selecionado
        else:
            self.selected_user_id = None 
        self.user_config_elementos() #atualiza a visibilidade dos botões

    #pets - selecao de registro
    def pet_select(self, index):
        row = index.row() #obtem o indice da linha selecionada
        if row >= 0:
            self.selected_pet_id = self.pet_model.data(self.pet_model.index(row, 0)) #obtem o id do registro selecionado
        else:
            self.selected_pet_id = None 
        self.pet_config_elementos() #atualiza a visibilidade dos botões

    #usuarios - exibe em um pop up as infos do cadastro selecionado
    def user_select_info(self, index):
        row = index.row() #obtem o indice da linha selecionada
        if row >= 0:
            self.selected_user_id = self.user_model.data(self.user_model.index(row, 0)) #obtem o id do registro selecionado
            #recupera dados do usuario selecionado
            db = DataBase()
            db.conecta()
            usuario = db.get_usuario(self.selected_user_id)
            db.close_connection()

            if usuario is not None:
                show_user_info_popup(usuario)
            else:
                show_error_popup("Usuário não encontrado.")
        else:
            self.selected_user_id = None 
        self.user_config_elementos() #atualiza a visibilidade dos botões

    #pets - exibe em um pop up as infos do cadastro selecionado
    def pet_select_info(self, index):
        row = index.row()  # obtem o índice da linha selecionada
        if row >= 0:
            self.selected_pet_id = self.pet_model.data(self.pet_model.index(row, 0))  # obtem o id do registro selecionado
            # recupera dados do pet selecionado
            db = DataBase()
            db.conecta()
            pet = db.get_pet(self.selected_pet_id)
            db.close_connection()

            if pet is not None:
                show_pet_info_popup(pet)
            else:
                show_error_popup("Pet não encontrado.")
        else:
            self.selected_pet_id = None
        self.pet_config_elementos()  #atualiza a visibilidade dos botões

    #usuarios - filtro de pesquisa
    def user_filtro(self, s):
        s = re.sub(r"\W+", "", s) #garante que a string de busca contenha apenas caracteres alfanuméricos
        filter_str = ('id LIKE "%{0}%" OR nome LIKE "%{0}%" OR cpf LIKE "%{0}%" OR email LIKE "%{0}%" OR cargo LIKE "%{0}%" OR tipo_usuario LIKE "%{0}%" OR login LIKE "%{0}%"').format(s) #filtra dados com base na string de busca
        self.user_model.setFilter(filter_str) #mostra apenas as linhas que correspondem a string de busca

    #pets - filtro de pesquisa 
    def pet_filtro(self, s):
        s = re.sub(r"\W+", "", s) # garante que a string de busca contenha apenas caracteres alfanuméricos
        filter_str = ('id LIKE "%{0}%" OR nome_pet LIKE "%{0}%" OR raca LIKE "%{0}%" OR cor LIKE "%{0}%" OR peso LIKE "%{0}%" OR sexo LIKE "%{0}%" OR idade LIKE "%{0}%" OR observacoes LIKE "%{0}%" OR nome_tutor LIKE "%{0}%" OR telefone1 LIKE "%{0}%" OR endereco LIKE "%{0}%" OR email LIKE "%{0}%" OR nome_tutor2 LIKE "%{0}%" OR telefone2 LIKE "%{0}%"').format(s) #filtra dados com base na string de busca
        self.pet_model.setFilter(filter_str) # mostra apenas as linhas que correspondem à string de busca

    #usuarios - configuracao elementos
    def user_config_elementos(self):
        indexes = self.tab_cadUser.selectionModel().selectedRows()
        if len(indexes) > 0: #se um registro estiver selecionado
            self.bt_edit_cadUser.setVisible(True) #botao editar visivel
            self.bt_edit_cadUser.setEnabled(True)
            self.bt_remover_cadUser.setVisible(True) #botao remover visivel
            self.bt_remover_cadUser.setEnabled(True)
            self.bt_pdf_cadUser.setVisible(True) #botao pdf visivel
            self.bt_pdf_cadUser.setEnabled(True)
            self.bt_cancelar_cadUser.setVisible(True) #botao cancelar visivel
            self.bt_cancelar_cadUser.setEnabled(True)
            self.bt_exportarExcel_cadUser.setVisible(False) #oculta botao excel
            self.bt_cad_cadUser.setVisible(False) #oculta botao cadastrar
            self.bt_salvar_cadUser.setVisible(False) #oculta botao salvar
            self.user_habilitar_campos(False) #impede o preenchimento dos campos
        else: #nenhum registro selecionado
            self.user_habilitar_campos(True) #permite o preenchimento dos campos
            self.tab_cadUser.setEnabled(True) #permite selecoes na tabela
            self.bt_exportarExcel_cadUser.setVisible(True) #botao excel visivel
            self.bt_exportarExcel_cadUser.setEnabled(True)
            self.bt_cad_cadUser.setVisible(True) #botao cadastrar visivel
            self.bt_cad_cadUser.setEnabled(True) 
            self.bt_edit_cadUser.setVisible(False) #oculta botao editar
            self.bt_remover_cadUser.setVisible(False) #oculta botao remover
            self.bt_pdf_cadUser.setVisible(False) #oculta botao pdf
            self.bt_cancelar_cadUser.setVisible(True) #botao cancelar visivel
            self.bt_salvar_cadUser.setVisible(False) #oculta botao salvar
    
    #pets - configuracao elementos
    def pet_config_elementos(self):
        indexes = self.tab_cadPet.selectionModel().selectedRows()
        if len(indexes) > 0: # se um registro estiver selecionado
            self.bt_edit_cadPet.setVisible(True) # botao editar visível
            self.bt_edit_cadPet.setEnabled(True)
            self.bt_remover_cadPet.setVisible(True) # botao remover visível
            self.bt_remover_cadPet.setEnabled(True)
            self.bt_pdf_cadPet.setVisible(True) # botao pdf visível
            self.bt_pdf_cadPet.setEnabled(True)
            self.bt_cancelar_cadPet.setVisible(True) # botao cancelar visível
            self.bt_cancelar_cadPet.setEnabled(True)
            self.bt_excel_cadPet.setVisible(False) # oculta botao excel
            self.bt_cad_cadPet.setVisible(False) # oculta botao cadastrar
            self.bt_salvar_cadPet.setVisible(False) # oculta botao salvar
            self.pet_habilitar_campos(False) # impede o preenchimento dos campos
        else: # nenhum registro selecionado
            self.pet_habilitar_campos(True) # permite o preenchimento dos campos
            self.tab_cadPet.setEnabled(True) # permite seleções na tabela
            self.bt_excel_cadPet.setVisible(True) # botao excel visível
            self.bt_excel_cadPet.setEnabled(True)
            self.bt_cad_cadPet.setVisible(True) # botao cadastrar visível
            self.bt_cad_cadPet.setEnabled(True) 
            self.bt_edit_cadPet.setVisible(False) # oculta botao editar
            self.bt_remover_cadPet.setVisible(False) # oculta botao remover
            self.bt_pdf_cadPet.setVisible(False) # oculta botao pdf
            self.bt_cancelar_cadPet.setVisible(True) # botao cancelar visível
            self.bt_salvar_cadPet.setVisible(False) # oculta botao salvar
            
    #usuarios - habilita todos os campos de preenchimento
    def user_habilitar_campos(self, enabled):
        self.edt_nome_cadUser.setEnabled(enabled)
        self.edt_cpf_cadUser.setEnabled(enabled)
        self.box_cargo_cadUser.setEnabled(enabled)
        self.edt_email_cadUser.setEnabled(enabled)
        self.box_tipoUser_cadUser.setEnabled(enabled)
        self.edt_login_cadUser.setEnabled(enabled)
        self.edt_senha_cadUser.setEnabled(enabled)
        self.edt_senhaConfirm_cadUser.setEnabled(enabled)

    #pets - habilita todos os campos de preenchimento
    def pet_habilitar_campos(self, enabled):
        self.edt_nomePet_cadPet.setEnabled(enabled)
        self.box_raca_cadPet.setEnabled(enabled)
        self.box_cor_cadPet.setEnabled(enabled)
        self.box_peso_cadPet.setEnabled(enabled)
        self.box_sexo_cadPet.setEnabled(enabled)
        self.box_idade_cadPet.setEnabled(enabled)
        self.edt_obs_cadPet.setEnabled(enabled)
        self.edt_nomeTutor_cadPet.setEnabled(enabled)
        self.edt_telTutor_cadPet.setEnabled(enabled)
        self.edt_end_cadPet.setEnabled(enabled)
        self.edt_email_cadPet.setEnabled(enabled)
        self.edt_nomeEmerg_cadPet.setEnabled(enabled)
        self.edt_telEmerg_cadPet.setEnabled(enabled)

    #usuarios - limpa os campos
    def user_limpar_campos(self): 
        self.edt_nome_cadUser.setText("")
        self.edt_cpf_cadUser.setText("")
        self.edt_email_cadUser.setText("")
        self.edt_login_cadUser.setText("")
        self.edt_senha_cadUser.setText("")
        self.edt_senhaConfirm_cadUser.setText("")
        self.box_cargo_cadUser.setCurrentIndex(-1)
        self.box_tipoUser_cadUser.setCurrentIndex(-1)

    #pets - limpa campos
    def pet_limpar_campos(self):
        self.edt_nomePet_cadPet.setText("")
        self.box_raca_cadPet.setCurrentIndex(-1)
        self.box_cor_cadPet.setCurrentIndex(-1)
        self.box_peso_cadPet.setCurrentIndex(-1)
        self.box_sexo_cadPet.setCurrentIndex(-1)
        self.box_idade_cadPet.setCurrentIndex(-1)
        self.edt_obs_cadPet.setPlainText("")
        self.edt_nomeTutor_cadPet.setText("")
        self.edt_telTutor_cadPet.setText("")
        self.edt_end_cadPet.setText("")
        self.edt_email_cadPet.setText("")
        self.edt_nomeEmerg_cadPet.setText("")
        self.edt_telEmerg_cadPet.setText("")