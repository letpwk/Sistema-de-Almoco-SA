class Matricula(Exception):
    pass

def verificar_matricula(matricula):
    if len(matricula) > 13 or len(matricula) < 13:
        raise Matricula()
    
    elif not matricula.isdigit():
        raise Matricula()
    
    elif len(matricula) == 13 and matricula.isdigit():
        print("Matrícula cadastrada comm sucesso!")
        return True