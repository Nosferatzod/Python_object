from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    @property
    def carros(self):
        base_str = super().__str__()
        return f'{base_str} - Portas: {self.portas}'
