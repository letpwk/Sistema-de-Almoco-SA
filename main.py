#2° B Informática Vespertino
#Programação Orientada a Objetos
#Beatriz Souza da Rocha
#Danielly Magno Barbosa
#Letícia de Sousa e Silva
#Maria Luisa Lôbo Gutierrez

from Aluno import Aluno
from Responsavel import Responsavel
from ServidorDepae import ServidorDepae

usuarios = [] 

import random
def gerar_chave_acesso():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    chave = ""
    for _ in range(4):
        chave += random.choice(caracteres)
    return chave

def acharAluno_pelaMatricula(usuarios, matricula):
    #busca o aluno na lista de usuários pela matrícula
    for usuario in usuarios:
        if isinstance(usuario, Aluno) and usuario.get_matricula() == matricula:
            return usuario
    return None  #retorna None caso não encontre nenhum aluno com a matrícula informada

def criar_usuario(usuarios):
    print('\nComo você deseja se cadastrar?')
    print('1 - Aluno')
    print('2 - Responsável')
    try:
        tipo_usuario = input('Escolha o tipo de usuário: ')

        nome = input("\nNome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        naturalidade = input("Naturalidade: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        telefone = input("Número de celular: ")

        if tipo_usuario == "1":
            matricula = input("Matrícula: ")
            pai = input("Pai: ")
            mae = input("Mãe: ")
            curso = input("Curso: ")
            turma_turno = input("Turma/Turno: ")
            serie = input("Série: ")
            aluno = Aluno(nome, cpf, rg, naturalidade, email, senha, telefone, matricula, pai, mae, curso, turma_turno, serie)
            usuarios.append(aluno)
            aluno.cadastro()

        elif tipo_usuario == "2":
            #verifica se há alunos cadastrados
            if not any(isinstance(usuario, Aluno) for usuario in usuarios):
                print("\nNão existem alunos cadastrados no sistema. Não é possível cadastrar um responsável.")
                return None
                
            matricula = input("Matrícula do aluno: ")
            chave_acesso = input("Chave de acesso fornecida pelo aluno: ")

            #verifica se a chave de acesso e a matrícula correspondem a algum objeto
            aluno_cadastrado = None
            for usuario in usuarios:
                if isinstance(usuario, Aluno) and usuario.get_matricula() == matricula and usuario.get_chave_acesso() == chave_acesso:
                    aluno_cadastrado = usuario
                    break

            if aluno_cadastrado:
                responsavel = Responsavel(nome, cpf, rg, naturalidade, email, senha, telefone, matricula, chave_acesso)
                usuarios.append(responsavel)
                responsavel.cadastro()
                return responsavel
            else:
                print("\nChave de acesso ou matrícula inválida.")
                return None

        else:
            print("\nTipo de usuário inválido.")
            return None
    except ValueError:
        print('Opa! Este valor é inválido, digite aqui um número de 1 a 2, por favor: ')
    finally:
        print('Etapa de processar a troca do dia de almoço concluída!')


def set_login(usuarios):
    email = input("E-mail: ").strip()
    senha = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.get_email() == email and usuario.validar_login(senha):
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario.get_nome()} :)")
            return True

        
    print("Login falhou. E-mail ou senha incorretos.")
    return False

def menu(usuarios):
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Consultar Cronograma")
        print("4. Solicitar Troca de Almoço")
        print("5. Visualizar Solicitações DEPAE")
        print("6. Sair")
        try:
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                criar_usuario(usuarios)
            elif opcao == '2':
                set_login(usuarios)
            elif opcao == '3':
                consultar_cronograma(usuarios)
            elif opcao == '4':
                solicitar_troca(usuarios)
            elif opcao == '5':
                visualizar_solicitacoes_depae(usuarios)
            elif opcao == '6':
                print("\nSaindo do sistema...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
        except ValueError:
            print('Opa! Este valor é inválido, digite aqui um número de 1 a 6, por favor: ')
            

def consultar_cronograma(usuarios):
    aluno = set_login(usuarios)  #obtém o aluno logado
    if isinstance(aluno, Aluno):
        print(f"Seu cronograma de almoço é: {aluno.consultar_cronograma()}")
    else:
        print("Você não tem permissão para consultar o cronograma de almoço.")

def solicitar_troca(usuarios):
    aluno = set_login(usuarios)  #obtém o aluno logado
    if isinstance(aluno, Aluno):
        dia_novo = input("Digite o dia novo para a troca (Ex: Segunda-feira): ")
        aluno.solicitar_troca(dia_novo)
    else:
        print("Você não tem permissão para solicitar a troca de almoço.")

def visualizar_solicitacoes_depae(usuarios):
    servidor = set_login(usuarios)  #obtém o servidor logado
    
    if isinstance(servidor, ServidorDepae):  #verifica se o usuário logado é um servidor DEPAE
        matricula_aluno = input("Digite a matrícula do aluno para visualizar as solicitações de troca: ")
        aluno = acharAluno_pelaMatricula(usuarios, matricula_aluno)

        if aluno:
            #exibe as solicitações de troca de almoço do aluno
            print(f"Solicitações de troca de almoço do aluno {aluno.get_nome()}: {aluno.cronograma.solicitacoes}")
        else:
            print("Aluno não encontrado.")
    else:
        print("Você não tem permissão para visualizar as solicitações de troca de almoço.")



#instância dos 4 objetos da subclasse Aluno
aluno1 = Aluno("Beatriz", 12, 123, "Manaus", "bia@gmail.com", "senha789", 699963503, 2023106060034, "Bruno", "Adriana", "Informática", "Vespertino", "1")

aluno2 = Aluno("Danielly", 34, 345, "Belo Horizonte", "dany@gmail.com", "senha123", 69981636274, 2023106060057, "Jorge", "Joanilce", "Edificações", "Vespertino", "3")

aluno3 = Aluno("Letícia", 23, 234, "Rio de Janeiro", "let@gmail.com", "senha456", 69992894496, 2023106060052, "Willian", "Patrícia", "Eletrotécnica", "Matutino", "2")

aluno4 = Aluno("Maria Luisa", 45, 456, "Curitiba", "marial@gmail.com", "senha101", 69993986151, 2023106060062, "Nelson", "Maria", "Química", "Matutino", "1")

#instância dos 4 objetos da subclasse Responsável
gerar_chave_acesso()
responsavelbia = Responsavel("Adriana", 56, 567, "Porto Velho", "adriana@gmail.com", "senha102", 69001, 2023106060034, "1")

responsavellet = Responsavel("Patrícia", 67, 678, "Ji-Paraná", "patricia@gmail.com", "senha203", 69002, 2023106060057, "2")

responsaveldany = Responsavel("Joanilce", 78, 789, "Ariquemes", "joanilce@gmail.com", "senha304", 69003, 2023106060052, "3")

responsavelmalu = Responsavel("Maria", 89, 890, "Cacoal", "maria@gmail.com", "senha405", 69004, 2023106060062, "4")

#adicionando os usuários nas listas
usuarios.extend([aluno1, aluno2, aluno3, aluno4, responsavelbia, responsavellet, responsaveldany, responsavelmalu])

if __name__ == "__main__":
    menu(usuarios)