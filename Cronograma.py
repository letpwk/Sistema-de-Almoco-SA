class Cronograma():
    def __init__(self, motivo, limiteTroca, cronograma):
        self.motivo = motivo
        self.limiteTroca = limiteTroca
        self.cronograma = cronograma

    def consultarMotivo(self):
        print(f'Motivo do seu almoço liberado hoje: {self.motivo}')
        return self.motivo
    
    def consultarLimiteTroca(self):
        print(f'Quantidade de trocas restantes: {self.limiteTroca}')
        return self.limiteTroca
    
    def consultarCronograma(self):
        print(f'{self.cronograma}')
        return self.cronograma
    
    def solicitarTrocaAlmoco(self):
        print('Você gostaria de alterar o dia de almoço?')
        print('1 - Sim')
        print('2 - Não')
        troca = input('Digite aqui: ')

        if troca == 1:
            print('Dias da semana')
            print('1 - Segunda-feira')
            print('2 - Terça-feira')
            print('3 - Quarta-feira')
            print('4 - Quinta-feira')
            print('5 - Sexta-feira')
            dia = input('Selecione o dia da semana que deseja trocar: ') #como utilizar set aqui? #self.diaSemana?
            
            if dia == 1:
                print('Segunda-feira selecionado!')
            elif dia == 2:
                print('Terça-feira selecionado!')
            elif dia == 3:
                print('Quarta-feira selecionado!')
            elif dia == 4:
                print('Quinta-feira selecionado!')
            elif dia == 5:
                print('Sexta-feira selecionado!')
            else:
                print('Número inválido, digite novamente.') #adicionar loop dos dias

            

            
    
