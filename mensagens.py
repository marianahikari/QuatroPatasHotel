from PySide6.QtWidgets import(QMessageBox, QTextEdit, QVBoxLayout, QPushButton, QLabel, QDialog)
from mensagens import *

#mensagem de erro geral
def show_error_popup(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setText("Erro")
    error_box.setInformativeText(message)
    error_box.setWindowTitle("Sistema de Cadastro")
    error_box.exec_()

#mensagem de sucesso geral
def show_success_popup(message):
    success_box = QMessageBox()
    success_box.setIcon(QMessageBox.Information)
    success_box.setText("Ação realizada com sucesso.")
    success_box.setInformativeText(message)
    success_box.setWindowTitle("Sistema de Cadastro")
    success_box.exec_()

#exibe as informações do usuário em um pop up
def show_user_info_popup(usuario):
    dialog = QDialog()
    dialog.setWindowTitle("Sistema de Cadastros")
    dialog.setFixedSize(422, 375)  #tamanho fixo do popup

    layout = QVBoxLayout(dialog)

    title_label = QLabel("<b>INFORMAÇÕES DO USUÁRIO</b>")
    layout.addWidget(title_label)

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setHtml(
        f"<b>ID:</b> {usuario['id']}<br><br>"
        f"<b>Nome:</b> {usuario['nome']}<br><br>"
        f"<b>CPF:</b> {usuario['cpf']}<br><br>"
        f"<b>Cargo:</b> {usuario['cargo']}<br><br>"
        f"<b>E-mail:</b> {usuario['email']}<br><br>"
        f"<b>Tipo de Usuário:</b> {usuario['tipo_usuario']}<br><br>"
        f"<b>Login:</b> {usuario['login']}<br><br>"
    )
    text_edit.setFixedSize(400, 300)  #tamanho do campo de informacoes
    layout.addWidget(text_edit)

    close_button = QPushButton("Close", dialog)
    layout.addWidget(close_button)
    close_button.clicked.connect(dialog.accept)

    dialog.exec_()

#exibe as informações do pet em um pop up
def show_pet_info_popup(pet):
    dialog = QDialog()
    dialog.setWindowTitle("Sistema de Cadastros")
    dialog.setFixedSize(422, 375)  #tamanho fixo do popup

    layout = QVBoxLayout(dialog)

    title_label = QLabel("<b>INFORMAÇÕES DO PET</b>")
    layout.addWidget(title_label)

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setHtml(
        f"<b>ID:</b> {pet['id']}<br><br>"
        f"<b>Nome:</b> {pet['nome_pet']}<br><br>"
        f"<b>Raça:</b> {pet['raca']}<br><br>"
        f"<b>Cor:</b> {pet['cor']}<br><br>"
        f"<b>Peso:</b> {pet['peso']}<br><br>"
        f"<b>Sexo:</b> {pet['sexo']}<br><br>"
        f"<b>Idade:</b> {pet['idade']}<br><br>"
        f"<b>Observações:</b> {pet['observacoes']}<br><br>"
        f"<b>Nome do Tutor:</b> {pet['nome_tutor']}<br><br>"
        f"<b>Tel. do Tutor:</b> {pet['telefone1']}<br><br>"
        f"<b>Endereço:</b> {pet['endereco']}<br><br>"
        f"<b>E-mail:</b> {pet['email']}<br><br>"
        f"<b>Nome - Contato de emergência:</b> {pet['nome_tutor2']}<br><br>"
        f"<b>Tel. - Contato de Emergência:</b> {pet['telefone2']}<br><br>"
    )
    text_edit.setFixedSize(400, 300)  #tamanho do campo de informacoes
    layout.addWidget(text_edit)

    close_button = QPushButton("Close", dialog)
    layout.addWidget(close_button)
    close_button.clicked.connect(dialog.accept)

    dialog.exec_()