class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def __str__(self):
        return f'Nome: {self.nome}, Preço Unitário: {self.preco_unitario:.2f}, Quantidade: {self.quantidade}'
