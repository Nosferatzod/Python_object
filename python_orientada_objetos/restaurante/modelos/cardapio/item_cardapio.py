from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        pass
    
    @abstractmethod
    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}"




