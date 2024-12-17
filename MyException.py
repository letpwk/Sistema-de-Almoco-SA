class MyException(Exception):
    pass
def verificar_senha(senha):
    if len(senha)< 7:
        raise MyException("A senha deve possuir pelo menos 7 caracteres")
    print("Senha válida.")

