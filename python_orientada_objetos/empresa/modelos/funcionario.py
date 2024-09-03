from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def aplicar_bonificacao(self, valor):
        pass

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id}, Salário: R${self.calcular_salario():.2f}"
