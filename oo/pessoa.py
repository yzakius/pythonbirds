class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    isaac = Homem(nome='Isaac')
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
    del manolo.filhos
    isaac.olhos = 1
    Pessoa.olhos = 3
    del isaac.olhos
    print(manolo.__dict__)
    print(isaac.__dict__)
    print(Pessoa.olhos)
    print(manolo.olhos)
    print(isaac.olhos)
    print(id(Pessoa.olhos), id(manolo.olhos), id(isaac.olhos))
    print(Pessoa.metodo_estatico(), isaac.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), isaac.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))