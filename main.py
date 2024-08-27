#2° B Informática Vespertino
#Programação Orientada a Objetos
#Beatriz Souza da Rocha
#Danielly Magno Barbosa
#Letícia de Sousa e Silva
#Maria Luisa Lôbo Gutierrez

'''from sa import *
from sa import Estudante, Responsavel

usuarios = []

# Função para calcular o quadrado de um número
def calcular_quadrado(numero):
    return numero ** 2

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Calcula o quadrado do número
resultado = calcular_quadrado(numero)

# Exibe o resultado
print(f"O quadrado de {numero} é {resultado}")


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


    #aluno1 = Estudante(2023106060035, 'Juliana da Silva Costa', 'juliana@estudante.ifro.edu.br', 12345678910, 'jujuifiana', 'Informática', '2° ano Matutino', 'Roberval Costa Chaves', 'Marta da Silva Santos', '992343535')
    #aluno1.cadastro()
    #aluno1.login()

    estu = Estudante(None, None, None, None, None, None, None, None, None, None, None, None, None)
    estu.cadastro()
    estu.login()

    respo = Responsavel(None, None, None, None, None, None, None, None)
    respo.cadastro()
    estu.login()'''
    
from sa import Aluno, Responsavel, menu

# Lista para armazenar os usuários cadastrados
usuarios = []

# Instanciando 4 objetos da subclasse Aluno
aluno1 = Aluno("Alice", "12", "123", "Porto Velho", "alice@example.com", "senha123", "001", "001", "Pai de Alice", "Mãe de Alice", "Engenharia", "T1", "1º")
aluno2 = Aluno("Bruno", "23", "234", "Ji-Paraná", "bruno@example.com", "senha456", "002", "002", "Pai de Bruno", "Mãe de Bruno", "Matemática", "T2", "2º")
aluno3 = Aluno("Carla", "34", "345", "Ariquemes", "carla@example.com", "senha789", "003", "003", "Pai de Carla", "Mãe de Carla", "Física", "T3", "3º")
aluno4 = Aluno("Diego", "45", "456", "Cacoal", "diego@example.com", "senha101", "004", "004", "Pai de Diego", "Mãe de Diego", "Química", "T4", "4º")

# Instanciando 4 objetos da subclasse Responsavel       nome, cpf, email, matricula_aluno, chave_acesso
responsavel1 = Responsavel("Eduardo", "56", "eduardo@example.com", "001")
responsavel2 = Responsavel("Fernanda", "67", "fernanda@example.com", "002")
responsavel3 = Responsavel("Gabriela", "78", "gabriela@example.com", "003")
responsavel4 = Responsavel("Henrique", "89", "henrique@example.com", "004")

# Adicionando os objetos à lista de usuários
usuarios.extend([aluno1, aluno2, aluno3, aluno4, responsavel1, responsavel2, responsavel3, responsavel4])

# Executa o menu principal, passando a lista de usuários
if __name__ == "__main__":
    menu(usuarios)
