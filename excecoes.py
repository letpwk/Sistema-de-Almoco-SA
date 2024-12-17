from Aluno import *

#criação da exceção para verificação de matrícula

class MatriculaInvalida(Exception):
    pass

def MatriculaVerific(matricula):
    if len(matricula) > 13 or len(matricula) < 13:
        raise MatriculaInvalida()
    elif not matricula.isdigit():
        raise MatriculaInvalida()
    elif len(matricula) == 13 and matricula.isdigit():
        print("Matrícula válida!")
        return True

   