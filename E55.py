"""Crie uma função que recebe um nome como parâmetro e exibe em tela uma mensagem de boas-vindas. O nome deve ser
fornecido pelo usuário, incorporado na mensagem de boas-vindas da função: """

def boas_vindas(nome):
    print(f'Seja Bem Vindo(a) {nome} !!!')

nome = input("Digite o seu nome: ")

boas_vindas(nome)
