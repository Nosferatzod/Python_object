from modelos.pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        # Dicionário sim fica mais fácil para armazenar cursos
        self.cursos = {}
    
    # Método para matricular o estudante em um curso
    def matricular(self, curso):
        # Verifica se o curso já está matriculado; se não estiver, adiciona ao dicionário
        if curso not in self.cursos:
            self.cursos[curso] = []
    
    # Método para adicionar uma nota a um curso específico
    def adicionar_nota(self, curso, nota):
        # Verifica se o estudante está matriculado no curso
        if curso in self.cursos:
            # Adiciona a nota à lista de notas do curso
            self.cursos[curso].append(nota)
        else:
            # Exibe uma mensagem de erro se o curso não estiver matriculado
            print("Estudante não matriculado neste curso.")
    
    def calcular_media(self, curso):
        # Verifica se o estudante está matriculado no curso e se há notas disponíveis senão ele papoca tudo
        if curso in self.cursos and len(self.cursos[curso]) > 0:
            return sum(self.cursos[curso]) / len(self.cursos[curso])
        # Retorna 0 se o curso não estiver matriculado ou não houver notas para não dar bronca
        return 0

    def __str__(self):
        # Retorna uma string formatada com o nome e a idade do estudante
        return f'Estudante: {self.nome}, Idade: {self.idade}'
