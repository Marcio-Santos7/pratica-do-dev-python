"""Crie uma função com dois parâmetros, sendo um deles com um dado/valor predeterminado: """

def multiplicacao_2(num1, num2 = 2):
    return num1 * num2

num = int(input("Digite um número: "))

resultado = multiplicacao_2(num)

print(resultado)
