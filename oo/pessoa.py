class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    milton = Pessoa(luciano, nome='Milton')
    print(Pessoa.cumprimentar(milton))
    print((id(milton)))
    print(milton.cumprimentar())
    # p.nome = 'Milton'
    print(milton.nome)
    print(milton.idade)
    for filho in milton.filhos:
        print(filho.nome)
    milton.sobrenome = 'Bastos'
    print(milton.__dict__)
    del milton.sobrenome


