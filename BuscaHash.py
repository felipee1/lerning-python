def main():
    lista = []
    for i in range(100):
        lista.append(None)
    c = 99
    while c is not 0:
        print('\nEscolha uma função:')
        print('\n1-Inserir')
        print('\n2-Buscar')
        print('\n3-listar')
        print('\n0-Sair')
        numero = int(input('\nDigite o valor da função: '))
        if numero == 1:
            from random import randint
            x = 0
            while x < 150:
                valor=randint(0,1000)
                ordem=valor%100
                inserir(lista,ordem,valor)
                x = x+1
        elif numero == 2:
            busca = int(input('\n Digite o valor a ser buscado:'))
            ordem = busca%100
            buscar(lista,busca,ordem)
        elif numero == 3:
            listar(lista)
        elif numero == 0:
            c=0
            print('\n Vlw Falooow!')

def inserir(lista,ordem,valor):
    no=[]
    if lista[ordem] is not None:
        no2 = lista[ordem]
        no2.append(valor)
    else:
        lista[ordem] = no
        no.append(valor)

def listar(lista):
    print('|Posição| |valores encadeados|')
    for i in range(100):
        print('|   '+str(i)+'   | |'+str(lista[i])+'|')

def buscar(lista,busca,ordem):
    g = lista[ordem]
    x = 0
    for i in sorted(g):
        if busca==i:
            x=x+1
            return print('\n Valor encontrado na posição '+str(ordem)+' da lista!')
    if x ==0:
        return print('\n Valor não encontrado na lista')

if __name__ == "__main__":
    main()


