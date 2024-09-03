class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def populacao_total(self):
        return sum(cidade.populacao for cidade in self.cidades)

def main():
    cidade1 = Cidade("Xique - Xique", 150000)
    cidade2 = Cidade("Salvador", 10000)
    cidade3 = Cidade("Aracaju", 5000)
    cidade4 = Cidade("Lagoas", 400000)
    cidade5 = Cidade("São José dos Campos", 520000)
    cidade6 = Cidade("Campinas", 60000)

    estado1 = Estado("Bahia", "BA")
    estado2 = Estado("Sergipe", "SE")
    estado3 = Estado("São Paulo", "SP")

    estado1.adicionar_cidade(cidade1)
    estado1.adicionar_cidade(cidade2)
    
    estado2.adicionar_cidade(cidade3)
    estado2.adicionar_cidade(cidade4)
    
    estado3.adicionar_cidade(cidade5)
    estado3.adicionar_cidade(cidade6)

    for estado in [estado1, estado2, estado3]:
        print(f"Estado: {estado.nome} ({estado.sigla})")
        print(f"População total: {estado.populacao_total()}")
        print()

if __name__ == "__main__":
    main()
