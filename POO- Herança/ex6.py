class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
class Refrigerante(Bebida):
    def __init__(self, nome, tipo, sabor):
        super().__init__(nome, tipo)
        self.sabor = sabor

class Cafe(Bebida):
    def __init__(self, nome, tipo, intensidade):
        super().__init__(nome, tipo)
        self.intensidade = intensidade

refrigerante1 = Refrigerante("Fanta", "Refrigerante",  "Uva")
print(f"Refrigerante: {refrigerante1.nome}, Tipo: {refrigerante1.tipo}, Sabor: {refrigerante1.sabor}")
cafe1 = Cafe("Espresso", "Café", "Forte")
print(f"Café: {cafe1.nome}, Tipo: {cafe1.tipo}, Intensidade: {cafe1.intensidade}")