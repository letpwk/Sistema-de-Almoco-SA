#Subclasse da super classe Usuario
# - Relacionamento de herança com a super classe Usuario
# - Relacionamento de associação com a subclasse Responsavel


from Usuario import *
from Cronograma import Cronograma

#método para gerar chave de acesso
import random
def gerar_chave_acesso():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    chave = ""
    for _ in range(4):
        chave += random.choice(caracteres)
    return chave

class Aluno(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, pai, mae, curso, turma_turno, serie):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self.__pai = pai
        self.__mae = mae
        self.__curso = curso
        self.__turma_turno = turma_turno
        self.__serie = serie
        self.__chave_acesso = gerar_chave_acesso() 
        self.cronograma = Cronograma() 

    def consultar_cronograma(self):
        return self.cronograma.consultarCronograma()

    def solicitar_troca(self, dia_novo):
        if self.cronograma.limiteTroca > 0:
            self.cronograma.solicitarTrocaAlmoco(dia_novo)
            self.cronograma.limiteTroca -= 1
        else:
            print("Limite de trocas atingido+-.")

        # - Relacionamento de agregação da classe todo Aluno e da classe parte Cronograma
        self.cronograma = Cronograma()

    def get_chave_acesso(self):
        return self.__chave_acesso

    def get_matricula(self):
        return self.__matricula

    def visualizarInfo(self):
        return self.__info    
        
    def cadastro(self):
        print(f"\nAluno {self.get_nome()} cadastrado com sucesso!")
        print(f"Chave de acesso para o responsável: {self.get_chave_acesso()}") 

        