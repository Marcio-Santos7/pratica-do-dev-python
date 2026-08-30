"""Escreva um programa que retorna o número de Fibonacci: Sendo o número de Fibonacci um valor iniciado em 0 ou em 1 onde cada termo subsequente corresponde à soma dos dois
anteriores."""

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input('Digite um número para encontrar seu Fibonacci: '))
resposta = fibonacci(num-1)
print(resposta)

    