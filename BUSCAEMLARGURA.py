from copy import deepcopy

class Node: 
  def __init__(self, cargo=None, next=None): 
    self.data = cargo 
    self.cdr = next    
  def __str__(self): 
    return str(self.car)


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data, cdr):
        new_node = Node() # create a new node

        new_node.data = data
        new_node.cdr = cdr # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.cdr

matriz = [ [1,2,3], [9,5,6], [8,4,7] ]
objetivo = [ [1,2,3], [4,5,6], [7,8,9] ]
lista =[matriz]
no = LinkedList()
no.add_node(matriz,None)
def sucessor(matriz,lista,no):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j]==9):
                if(i+1<3):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i+1][j]
                    aux[i+1][j]=9
                    no.add_node(aux,matriz)
                    lista.append(aux)
                    #print(aux, "baixo")
                if(j+1<3):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i][j+1]
                    aux[i][j+1]=9
                    no.add_node(aux,matriz)
                    lista.append(aux)
                    #print(aux, "dir")
                if(i-1>=0):
                    aux = deepcopy(matriz)                   
                    aux[i][j]=aux[i-1][j]
                    aux[i-1][j]=9
                    no.add_node(aux,matriz)
                    lista.append(aux)
                    #print(aux, "cima")
                if(j-1>=0):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i][j-1]
                    aux[i][j-1]=9
                    no.add_node(aux,matriz)
                    lista.append(aux)
                    #print(aux, "esquerda")
def buscaLargura(lista,no):
     while(lista[0]!=objetivo):
         sucessor(lista[0],lista,no)
         del(lista[0])
     print("este é o fera",lista[0])
     
def buscaProfundidade(lista,no):
     while(lista[len(lista)-1]!=objetivo):
          sucessor(lista[len(lista)-1],lista,no)
     print("este é o fera",lista[len(lista)-1])

buscaProfundidade(lista,no)
