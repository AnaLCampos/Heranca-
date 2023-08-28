class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class livro(produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class eletronico(produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

livro = livro("O pequeno príncipe", 15.22, "Antoine de Saint-Exupéry")
eletronico = eletronico("Microondas", 1154.75, "220V")

print("Livro:", livro.nome, "- Autor:", livro.autor, "- Preço:", livro.preco)
print("Eletrônico:", eletronico.nome, "- Voltagem:", eletronico.voltagem, "- Preço:", eletronico.preco)
