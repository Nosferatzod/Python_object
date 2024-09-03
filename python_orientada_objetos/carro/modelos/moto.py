from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    @property
    def motos(self):
        base_str = super().__str__()
        return f'{base_str} - Tipo: {self.tipo}'
