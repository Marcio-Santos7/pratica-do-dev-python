"""Crie um programa que recebe dados de um aluno como nome e suas notas em supostos 3 trimestres de aula, retornando um novo
dicionário com o nome do aluno e a média de suas notas: """

aluno = [{'Nome':'Paulo', 'Notas':[6, 8, 9]}, {'Nome':'Carlos', 'Notas':[5, 9, 7]}]



def calcula_media(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas'])/len(media['Notas']))
        else: 
            temp = 0
        notas.append({'Nome':media['Nome'], 'Média das notas':temp})
    print(notas)
    
media_estudante = calcula_media(aluno)
