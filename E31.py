"""Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário: """

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

progressao_20 = primeiro_termo + (19 * razao)

progressao_aritmetica = []

for i in range(primeiro_termo, progressao_20 + razao, razao):
    print(i)


     
