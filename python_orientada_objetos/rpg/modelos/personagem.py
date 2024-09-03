from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, pontos_de_vida, defesa):
        self.nome = nome
        self.pontos_de_vida = pontos_de_vida
        self.defesa = defesa

    @abstractmethod
    def atacar(self):
        pass
