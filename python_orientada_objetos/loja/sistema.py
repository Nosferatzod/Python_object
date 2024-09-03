from produto import Produto

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

if __name__ == "__main__":
    cadastrar_produto("Produto A", 10.50, 20)
    cadastrar_produto("Produto B", 5.75, 15)
    cadastrar_produto("Produto C", 20.00, 10)

    print("Lista de Produtos:")
    listar_produtos()

    valor_total = calcular_valor_total_estoque()
    print(f"\nValor Total do Estoque: R$ {valor_total:.2f}")

    total_produtos = quantidade_produtos()
    print(f"\nQuantidade Total de Produtos: {total_produtos}")
    
def remover_produto(nome):
    global produtos
    produtos = [p for p in produtos if p.nome != nome]

def atualizar_preco(nome, novo_preco):
    for produto in produtos:
        if produto.nome == nome:
            produto.preco_unitario = novo_preco
            break

