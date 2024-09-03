from modelos.guerreiro import Guerreiro
from modelos.mago import Mago
from modelos.ladrao import Ladrao

def testar_personagens():
    guerreiro = Guerreiro(nome="Elden Lord", pontos_de_vida=150, defesa=50, arma="Excalibur")
    mago = Mago(nome="Gandalf", pontos_de_vida=100, defesa=30, mana=200)
    ladrao = Ladrao(nome="Frodo", pontos_de_vida=80, defesa=20, agilidade=70)

    personagens = [guerreiro, mago, ladrao]
    for p in personagens:
        p.atacar()

if __name__ == "__main__":
    testar_personagens()
