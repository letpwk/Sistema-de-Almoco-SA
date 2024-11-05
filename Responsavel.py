#Subclasse da super classe Usuario - Relacionamento de herança
import Usuario








class Responsavel(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, chave_acesso):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self.__chave_acesso = chave_acesso
        self.aluno = None

    def consultar_cronograma(self, aluno):
        return aluno.consultar_cronograma()

    def solicitar_troca(self, aluno, dia_novo):
        aluno.solicitar_troca(dia_novo)

    def definirAluno(self, aluno): 
        self.aluno = aluno  

    def get_matricula(self):
        return self.__matricula
    
    def get_chave_acesso(self):
        return self.__chave_acesso
    
    def visualizarInfo(self):
        return self.__info

    def cadastro(self):
        print(f"\nResponsável {self.get_nome()} cadastrado com sucesso.")

                            