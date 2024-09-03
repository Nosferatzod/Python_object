from modelos.personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome, pontos_de_vida, defesa, mana):
        super().__init__(nome, pontos_de_vida, defesa)
        self.mana = mana

    def atacar(self):
        print(f"{self.nome} lança um feitiço de fogo, deixa seu inimigo em chamas!")
