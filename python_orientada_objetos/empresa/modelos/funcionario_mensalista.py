from modelos.funcionario import Funcionario

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, id, salario_mensal):
        super().__init__(nome, id)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal

    def aplicar_bonificacao(self, valor):
        self.salario_mensal += valor
