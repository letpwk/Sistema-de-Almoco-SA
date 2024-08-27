import random
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

        for usuario in usuarios:
            if usuario.usuario == self.usuario:
                print('Erro: Usuário já cadastrado!')
                return

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

    def _init_(self, usuario, nome, email, cpf, senha, curso, turma, pai, mae, telres):
        super()._init_(usuario, nome, email, cpf, senha)
        self.curso = curso
        self.turma = turma
        self.serie = serie
        self.pai = pai
        self.mae = mae
        self.telres = telres


''' def cadastro(self):
    super().cadastro()
    self.curso = input('Curso: ')
    self.turma = input('Turma: ')
    self.serie = input('Série: ')
    self.pai = input('Nome do Pai: ')
    self.mae = input('Nome da Mãe: ')
    self.telres = input('Telefone Residencial: ')'''


class Responsavel(UsuariosDoIfro):
    def _init_(self, usuario, nome, email, cpf, senha, chave):
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
        return self.usuario and self.senha