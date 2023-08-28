class forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class retangulo(forma):
    def calcular_area(self):
        return self.largura * self.altura

class triangulo(forma):
    def calcular_area(self):
        return (self.largura * self.altura) / 2

retangulo = retangulo(6, 12)
triangulo = triangulo(18, 9)

print("Área do Retângulo:", retangulo.calcular_area())
print("Área do Triângulo:", triangulo.calcular_area())
