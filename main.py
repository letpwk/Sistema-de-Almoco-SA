#2° B Informática Vespertino
#Programação Orientada a Objetos
#Beatriz Souza da Rocha
#Danielly Magno Barbosa
#Letícia de Sousa e Silva
#Maria Luisa Lôbo Gutierrez

from sa import Aluno, Responsavel, gerar_chave_acesso, menu

usuarios = []

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
