#Felipe Stefani
class No(object):

    def __init__(self, carga, carga2, anterior, proximo):
        self.carga = int(carga)
        self.carga2 = carga2
        self.anterior = anterior
        self.proximo = proximo

class ListaDuplamenteEncadeada(object):
    cabeca = None
    rabo = None

def busca(listaTexto,listaCod,texto):
    j = 0
    for i in texto:
        for j in range(len(listaTexto)):
            if i == listaTexto[j]:
                print(listaCod[j], end='')
            

def acrescentar(self, carga, carga2):
    novo_no = No(carga,carga2, None, None)
    i = self.cabeca
    if self.cabeca is None:
        self.cabeca = novo_no
        self.rabo = novo_no
    else:
        if carga > int(self.cabeca.carga):
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
        else:
            v = int(self.cabeca.carga)
            while carga < v or carga == v:
                if i == self.rabo:
                    i.proximo = novo_no
                    novo_no.anterior = i
                    self.rabo = novo_no
                    break
                else:
                    if i.proximo is not None:
                        i = i.proximo
                        v = int(i.carga)
            if carga > v:
                novo_no.proximo = i
                novo_no.anterior = i.anterior
                i.anterior.proximo = novo_no
                i.anterior = novo_no
                       

def criararvore(self, listaTexto, listaCod):
    if self.rabo.proximo == None:
        self.rabo.carga = self.rabo.carga+self.rabo.anterior.carga
        listaTexto.append(self.rabo.carga2)
        listaCod.append('1')
        listaTexto.append(self.rabo.anterior.carga2)
        listaCod.append('0')
        self.rabo = self.rabo.anterior
        self.rabo.proximo.anterior = self.rabo.carga2
        self.rabo.proximo.proximo = self.rabo.proximo.carga2
        self.rabo = self.rabo.anterior
        self.rabo.proximo = self.rabo.proximo.proximo
        i = 2
        j = i
        k = i
    while True:
        if self.rabo == self.cabeca:
            self.rabo.anterior = self.rabo.carga2
            listaTexto.append(self.rabo.carga2)
            listaCod.append('0')
            for j in range(i):
                    listaCod[j] = '1' + listaCod[j]
            break
        else:
            a = self.rabo.anterior.carga
            b = self.rabo.proximo.carga
            if a > b:
                self.rabo.carga = self.rabo.carga+self.rabo.proximo.carga
                listaTexto.append(self.rabo.carga2)
                listaCod.append('0')
                for o in range(i):
                    listaCod[o] = '1' + listaCod[o]
                i = i+1
                j = i+1
                self.rabo = self.rabo.anterior
                self.rabo.proximo.anterior = self.rabo.proximo.carga2
            else:
                novo_no = No(self.rabo.carga+self.rabo.anterior.carga, None, self.rabo.carga2, self.rabo.anterior.carga2)
                self.rabo = self.rabo.anterior
                self.rabo.proximo.anterior = novo_no
                self.rabo.proximo.carga = self.rabo.proximo.carga+self.rabo.carga
                listaTexto.append(self.rabo.carga2)
                listaCod.append('00')
                listaTexto.append(self.rabo.proximo.carga2)
                listaCod.append('01')
                for j in range(k):
                    listaCod[j] = '1' + listaCod[j]
                k = k+1
                self.rabo = self.rabo.anterior
        
def percorrer(self):
    i = self.cabeca
    while i != self.rabo:
        i = i.proximo
    
    

def comparar(self,carga2):
    no_atual = self.cabeca
    while no_atual is not None:
        if str(no_atual.carga2) == carga2:
            return True
            break
        else:
            no_atual = no_atual.proximo  
    if no_atual is None:
        return False

def contador(texto):
    c = bool
    j = 0
    lista = ListaDuplamenteEncadeada()
    listaTexto = []
    listaCod = []
    for i in texto:
        c = comparar(lista,i)
        if c == False:
            acrescentar(lista,texto.count(i),i)
    criararvore(lista,listaTexto,listaCod)
    print('Tabela para comparação:')
    for j in range(len(listaCod)):
        print('|'+listaTexto[j]+'||'+listaCod[j]+'|')
        j = j+1
    print('Codigo comprimido:')
    busca(listaTexto,listaCod,texto)


texto = str(input('\ndigite a palavra: '))
print('o texto:',texto,' Comprimido fica:')
contador(texto)
