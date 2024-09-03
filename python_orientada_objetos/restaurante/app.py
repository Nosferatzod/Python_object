from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Goumert')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho Gourmet', 20.0, 'O melhor pão da cidade')
sobremesa = Sobremesa(nome="Pudim", preco=25.0,tipo="Doce", tamanho="Individual", descricao="Sobremesa de Portugal.")
 
sobremesa.aplicar_desconto()
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(sobremesa)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()