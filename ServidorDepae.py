from Usuario import Usuario
from main import *

#Subclasse da super classe Usuario 

# - Relacionamento de herança com a super classe Usuario
class ServidorDepae(Usuario):
    def __init__(self, nome, cpf, rg, naturalidade, email, senha, telefone, matricula, setor, data, motivo, limiteTroca):
        super().__init__(nome, cpf, rg, naturalidade, email, senha, telefone, matricula)
        self._setor = setor
        self._data = data
        self._motivo = motivo
        self._limiteTroca = limiteTroca
        self.cronograma = None
        self.solicitacoes = [] # Lista para armazenar as soliçitaçoes de troca de almoço

    def consultar_solicitacoes(self):
        return self.solicitacoes
    
    def visualizar_solicitacoes_depae(usuarios):
        servidor = set_login(usuarios)  
    
        if isinstance(servidor, ServidorDepae):  
            matricula_aluno = input("Digite a matrícula do aluno para visualizar as solicitações de troca: ")
            aluno = find_aluno_by_matricula(usuarios, matricula_aluno)  

            if aluno:
                # Exibe as solicitações de troca de almoço do aluno
                print(f"Solicitações de troca de almoço do aluno {aluno.get_nome()}: {aluno.cronograma.solicitacoes}")
            else:
                print("Aluno não encontrado.")
        else:
            print("Você não tem permissão para visualizar as solicitações de troca de almoço.")


    def definirCronograma(self, cronograma): 
        self.cronograma = cronograma  

# - Relacionamento de associação entre a classe ServidorDepae e a classe Cronograma
    def consultarData(self):
        print(f'Data do seu almoço liberado:{self.data}')
        return self.data

    def consultarMotivo(self):
        print(f'Motivo do seu almoço liberado hoje: {self.motivo}')
        return self.motivo   

    def consultarLimiteTroca(self):  
         print(f'Quantidade de trocas restantes: {self.limiteTroca}')
         return self.limiteTroca

    def autorizar_solicitacao(self, aluno, dia_novo):
        if dia_novo in aluno.cronograma.consultarCronograma():
            print(f"Solicitação de troca para {dia_novo} do aluno {aluno.get_nome()} autorizada.")
            aluno.cronograma.cronograma.append(dia_novo)
            aluno.cronograma.solicitacoes.remove(dia_novo)
        else:
            print(f"Solicitação de troca para {dia_novo} do aluno {aluno.get_nome()} negada.")

        
    def cadastro(self):
        print(f"\nServidor do Depae {self.get_nome()} cadastrado com sucesso!")