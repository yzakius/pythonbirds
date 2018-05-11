class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    isaac = Pessoa(nome='Isaac')
    tobias = Pessoa(nome='Tobias')
    manolo = Pessoa(isaac, tobias, nome='Manolo')
    print(Pessoa.cumprimentar(manolo))
    print(id(manolo))
    print(manolo.cumprimentar())
    print(manolo.nome)
    print(manolo.idade)
    for filho in manolo.filhos:
        print(filho.nome)
    manolo.sobrenome = 'Ferreira'
    print(manolo.__dict__)
    print(isaac.__dict__)
    del manolo.filhos
    print(manolo.__dict__)
    print(isaac.__dict__)
