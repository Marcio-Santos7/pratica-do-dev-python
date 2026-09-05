"""Crie uma função que recebe parâmetros tanto por justaposição quanto nomeados a partir de uma lista e de um dicionário,
desempacotando os elementos e reorganizando os mesmos como parâmetro da função:"""

numeros = [33, 1987, 2020]

dados = {'Nome': 'Marcio', 'Profissão':'Cientista de Dados'}

def identificacao(*args, **kwargs):
    print(args)
    print(kwargs)

identificacao(*numeros, **dados)
