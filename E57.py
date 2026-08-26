"""Crie uma função com dois parâmetros relacionados ao nome e sobrenome de uma pessoa, a função deve retornar uma 
mensagem de boas-vindas e esses dados devem ser digitados pelo usuário: """

def boas_vindas(nome, sobrenome):
    print(f'Seja Bem Vindo(a) {nome} {sobrenome}')

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

boas_vindas(nome, sobrenome)

