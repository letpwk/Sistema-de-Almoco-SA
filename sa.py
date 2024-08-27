'''import random
from abc import ABC, abstractmethod, abstractmethod
from enum import Enum
#encapusulamento
#get
#set
#


class TipoUsuario(Enum):
    ESTUDANTE = "estudante"
    RESPONSAVEL = "responsavel"


class UsuariosDoIfro(ABC):
    number = random.randint(1, 10)

    def _init_(self, nome, email, cpf, senha, usuario):
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def cadastro(self):
        print('Cadastro de Usuários')
        print('--------------------')
        self.usuario = input('Usuário: ')
        self.nome = input('Nome:  ')
        self.email = input('Email: ')
        self.cpf = input('CPF: ')
        self.senha = input('Senha: ')

        
        #if usuario.usuario == self.usuario:
            #print('Erro: Usuário já cadastrado!')
            #return

    @abstractmethod
    def cadastro(self):
        pass

    def login(self):
        if self.usuario == self.usuario and self.senha == self.senha:
            print('Bem vindo,', self.nome)
            return True
        else:
            print('Erro: Usuário ou senha incorretos, digite novamente')
            return False


class Estudante(UsuariosDoIfro):

    def _init_(self, usuario, nome, email, cpf, senha, curso, turma, serie, pai, mae, telres):
        super()._init_(usuario, nome, email, cpf, senha)
        self.curso = curso
        self.turma = turma
        self.serie = serie
        self.pai = pai
        self.mae = mae
        self.telres = telres


def cadastro(self):
    super().cadastro()
    self.curso = input('Curso: ')
    self.turma = input('Turma: ')
    self.serie = input('Série: ')
    self.pai = input('Nome do Pai: ')
    self.mae = input('Nome da Mãe: ')
    self.telres = input('Telefone Residencial: ')


class Responsavel(UsuariosDoIfro):
    def _init_(self, usuario, nome, email, cpf, senha):
        super()._init_(usuario, nome, email, cpf, senha)
        self.chave = random.randint(1, 10)

    def cadastro(self):
        super().cadastro()
        self.chave = input('Chave de Acesso: ')

    def ChaveDeAcesso(self):
        chave = int(input('Insira a chave de acceso: '))
        if chave == self.chave:
            print('Seja bem-vindo,', self.nome)
        else:
            print('Chave de acesso incorreta, tente novamente.')
        return

    def get_login(self):
        return self.usuario and self.senha'''
        
        
        
from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, numero):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.naturalidade = naturalidade
        self.email = email
        self._senha = senha  # Atributo privado
        self.numero = numero

    @abstractmethod
    def cadastro(self):
        pass

    def validar_login(self, senha):
        return self._senha == senha


class Aluno(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, numero, matricula, pai, mae, curso, turma_turno, serie):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, numero)
        self.matricula = matricula
        self.pai = pai
        self.mae = mae
        self.curso = curso
        self.turma_turno = turma_turno
        self.serie = serie

    def cadastro(self):
        print(f"Aluno {self.nome} cadastrado com sucesso.")


class Responsavel(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, numero, matricula_aluno):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, numero)
        self.matricula_aluno = matricula_aluno

    def cadastro(self):
        print(f"Responsável {self.nome} cadastrado com sucesso.")


def criar_usuario():
    tipo_usuario = input("Você deseja cadastrar um aluno ou responsável? (aluno/responsável): ").strip().lower()

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    naturalidade = input("Naturalidade: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    numero = input("Número: ")

    if tipo_usuario == "aluno":
        matricula = input("Matrícula: ")
        pai = input("Pai: ")
        mae = input("Mãe: ")
        curso = input("Curso: ")
        turma_turno = input("Turma/Turno: ")
        serie = input("Série: ")
        usuario = Aluno(nome, cpf, rg, naturalidade, email, senha, numero, matricula, pai, mae, curso, turma_turno, serie)
    
    elif tipo_usuario == "responsável":
        matricula_aluno = input("Matrícula do aluno: ")
        usuario = Responsavel(nome, cpf, rg, naturalidade, email, senha, numero, matricula_aluno)
    
    else:
        print("Tipo de usuário inválido.")
        return None
    
    usuario.cadastro()
    return usuario


def login(usuarios):
    email = input("E-mail: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.email == email and usuario.validar_login(senha):
            print(f"Login bem-sucedido! Bem-vindo, {usuario.nome}.")
            return True

    print("Login falhou. E-mail ou senha incorretos.")
    return False


usuarios = []


def menu():
    while True:
        print("\n1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario = criar_usuario()
            if usuario:
                usuarios.append(usuario)
        
        elif opcao == '2':
            login(usuarios)
        
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


menu()

        