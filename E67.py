"""Crie uma classe de nome Carro e lhe dê três atributos: nome, ano e cor."""

class Carro:
    def __init__(self, nome, ano, cor):
        self.nome = nome
        self.ano = ano
        self.cor = cor
        

c = Carro("Polo", 2025, "prata")

print(c.nome)
print(c.cor)
print(c.ano)

