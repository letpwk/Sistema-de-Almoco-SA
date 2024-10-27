#2° B Informática Vespertino
#Programação Orientada a Objetos
#Beatriz Souza da Rocha
#Danielly Magno Barbosa
#Letícia de Sousa e Silva
#Maria Luisa Lôbo Gutierrez

import random
from abc import ABC, abstractmethod


#método para gerar chave de acesso
def gerar_chave_acesso():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    chave = ""
    for _ in range(4):
        chave += random.choice(caracteres)
    return chave


#classe mãe
class Usuario(ABC):
    def __init__(self, nome, cpf:int, rg:int, naturalidade, email, senha, telefone:int):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__naturalidade = naturalidade
        self.__email = email
        self.__senha = senha  #atributo privado
        self.__telefone = telefone

    @abstractmethod
    def cadastro(self):
        pass
        
    def get_senha(self):
        return self.__senha
        
    def validar_login(self, senha):
        return self.__senha == senha

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha

    def set_telefone(self, telefone):
        self.__telefone = telefone

    #subclasse
    class ServidorDepae(Usuario):
        def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, setor):
            super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
            self.__matricula = matricula
            self._setor = setor
        
        def cadastro(self):
            print(f"\nServidor do Depae {self.get_nome()} cadastrado com sucesso!")

#subclasse
class Aluno(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, pai, mae, curso, turma_turno, serie):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self.__pai = pai
        self.__mae = mae
        self.__curso = curso
        self.__turma_turno = turma_turno
        self.__serie = serie
        self.__chave_acesso = gerar_chave_acesso() #gera a chave de acesso pro responsável

    def get_chave_acesso(self):
        return self.__chave_acesso

    def get_matricula(self):
        return self.__matricula
        
    def cadastro(self):
        print(f"\nAluno {self.get_nome()} cadastrado com sucesso!")
        print(f"Chave de acesso para o responsável: {self.get_chave_acesso()}")

#subclasse
class Responsavel(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, chave_acesso):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self.__chave_acesso = chave_acesso

    def cadastro(self):
        print(f"\nResponsável {self.get_nome()} cadastrado com sucesso.")

def criar_usuario(usuarios):
    print('\nComo você deseja se cadastrar?')
    print('1 - Aluno')
    print('2 - Responsável')
    tipo_usuario = input('Escolha o tipo de usuário: ')

    nome = input("\nNome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    naturalidade = input("Naturalidade: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Número de celular: ")

    if tipo_usuario == "1":
        matricula = input("Matrícula: ")
        pai = input("Pai: ")
        mae = input("Mãe: ")
        curso = input("Curso: ")
        turma_turno = input("Turma/Turno: ")
        serie = input("Série: ")
        aluno = Aluno(nome, cpf, rg, naturalidade, email, senha, telefone, matricula, pai, mae, curso, turma_turno, serie)
        usuarios.append(aluno)
        aluno.cadastro()

    elif tipo_usuario == "2":
        #verifica se há alunos cadastrados
        if not any(isinstance(usuario, Aluno) for usuario in usuarios):
            print("\nNão existem alunos cadastrados no sistema. Não é possível cadastrar um responsável.")
            return None
            
        matricula = input("Matrícula do aluno: ")
        chave_acesso = input("Chave de acesso fornecida pelo aluno: ")

        #verifica se a chave de acesso e a matrícula correspondem a algum objeto
        aluno_cadastrado = None
        for usuario in usuarios:
            if isinstance(usuario, Aluno) and usuario.get_matricula() == matricula and usuario.get_chave_acesso() == chave_acesso:
                aluno_cadastrado = usuario
                break

        if aluno_cadastrado:
            responsavel = Responsavel(nome, cpf, rg, naturalidade, email, senha, telefone, matricula, chave_acesso)
            usuarios.append(responsavel)
            responsavel.cadastro()
            return responsavel
        else:
            print("\nChave de acesso ou matrícula inválida.")
            return None

    else:
        print("\nTipo de usuário inválido.")
        return None


def set_login(usuarios):
    email = input("E-mail: ").strip()
    senha = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.get_email() == email and usuario.validar_login(senha):
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario.get_nome()} :)")
            return True

        
    print("Login falhou. E-mail ou senha incorretos.")
    return False

def menu(usuarios):
    usuarios = []
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario = criar_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)

        elif opcao == '2':
            set_login(usuarios)

        elif opcao == '3':
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


