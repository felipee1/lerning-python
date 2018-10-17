class No(object):

    def __init__(self, carga, carga2, anterior, proximo):
        self.carga = carga
        self.carga2 = carga2
        self.anterior = anterior
        self.proximo = proximo

class ListaDuplamenteEncadeada(object):
    cabeca = None
    rabo = None


class arvbin:
    def __init__(self, Valor):
        self.Menor = None
        self.Maior = None
        self.conta = 1
        self.valor = Valor

    def add(self, valor):
        if valor > self.valor:
            self.addmaior(valor)
        elif valor < self.valor:
            self.addmenor(valor)
        else:
            self.conta = self.conta + 1

    def addmenor(self, valor):
        if self.Menor:
            self.Menor.add(valor)
        else:
            self.Menor = arvbin(valor)

    def addmaior(self, valor):
        if self.Maior:
            self.Maior.add(valor)
        else:
            self.Maior = arvbin(valor)

    def busca(self,valor):
        if valor == self.Maior.valor:
            print('0')
        else:
            print('1')
            self.Maior.busca(valor)


def acrescentar(self, carga, carga2):
    novo_no = No(carga,carga2, None, None)
    if self.cabeca is None:
        self.cabeca = novo_no
        self.rabo = novo_no
    else:
        novo_no.anterior = self.rabo
        novo_no.proximo = None
        self.rabo.proximo = novo_no
        self.rabo = novo_no

def comparar2(self,carga2):
    no_atual = self.cabeca
    while no_atual is not None:
        if str(no_atual.carga2) == carga2:
            return no_atual.carga
        else:
             no_atual = no_atual.proximo

def comparar(self,carga2):
    no_atual = self.cabeca
    while no_atual is not None:
        if str(no_atual.carga2) == carga2:
            return no_atual.carga
        else:
             no_atual = no_atual.proximo
    return False

def list(self):
    no_atual = self.cabeca
    listas = []
    while no_atual is not None:
        listas.append(no_atual.carga)
        no_atual = no_atual.proximo
    return listas

def inserirA(self,dado,raiz):
    no_atual = self.cabeca
    while no_atual is not None:
        if int(no_atual.carga) == dado:
            raiz.add(str(dado))
            no_atual = no_atual.proximo
        else:
            no_atual = no_atual.proximo


def contador(texto):
    i: str = None
    j: str = None
    a: str = None
    c: bool
    raiz = arvbin('1')
    lista = ListaDuplamenteEncadeada()
    for i in texto:
        a = i
        c = comparar(lista,a)
        if c == False:
            acrescentar(lista,texto.count(a),a)
    listf = list(lista)
    print(' >>>', listf)
    listf.sort()
    print(' >>>', listf)
    listf.reverse()
    print(' >>>',listf)
    for k in listf:
        print(' >>>', k)
        inserirA(lista,k,raiz)
    for l in texto:
        u = comparar2(lista,l)
        print('----',u)
        raiz.busca(u)


texto = str(input('\ndigite a palavra: '))
print('\na compressão é :')
contador(texto)

#criar arvore baseado no codigo da lista alocando valor por string comparar