from modelos.curso import Curso
from modelos.estudante import Estudante
from modelos.professor import Professor

class Gerenciador:
    def __init__(self):
        self.cursos = []
        self.estudantes = []
        self.professores = []
    #_______________CURSO_______________
    def adicionar_curso(self, nome, carga_horaria):
        curso = Curso(nome, carga_horaria)
        # Adiciona o curso à lista de cursos
        self.cursos.append(curso)
        return curso
    #_______________ESTUDANTE_______________
    def adicionar_estudante(self, nome, idade):
        estudante = Estudante(nome, idade)
        self.estudantes.append(estudante)
        return estudante
    
    #_______________PROFESSOR_______________
    def adicionar_professor(self, nome, idade):
        professor = Professor(nome, idade)
        self.professores.append(professor)
        return professor
    
    def gerar_relatorios(self):
        # Cria relatórios convertendo os objetos em strings para cursos, estudantes e professores
        #Além de que isso muda todos os vetores para strings
        relatorio_cursos = [str(curso) for curso in self.cursos]
        relatorio_estudantes = [str(estudante) for estudante in self.estudantes]
        relatorio_professores = [str(professor) for professor in self.professores]
        
        print("Relatório de Cursos:")
        print("\n".join(relatorio_cursos))
        
        print("\nRelatório de Estudantes:")
        print("\n".join(relatorio_estudantes))
        
        print("\nRelatório de Professores:")
        print("\n".join(relatorio_professores))
        
        print("\nRelatório de Notas:")
        for estudante in self.estudantes:
            print(f"Notas de {estudante.nome}:")
            for curso in estudante.cursos:
                # Calcular a média das notas do estudante em cada curso
                media = estudante.calcular_media(curso)
                print(f"{curso.nome}: Média = {media:.2f}")
