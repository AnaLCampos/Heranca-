class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

pessoa1 = pessoa("Kátia", 38)

aluno1 = Aluno("Ana Luiza", 17, "11111")
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {aluno1.nome}, Idade: {aluno1.idade}, Matrícula: {aluno1.matricula}")
