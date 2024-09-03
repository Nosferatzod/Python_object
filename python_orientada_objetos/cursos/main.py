from modelos.gerenciador import Gerenciador

def main():
    gerenciador = Gerenciador()

    #______________CURSOS______________
    curso_math = gerenciador.adicionar_curso("Matemática Básica", 24)
    curso_prog = gerenciador.adicionar_curso("Programação em Python", 8)
    curso_historia = gerenciador.adicionar_curso("História", 90)
    #______________ALUNO______________
    ju = gerenciador.adicionar_estudante("ju", 17)
    bibi = gerenciador.adicionar_estudante("Bibi", 16)
    arthuro = gerenciador.adicionar_estudante("Arthuro", 21)

    #______________PROFESSORES______________
    prof_diego = gerenciador.adicionar_professor("Diego", 39)
    prof_lenon = gerenciador.adicionar_professor("Lenon", 25)
    prof_kaua = gerenciador.adicionar_professor("Kauã", 20)

    #______________MATRICULA______________
    curso_math.adicionar_estudante(ju)
    curso_prog.adicionar_estudante(bibi)
    curso_historia.adicionar_estudante(bibi)
    curso_historia.adicionar_estudante(arthuro)

    #______________ADICIONAR PROFESSORES NOS CURSOS______________
    prof_diego.adicionar_curso(curso_math)
    prof_lenon.adicionar_curso(curso_prog)
    prof_kaua.adicionar_curso(curso_historia)

    #______________ADICIONAR NOTAS______________
    ju.adicionar_nota(curso_math, 4.5)
    ju.adicionar_nota(curso_math, 5.0)
    bibi.adicionar_nota(curso_prog, 9.0)
    bibi.adicionar_nota(curso_prog, 10.0)
    bibi.adicionar_nota(curso_historia, 9.0)
    arthuro.adicionar_nota(curso_historia, 7.0)

    gerenciador.gerar_relatorios()

if __name__ == "__main__":
    main()
