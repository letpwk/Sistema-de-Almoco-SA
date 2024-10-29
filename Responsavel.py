#subclasse
class Responsavel(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, chave_acesso):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self.__chave_acesso = chave_acesso

    def visualizarInfo(self):
        return self.__info

    
    def cadastro(self):
        print(f"\nResponsável {self.get_nome()} cadastrado com sucesso.")
