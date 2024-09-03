from modelos.personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, pontos_de_vida, defesa, arma):
        super().__init__(nome, pontos_de_vida, defesa)
        self.arma = arma

    def atacar(self):
        print(f"{self.nome} ataca com sua espada {self.arma}, causando muito dano ao oponete que chega a morrer!")
