from Atividade import *

class Cronograma:
    def __init__(self, motivo, limiteTroca, cronograma):
        self.motivo = motivo
        self.limiteTroca = limiteTroca
        self.cronograma = cronograma
        self.solicitacoes = []  # Armazena as solicitações de troca de almoço
        #Relacionamento de agregação da classe todo Cronograma e da classe parte Atividade
        self.atividade = Atividade()

    def consultarMotivo(self):
        print(f'Motivo do seu almoço liberado hoje: {self.motivo}')
        return self.motivo
    
    def consultarLimiteTroca(self):
        print(f'Quantidade de trocas restantes: {self.limiteTroca}')
        return self.limiteTroca
    
    def solicitarTrocaAlmoco(self, dia_novo):
        if dia_novo not in self.cronograma:
            print("Esse dia já foi reservado para outra atividade.")
        else:
            self.solicitacoes.append(dia_novo)
            print(f"Solicitação de troca para {dia_novo} foi registrada.")

    
    def consultarCronograma(self):
        print('Dias da semana')
        print('1 - Segunda-feira')
        print('2 - Terça-feira')
        print('3 - Quarta-feira')
        print('4 - Quinta-feira')
        print('5 - Sexta-feira')
        return self.cronograma
    
    def solicitarTrocaAlmoco(self):
        while True: 
            print('Você gostaria de alterar o dia de almoço?')
            print('1 - Sim')
            print('2 - Não')
            try:
                troca = input('Digite aqui: ')
            except ValueError:
                print("Inválido! Digite o valor correto:")

            if troca == '1':  
                self.consultarCronograma() 
                while True:
                    try:
                        diaAdicionado = int(input('Selecione o dia da semana que deseja adicionar:\n1 - Segunda-feira\n2 - Terça-feira\n3 - Quarta-feira\n4 - Quinta-feira\n5 - Sexta-feira\nDigite aqui: '))
                        if diaAdicionado == 1:
                            print('Segunda-feira adicionado!')
                            break
                        elif diaAdicionado == 2:
                            print('Terça-feira adicionado!')
                            break
                        elif diaAdicionado == 3:
                            print('Quarta-feira adicionado!')
                            break
                        elif diaAdicionado == 4:
                            print('Quinta-feira adicionado!')
                            break
                        elif diaAdicionado == 5:
                            print('Sexta-feira adicionado!')
                            break
                        else:
                            print('Número inválido! Por favor, digite novamente:')
                    except ValueError:
                        print('Número inválido! Por favor, digite novamente:')

                while True:
                    try:
                        diaRemovido = int(input('Selecione o dia da semana que deseja remover:\n1 - Segunda-feira\n2 - Terça-feira\n3 - Quarta-feira\n4 - Quinta-feira\n5 - Sexta-feira\nDigite aqui: '))
                        if diaRemovido == 1:
                            print('Segunda-feira removido!')
                            break
                        elif diaRemovido == 2:
                            print('Terça-feira removido!')
                            break
                        elif diaRemovido == 3:
                            print('Quarta-feira removido!')
                            break
                        elif diaRemovido == 4:
                            print('Quinta-feira removido!')
                            break
                        elif diaRemovido == 5:
                            print('Sexta-feira removido!')
                            break
                        else:
                            print('Número inválido! Por favor, digite novamente:')
                    except ValueError:
                        print('Número inválido! Por favor, digite novamente:')
                
                break 

            elif troca == '2': 
                print('Você optou por não alterar o dia de almoço.')
                break  

            else:
                print('Número inválido! Por favor, digite novamente:')
