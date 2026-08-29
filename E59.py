"""Crie uma função com três parâmetros sendo dois deles com dados/valores padrão, alterando o 
terceiro deles contornando o paradigma da justaposição de argumentos:"""

def pessoa1(nome, idade=18, funcao='técnico'):
    print(f'{nome} tem {idade} anos, e sua função é {funcao}')

p1 = pessoa1('Fernando', funcao='gerente')

