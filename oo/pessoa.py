class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    isaac = Mutante(nome='Isaac')
    tobias = Pessoa(nome='Tobias')
    manolo = Homem(isaac, tobias, nome='Manolo')
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
    print(isaac.olhos)
    print(manolo.cumprimentar())
    print(isaac.cumprimentar())