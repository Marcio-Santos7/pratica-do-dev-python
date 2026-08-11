"""Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final 
do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a
soma dos mesmos: """

impares = 0
soma = 0

for i in range(1, 101, 2):
    impares += 1
    soma += i

print(f'Foram encontrados {impares} números ímpares!')
print(f'A soma destes números é: {soma}')


