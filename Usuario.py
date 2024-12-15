#Classe Mãe - Relacionamento de Herança
from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone):
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

