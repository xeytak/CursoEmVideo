
def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * taxa/100)
    return res if form is False else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * taxa/100)
    return res if form is False else moeda(res)

def dobro(preco=0, form=False):
    res = preco * 2
    return res if form is False else moeda(preco)


def metade(preco=0, form=False):
    res = preco / 2
    return res if form is False else moeda(preco)


def moeda(preco=0):
    f = f'R${preco:.2f}'.replace('.', ',')
    return f

