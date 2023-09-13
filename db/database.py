import sqlite3
import bcrypt
import os

#***CLASSE DATABSE***
class DataBase():

    #cria conexao
    def __init__(self, name="system.db"):
        db_folder = "db"
        self.name = os.path.join(db_folder, name)
        self.connection = None

    #conecta
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
    
    #fecha conexao
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    #DEFS

    #usuarios - cria tabela
    def create_tab_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(70) NOT NULL,
                    cpf VARCHAR(14) NOT NULL,
                    cargo VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    tipo_usuario VARCHAR(20) NOT NULL,
                    login VARCHAR(20) UNIQUE NOT NULL,
                    senha VARCHAR(20) NOT NULL
                );
            """)
        except AttributeError:
            print("faça a conexao")

    #pets - cria tabela
    def create_tab_pets(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_pet VARCHAR(50) NOT NULL,
                    raca VARCHAR(50) NOT NULL,
                    cor VARCHAR(30) NOT NULL,
                    peso VARCHAR(10) NOT NULL,
                    sexo VARCHAR(10) NOT NULL,
                    idade VARCHAR(30) NOT NULL,
                    observacoes VARCHAR(700),
                    nome_tutor VARCHAR(70) NOT NULL,
                    telefone1 VARCHAR(20) NOT NULL,
                    endereco VARCHAR(200) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    nome_tutor2 VARCHAR(70) NOT NULL,
                    telefone2 VARCHAR(20) NOT NULL
                );
            """)
        except AttributeError:
            print("faça a conexao")
    
    #usuarios - insere usuario
    def insert_usuario(self, nome, cpf, cargo, email, tipo_usuario, login, senha):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO usuarios(nome, cpf, cargo, email, tipo_usuario, login, senha) VALUES (?,?,?,?,?,?,?)
                """, (nome, cpf, cargo, email, tipo_usuario, login, senha))
        except AttributeError:
            print("Faça a conexão")

    #pets - insere pet
    def insert_pet(self, nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO pets(nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2))
        except sqlite3.OperationalError as e:
            print(f"Erro ao inserir o pet: {e}")
        except AttributeError:
            print("Faça a conexão")
            
    #usuarios - verifica login e senha, e retorna tipo de usuario
    def check_user(self, login, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuarios")                           
            for linha in cursor.fetchall():
                print("Linha:", linha)
                if linha[6].upper() == login.upper() and bcrypt.checkpw(senha.encode(), linha[7].encode()) and linha[5] == "Administrador":
                    return "Administrador"
                elif linha[6].upper() == login.upper() and bcrypt.checkpw(senha.encode(), linha[7].encode()) and linha[5] == "Comum":
                    return "Comum"
                else:
                    continue
            return "sem acesso"
        except Exception as e:
            print("Erro:", e)

    #usuarios - atualiza usuario
    def update_usuario(self, id_usuario, nome, cpf, cargo, email, tipo_usuario, login, senha):
        try:
            cursor = self.connection.cursor()
            # Corrigindo a consulta SQL e o uso dos parâmetros
            cursor.execute("""
                UPDATE usuarios 
                SET nome = ?, cpf = ?, cargo = ?, email = ?, tipo_usuario = ?, login = ?, senha = ? 
                WHERE id = ?""",
                (nome, cpf, cargo, email, tipo_usuario, login, senha, id_usuario)
            )
            self.connection.commit()
        except Exception as e:
            print("Erro ao atualizar o usuário:", e)

    #pets - atualiza pet
    def update_pet(self, id_pet, nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2):
        try:
            cursor = self.connection.cursor()
            # Corrigindo a consulta SQL e o uso dos parâmetros
            cursor.execute("""
                UPDATE pets 
                SET nome_pet = ?, raca = ?, cor = ?, peso = ?, sexo = ?, idade = ?, observacoes = ?, 
                nome_tutor = ?, telefone1 = ?, endereco = ?, email = ?, nome_tutor2 = ?, telefone2 = ? 
                WHERE id = ?""",
                (nome_pet, raca, cor, peso, sexo, idade, observacoes, nome_tutor, telefone1, endereco, email, nome_tutor2, telefone2, id_pet)
            )
            self.connection.commit()
        except Exception as e:
            print("Erro ao atualizar o pet:", e)

    #usuarios - remove usuario
    def remover_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_usuario,))
        self.connection.commit()

    #pets - remove pet
    def remover_pet(self, id_pet):
        try:
            query = "DELETE FROM pets WHERE id = ?"
            cursor = self.connection.cursor()
            cursor.execute(query, (id_pet,))
            self.connection.commit()
        except Exception as e:
            print("Erro ao remover o pet:", e)

    #usuarios - recupera informacoes do usuario com base no id
    def get_usuario(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_usuario,))
        result = cursor.fetchone()

        if result:
            column_names = [description[0] for description in cursor.description]
            usuario = dict(zip(column_names, result))
            return usuario

        return None
    
    #pets - recupera informações do pet com base no id
    def get_pet(self, id_pet):
        query = "SELECT * FROM pets WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_pet,))
        result = cursor.fetchone()

        if result:
            column_names = [description[0] for description in cursor.description]
            pet = dict(zip(column_names, result))
            return pet

        return None

    #usuarios - verifica se o login já é utilizado
    def is_login_used(self, login, exclude_user_id=None):
        query = "SELECT COUNT(*) FROM usuarios WHERE login = ?"
        params = (login,)

        if exclude_user_id is not None:
            query += " AND id != ?"
            params += (exclude_user_id,)

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()

        return result[0] > 0

if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_tab_pets()
    db.create_tab_usuarios()
    db.close_connection()
