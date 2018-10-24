class No(object):

    def __init__(self, carga, carga2, anterior, proximo):
        self.carga = carga
        self.carga2 = carga2
        self.anterior = anterior
        self.proximo = proximo

class ListaDuplamenteEncadeada(object):
    cabeca = None
    rabo = None


class NoArv:
    def __init__(self, Valor, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
        self.valor = Valor

class Arvore(object):
        raiz = None
        base = None

def add(self, valor):
    novo_noarv = NoArv(valor, None, None)
    if self.raiz is None:
        self.raiz = novo_noarv
        self.base = novo_noarv
    else:
        self.base.direita = novo_noarv
        self.base = novo_noarv


def busca(self,valor):
    no_atual = self.raiz
    listaa = []
    L: int = 0
    for i in valor:
        no_atual = self.raiz
        while no_atual is not None:
            if no_atual.valor == i:
                listaa.append(0)
                L += 1
                no_atual = None
            else:
                listaa.append(1)
                no_atual = no_atual.direita
                L += 1
    del(listaa[L-1])
    print('-<',listaa,'>-')


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
        if no_atual.carga == dado:
            add(raiz,str(no_atual.carga2))
            no_atual = no_atual.proximo
        else:
            no_atual = no_atual.proximo


def contador(texto):
    i: str = None
    j: str = None
    a: str = None
    c: bool
    raiz = Arvore()
    lista = ListaDuplamenteEncadeada()
    for i in texto:
        a = i
        c = comparar(lista,a)
        if c == False:
            acrescentar(lista,texto.count(a),a)
    listf = list(lista)
    listf.sort()
    listf.reverse()
    for k in listf:
        inserirA(lista,k,raiz)
    busca(raiz,texto)


texto = str(input('\ndigite a palavra: '))
print('o texto:',texto,' Comprimido fica:')
contador(texto)