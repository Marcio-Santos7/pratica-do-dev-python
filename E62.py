"""Crie uma função que recebe parâmetros tanto por justaposição (*args) quanto nomeados (**kwargs): """

def parametros(*args, **kwargs):
    print("Args: ", args)
    print("Kwargs: ", kwargs)

parametros(30, 5, 9, nome='Marcio', idade='39')

