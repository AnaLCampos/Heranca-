class empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class gerente(empregado):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

empregado = empregado("Breno", 5000)
gerente = gerente("Ana Luiza", 10000, "Marketing")

print(f"empregado: {empregado.nome}, Salário: {empregado.salario}")
print(f"gerente: {gerente.nome}, Salário: {gerente.salario}, Setor: {gerente.setor}")
