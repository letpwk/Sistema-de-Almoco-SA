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