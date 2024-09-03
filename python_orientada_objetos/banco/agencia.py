# Importa a classe Banco de um módulo chamado banco
from banco import Banco

# Define uma classe chamada Agencia que herda de Banco
class Agencia(Banco):
    # Define o construtor da classe Agencia.
    def __init__(self, nome, endereco, numero):
        # Chama o construtor da classe base Banco, passando os parâmetros nome e endereco
        super().__init__(nome, endereco)
        # Inicializa o atributo numero específico da classe Agencia
        self.numero = numero
        
# Cria uma instância
banco = Banco("Banco Central", "Rua Principal, 123")
agencia = Agencia("Banco Central", "Rua Principal, 123", 456)

# Imprime os atributos nome e endereco da instância banco.
print(f"Banco - Nome: {banco.nome}, Endereço: {banco.endereco}")

# Imprime os atributos nome, endereco e numero da instância agencia.
print(f"Agência - Nome: {agencia.nome}, Endereço: {agencia.endereco}, Número: {agencia.numero}")
