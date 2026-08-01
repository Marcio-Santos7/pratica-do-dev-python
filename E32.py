"""Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário: """

num = int(input("Digite o número para obter a tabuada: "))

print(f'A tabuada do número {num} é: ')
print()
for i in range(1, 11):
    print(f'{num} X {i} = {num * i}')

