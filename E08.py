"""Peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela 
tanto o número em si quanto seu tipo de dado."""

num = float(input("Digite um número: "))

tipo = type(num)

print(f'O número digitado é {num} e seu tipo é {tipo}')
