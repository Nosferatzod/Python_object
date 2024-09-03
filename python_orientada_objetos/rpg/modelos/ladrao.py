from modelos.personagem import Personagem

class Ladrao(Personagem):
    def __init__(self, nome, pontos_de_vida, defesa, agilidade):
        super().__init__(nome, pontos_de_vida, defesa)
        self.agilidade = agilidade

    def atacar(self):
        print(f"{self.nome} realiza um ataque furtivo, causando dano critico ao oponenete sem ele perceber!")
