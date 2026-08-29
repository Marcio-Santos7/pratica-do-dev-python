"""Crie uma função que pode conter dois ou mais parâmetros, porém sem um número definido e declarado de parâmetros:"""

def msg(*args):
    print(f'Os parâmetros são: {args}')

ex2 = msg('nome=Fernando', 'idade=33', 'profissão=professor')

