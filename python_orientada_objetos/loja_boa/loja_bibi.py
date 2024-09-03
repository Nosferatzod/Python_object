class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def __str__(self):
        return f'Nome: {self.nome}, Preço Unitário: {self.preco_unitario:.2f}, Quantidade: {self.quantidade}'

produtos = []

def cadastrar_produto(nome, preco_unitario, quantidade):
    produto = Produto(nome, preco_unitario, quantidade)
    produtos.append(produto)

def listar_produtos():
    for produto in produtos:
        print(produto)

def calcular_valor_total_estoque():
    valor_total = sum(p.preco_unitario * p.quantidade for p in produtos)
    return round(valor_total, 2)

def quantidade_produtos():
    return len(produtos)

def main():
    cadastrar_produto("Leite", 10.50, 4)
    cadastrar_produto("Biscoito", 5.75, 3)
    cadastrar_produto("Sorvete", 20.00, 5)


    print("Lista de Produtos:")
    listar_produtos()

    valor_total = calcular_valor_total_estoque()
    print(f"\nValor Total do Estoque: R$ {valor_total:.2f}")

    total_produtos = quantidade_produtos()
    print(f"\nQuantidade Total de Produtos: {total_produtos}")
if __name__ == "__main__":
    main()