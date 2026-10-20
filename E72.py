"""Crie uma classe Biblioteca que possui uma estrutura molde básica para cadastro de um livro de acordo com seu título,
porém que espera a inclusão de um número não definido de títulos. Em seguida cadastre ao menos 5 livros nessa biblioteca:"""

class Biblioteca:
    def __init__(self, livro1, **kwargs):
        self.livro1 = livro1

prateleira1 = Biblioteca('Livro Teste')
prateleira1.livro2 = '1984 - George Orwell'
prateleira1.livro3 = 'Duna - Frank Herbert'
prateleira1.livro4 = 'O iluminado - Stephen King'
prateleira1.livro5 = 'O Exorcista - William Peter Blatty'
prateleira1.livro6 = 'O Hobbit - J. R. R. Tolkien'

print(prateleira1.livro4)
print(prateleira1.livro1)

