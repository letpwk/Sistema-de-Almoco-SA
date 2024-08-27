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
        
        
import random
import string
from abc import ABC, abstractmethod

# Função para gerar uma chave de acesso aleatória
def gerar_chave_acesso():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Superclasse abstrata
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

# Subclasse Aluno
class Aluno(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, numero, matricula, pai, mae, curso, turma_turno, serie):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, numero)
        self.matricula = matricula
        self.pai = pai
        self.mae = mae
        self.curso = curso
        self.turma_turno = turma_turno
        self.serie = serie
        self.chave_acesso = gerar_chave_acesso()  # Gerar e atribuir chave de acesso

    def cadastro(self):
        print(f"Aluno {self.nome} cadastrado com sucesso.")
        print(f"Chave de acesso para o responsável: {self.chave_acesso}")

# Subclasse Responsavel   usuario, nome, email, cpf, senha
class Responsavel(Usuario):
    def __init__(self, nome, cpf, email, matricula_aluno, chave_acesso):
        super().__init__(nome, cpf, email)
        self.matricula_aluno = matricula_aluno
        self.chave_acesso = chave_acesso

    def cadastro(self):
        print(f"Responsável {self.nome} cadastrado com sucesso.")

# Função para criar usuários (Alunos e Responsáveis)
def criar_usuario(usuarios):
    print('Como você deseja se cadastrar?')
    print('1 - Aluno')
    print('2 - Responsável')
    tipo_usuario = input('Escolha o tipo de usuário: ')

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    naturalidade = input("Naturalidade: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    numero = input("Número: ")

    if tipo_usuario == "1":
        matricula = input("Matrícula: ")
        pai = input("Pai: ")
        mae = input("Mãe: ")
        curso = input("Curso: ")
        turma_turno = input("Turma/Turno: ")
        serie = input("Série: ")
        usuario = Aluno(nome, cpf, rg, naturalidade, email, senha, numero, matricula, pai, mae, curso, turma_turno, serie)
        print(f"Chave de acesso gerada para o responsável: {usuario.chave_acesso}")
    
    elif tipo_usuario == "2":
        matricula_aluno = input("Matrícula do aluno: ")
        chave_acesso = input("Chave de acesso fornecida pelo aluno: ")
        
        # Verifica se a chave de acesso é válida
        aluno_cadastrado = next((u for u in usuarios if isinstance(u, Aluno) and u.chave_acesso == chave_acesso and u.matricula == matricula_aluno), None)
        
        if aluno_cadastrado:
            usuario = Responsavel(nome, cpf, rg, naturalidade, email, senha, numero, matricula_aluno, chave_acesso)
        else:
            print("Chave de acesso ou matrícula inválida.")
            return None
    
    else:
        print("Tipo de usuário inválido.")
        return None
    
    usuario.cadastro()
    return usuario

# Função de login
def login(usuarios):
    email = input("E-mail: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.email == email and usuario.validar_login(senha):
            print(f"Login bem-sucedido! Bem-vindo, {usuario.nome}.")
            return True

    print("Login falhou. E-mail ou senha incorretos.")
    return False

# Função do menu
def menu(usuarios):
    while True:
        print("\n1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario = criar_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)
        
        elif opcao == '2':
            login(usuarios)
        
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
