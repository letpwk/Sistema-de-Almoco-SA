
#subclasse
class ServidorDepae(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, setor, data, motivo, limiteTroca):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone, matricula)
        self._setor = setor
        self._data = data
        self._motivo = motivo
        self._limiteTroca = limiteTroca

    def consultarData(self):
        print(f'Data do seu almoço liberado:{self.data}')
        return self.data

    def consultarMotivo(self):
        print(f'Motivo do seu almoço liberado hoje: {self.motivo}')
        return self.motivo   

    def consultarLimiteTroca(self):  
         print(f'Quantidade de trocas restantes: {self.limiteTroca}')
         return self.limiteTroca


    def autorizarSolicitacao(self):
        print('Você gostaria de autorizar solicitação?')
        print('1 - Sim')
        print('2 - Não')
        solici = input('Digite aqui: ')

        if solici == 1:
            print('Troca realizada com sucesso')

        elif solici == 2:
            print('Troca não autorizada')


     




        
    def cadastro(self):
        print(f"\nServidor do Depae {self.get_nome()} cadastrado com sucesso!")