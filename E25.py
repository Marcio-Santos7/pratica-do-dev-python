"""Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal 
número é PAR ou se é ÍMPAR:"""

num = int(input("Digite um número: "))

if(num % 2 == 0):
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')
