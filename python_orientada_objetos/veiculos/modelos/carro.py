from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str):
        super().__init__(marca, modelo)
        self.cor = cor
    
    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} está ligado.")
