"""Crie uma classe de nome Inventario com os atributos de classe pré-definidos item1 e item2, a serem cadastrados manualmente pelo usuário,
simulando um simples carrinho de compras:"""

class Inventario:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

cliente1 = Inventario('Camisa Adidas Tam GG', 'Calça Jeans Tam 50')

print(cliente1.item1)
print(cliente1.item2)

    
