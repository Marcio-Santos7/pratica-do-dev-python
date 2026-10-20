"""Crie uma classe que armazena algumas características de um carro, em seguida crie dois carros distintos, de características diferentes,
usando da classe para construção de seus objetos/variáveis."""

class Carro:
    ano = 2020
    cor = 'prata'
    modelo = 'hatch'
    opcionais = 'nenhum'
    

carro1 = Carro()

carro2 = Carro()
carro2.ano = 2016
carro2.cor = 'preto'
carro2.modelo = 'sedan'

print(f'Carro nº 1: Ano = {carro1.ano}, Cor = {carro1.cor}, Modelo = {carro1.modelo}, Opcionais = {carro1.opcionais}')

print(f'Carro nº 2: Ano = {carro2.ano}, Cor = {carro2.cor}, Modelo = {carro2.modelo}, Opcionais = {carro2.opcionais}')       