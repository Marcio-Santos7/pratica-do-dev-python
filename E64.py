"""Crie um programa modularizando, onde em um arquivo teremos uma lista de médicos fictícios a serem consultados, em outro arquivo, teremos a estrutura principal do 
programa, que por sua vez realiza o agendamento de uma consulta médica com base na interação com o usuário."""

# Arquivo medicos.py
# medicos = ['Grazielle Veiga', 'Matheus Correa']

# Arquivo main.py
import medicos

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()

if menu == 'S':
    paciente = input('Por favor, digite seu nome completo:')
    print(f'{paciente}, escolha com qual médico deseja consultar:')
    print('1 - Grazielle Veiga')
    print('2 - Matheus Correa')
    medico = int(input('Com qual médico deseja agendar consulta?'))
    if medico == 1:
        print(f'Sua consulta com a Dr.a {medicos.medicos[0]} será agendada.')
    if medico == 2:
        print(f'Sua consulta com o Dr {medicos.medicos[1]} será agendada.')
else:
    print('Agradecemos o seu contato!!!')



