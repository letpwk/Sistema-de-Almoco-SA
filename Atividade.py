# - Relacionamento de agregação da classe todo Cronograma e da classe parte Atividade
class Atividade:
    def __init__(self, tipoAtividade, professor, horarioAtiv, dataInicio, dataFim, diaSemana):
        self.tipoAtividade = tipoAtividade
        self.professor = professor
        self.horarioAtiv = horarioAtiv
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.diaSemana = diaSemana

    def consultarAtividade(self):
        print(f"Atividade executada pelo discente: {self.tipoAtividade()}")

    def consultarProfessor(self):
        print(f"Professor responsável pela atividade: {self.professor()}")
    
    def consultarHorarioAtiv(self):
        print(f"Horário da atividade: {self.horarioAtiv()}")

    def consultarDataInicio(self):
        print(f"Data de início da atividade: {self.dataInicio()}")

    def consultarDataFim(self):
        print(f"Data de fim da atividade: {self.dataFim()}")

    def consultarDiaSemana(self):
        print(f"Dia da semana em que a atividade ocorre: {self.diaSemana()}")