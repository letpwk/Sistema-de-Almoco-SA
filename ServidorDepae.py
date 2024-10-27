#subclasse
class ServidorDepae(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, setor):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone)
        self.__matricula = matricula
        self._setor = setor
        
    def cadastro(self):
        print(f"\nServidor do Depae {self.get_nome()} cadastrado com sucesso!")