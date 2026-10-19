"""Crie uma classe Pessoa, instancie a mesma por meio de uma variável e crie alguns atributos de classe dando características 
a essa pessoa. Por fim exiba em tela alguma mensagem que incorpore os atributos de classe criados:"""

class Pessoa:
    def __init__(self, nome, sobrenome, cor, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cor = cor
        self.idade = idade
      
        print(f"A pessoa criada tem o nome {self.nome} {self.sobrenome} e é da cor {self.cor}, possui a idade de {self.idade} anos") 

p = Pessoa("Marcio", "Santos", "Preta", 40)


