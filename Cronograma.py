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
        print('Dias da semana')
        print('1 - Segunda-feira')
        print('2 - Terça-feira')
        print('3 - Quarta-feira')
        print('4 - Quinta-feira')
        print('5 - Sexta-feira')
        return self.cronograma
    
    def solicitarTrocaAlmoco(self):
        print('Você gostaria de alterar o dia de almoço?')
        print('1 - Sim')
        print('2 - Não')
        troca = input('Digite aqui: ')

        if troca == 1:
            self.consultarCronograma()

            #para escolher o dia pelo qual quer trocar
            diaAdicionado = input('Selecione o dia da semana que deseja adicionar: ')

            if diaAdicionado == 1:
                print('Segunda-feira adicionado!')
            elif diaAdicionado == 2:
                print('Terça-feira adicionado!')
            elif diaAdicionado == 3:
                print('Quarta-feira adicionado!')
            elif diaAdicionado == 4:
                print('Quinta-feira adicionado!')
            elif diaAdicionado == 5:
                print('Sexta-feira adicionado!')
            else:
                print('Número inválido, digite novamente.')


            #para escolher o dia que ja tem almoço
            diaRemovido = input('Selecione o dia da semana que deseja remover: ') #como utilizar set aqui? #self.diaSemana?
            
            if diaRemovido == 1:
                print('Segunda-feira removido!')
            elif diaRemovido == 2:
                print('Terça-feira removido!')
            elif diaRemovido == 3:
                print('Quarta-feira removido!')
            elif diaRemovido == 4:
                print('Quinta-feira removido!')
            elif diaRemovido == 5:
                print('Sexta-feira removido!')
            else:
                print('Número inválido, digite novamente.') #adicionar loop dos dias

                

            
    
