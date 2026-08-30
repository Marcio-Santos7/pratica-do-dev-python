"""Crie uma função de número de parâmetros indefinido, que realiza a soma dos números repassados como parâmetro, independentemente da quantidade de números:"""

def soma(*args):
    num = 0
    for valordigitado in args:
        num += valordigitado
    print(f'O resultado da soma é: {num}')


soma(18, 43, 99, 1)


