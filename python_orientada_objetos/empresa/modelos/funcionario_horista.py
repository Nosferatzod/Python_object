from modelos.funcionario import Funcionario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, id, horas_trabalhadas, valor_por_hora):
        super().__init__(nome, id)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora

    def aplicar_bonificacao(self, valor):
        self.valor_por_hora += valor / self.horas_trabalhadas
