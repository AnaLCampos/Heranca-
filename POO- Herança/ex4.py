class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class carro(veiculo):
    def __init__(self, marca, modelo, ano, numeroportas):
        super().__init__(marca, modelo, ano)
        self.numeroportas = numeroportas

class moto(veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

meucarro = carro(marca="Volkswagen", modelo="Gol", ano=1996, numeroportas=2)
minhamoto = moto(marca="Honda", modelo="CBR500R", ano=2021, cilindradas=500)

print("Carro:", meucarro.marca, meucarro.modelo, meucarro.ano, meucarro.numeroportas)
print("Moto:", minhamoto.marca, minhamoto.modelo, minhamoto.ano, minhamoto.cilindradas)
