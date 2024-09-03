class Curso:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.estudantes = []
        self.professores = []
    
    def adicionar_estudante(self, estudante):
        if estudante not in self.estudantes:
            self.estudantes.append(estudante)
            estudante.matricular(self)
    
    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def __str__(self):
        return f'Curso: {self.nome}, Carga Horária: {self.carga_horaria}'
