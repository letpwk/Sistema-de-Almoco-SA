# Exceção criada para verficar a senha do usuário
class MinhaExceptionSenha(Exception):
    pass
def verificar_senha(senha):
    if len(senha)< 7:
        raise MinhaExceptionSenha("A senha deve possuir pelo menos 7 caracteres")
    print("Senha válida.")
