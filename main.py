#2° B Informática Vespertino
#Programação Orientada a Objetos
#Beatriz Souza da Rocha
#Danielly Magno Barbosa
#Letícia de Sousa e Silva
#Maria Luisa Lôbo Gutierrez

from sa import *
from sa import Estudante, Responsavel

usuarios = []

def menu(UsuariosDoIfro):
    print("Bem vindo ao sistema de cadastro do Instituto Federal de Rondônia!\n")

    print( 1, "- Sou aluno do IFRO")
    print('1 - Sou aluno do IFRO')
    print('2 - Sou responsável legal de um aluno do IFRO')
    opcao = input('Escolha a opção que melhor se encaixa:')
    if opcao == '1':
        estudante = Estudante()
        estudante.cadastro()
        
    elif opcao == '2':
        responsavel = Responsavel()
        responsavel.cadastro()
    else:
        print('Opção inválida! Tente novamente.')
        return


    aluno1 = Estudante(2023106060035, 'Juliana da Silva Costa', 'juliana@estudante.ifro.edu.br', 12345678910, 'jujuifiana', 'Informática', '2° ano Matutino', 'Roberval Costa Chaves', 'Marta da Silva Santos', '992343535')
    aluno1.cadastro()
    aluno1.login()

    '''estu = Estudante(None, None, None, None, None, None, None, None, None, None, None, None, None)
    estu.cadastro()
    estu.login()

    respo = Responsavel(None, None, None, None, None, None, None, None)
    respo.cadastro()
    estu.login()'''