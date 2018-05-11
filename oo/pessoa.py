class Pessoa:
    def __init__(self, nome = None, idade=33):
        self.idade = idade
        self.nome = None


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Isaac'
    print(p.nome)
    print(p.idade)
    p.idade = 78
    print(p.idade)