from modelos.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.cursos = []
    
    def adicionar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.adicionar_professor(self)

    def __str__(self):
        return f'Professor: {self.nome}, Idade: {self.idade}'
