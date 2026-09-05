"""Aprimore o exemplo anterior, incluindo um módulo simulando o cadastro de usuários em um plano de saúde, apenas permitindo o 
agendamento de consulta caso o usuário que está interagindo com o programa conste no cadastro: """

# Arquivo medicos.py
# medicos = ['Grazielle Veiga', 'Matheus Correa']

# Arquivo cadastro_plano_saude.py
# usuarios = {'001':'Fernando Feltrin', '002':'Marcio Leandro'}

# Arquivo main.py
import medicos
import cadastro_plano_saude
import sys

usuario = str(input('Digite seu número de usuário: '))

if usuario in cadastro_plano_saude.usuarios.keys():
    if usuario == '001':
        usuario = 'Fernando'
        print('Bem-vindo Fernando!!!')
        #return usuario
    elif usuario == '002':
        usuario = 'Marcio'
        print('Bem-vindo Marcio!!!')
        #return usuario
else:
    print('Usuário desconhecido ou não cadastrado.')
    sys.exit()
    

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()

if menu == 'S':
    print(f'{usuario}, escolha com qual médico deseja consultar:')
    print('1 - Grazielle Veiga')
    print('2 - Matheus Correa')
    medico = int(input('Com qual médico deseja agendar consulta?'))
    if medico == 1:
        print(f'Sua consulta com a Dr.a {medicos.medicos[0]} será agendada.')
    elif medico == 2:
        print(f'Sua consulta com o Dr {medicos.medicos[1]} será agendada.')
else:
    print('Agradecemos o seu contato!!!')