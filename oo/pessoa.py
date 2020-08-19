class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    beatriz = Pessoa(nome='Beatriz')
    rafael = Pessoa(beatriz, nome='Rafael')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Puyau'
    del rafael.filhos
    print(rafael.__dict__)
    print(beatriz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rafael.olhos)
    print(beatriz.olhos)
    print(id(Pessoa.olhos), id(rafael.olhos), id(beatriz.olhos))
