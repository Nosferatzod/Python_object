from modelos.funcionario_horista import FuncionarioHorista
from modelos.funcionario_mensalista import FuncionarioMensalista

def print_funcionario(funcionarios, index=0):
    if index < len(funcionarios):
        print(funcionarios[index])
        print_funcionario(funcionarios, index + 1)

def aplicar_bonificacao(funcionarios, valor, index=0):
    if index < len(funcionarios):
        funcionarios[index].aplicar_bonificacao(valor)
        aplicar_bonificacao(funcionarios, valor, index + 1)

def main():
    funcionarios = [
        FuncionarioHorista("Bibi", 1, 160, 50),
        FuncionarioHorista("Kauã", 2, 180, 45),
        FuncionarioMensalista("Arthur", 3, 3000),
        FuncionarioMensalista("Dudao", 4, 3500)
    ]

    print("Funcionários cadastrados:")
    print_funcionario(funcionarios)

    bonificacao = 200
    aplicar_bonificacao(funcionarios, bonificacao)

    print("\nApós aplicação da bonificação:")
    print_funcionario(funcionarios)

if __name__ == "__main__":
    main()
