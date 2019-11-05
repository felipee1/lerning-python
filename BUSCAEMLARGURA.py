from copy import deepcopy


matriz = [ [1,9,3], [4,2,6], [7,5,8] ]
raiz = {
  'profundidade':0,
  'data':matriz,
  'pai': None,
  'custo':0,
}
objetivo = [ [1,2,3], [4,5,6], [7,8,9] ]
lista = [raiz]

def sucessor(matriz,lista,no):
    pai=no
    no={
      'profundidade':'',
      'data':'',
      'pai':'',
      'custo':'',
    }
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j]==9):
                if(i+1<3):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i+1][j]
                    aux[i+1][j]=9
                    no['data']=aux
                    no['pai']=pai
                    no['profundidade']= pai['profundidade']+1
                    no['custo'] = 1
                    lista.append(deepcopy(no))
                    no['data']=''
                    no['pai']=''
                    no['profundidade']=''
                    no['custo'] = ''
                    #print(lista, "baixo")
                if(j+1<3):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i][j+1]
                    aux[i][j+1]=9
                    no['data']=aux
                    no['pai']=pai
                    no['profundidade']= pai['profundidade']+1
                    no['custo'] = 1
                    lista.append(deepcopy(no))
                    no['data']=''
                    no['pai']=''
                    no['profundidade']=''
                    no['custo'] = ''
                    #print(lista, "dir")
                if(i-1>=0):
                    aux = deepcopy(matriz)                   
                    aux[i][j]=aux[i-1][j]
                    aux[i-1][j]=9
                    no['data']=aux
                    no['pai']=pai
                    no['profundidade']= pai['profundidade']+1
                    no['custo'] = 1
                    lista.append(deepcopy(no))
                    no['data']=''
                    no['pai']=''
                    no['profundidade']=''
                    no['custo'] = ''
                    #print(lista, "cima")
                if(j-1>=0):
                    aux = deepcopy(matriz)
                    aux[i][j]=aux[i][j-1]
                    aux[i][j-1]=9
                    no['data']=aux
                    no['pai']=pai
                    no['profundidade']= pai['profundidade']+1
                    no['custo'] = 1
                    lista.append(deepcopy(no))
                    no['data']=''
                    no['pai']=''
                    no['profundidade']=''
                    no['custo'] = ''
                    #print(lista, "esquerda")
    #print(lista,"seu pai de calcinha")
                
def buscaLargura(lista):
  while(lista[0]['data']!=objetivo):
    sucessor(lista[0]['data'],lista[0])
    del(lista[0])
  print("este é o fera",lista[0])
     
def buscaProfundidade(lista):
  while(lista[len(lista)-1]['data']!=objetivo):
    aux=lista[len(lista)-1]['data']
    no=lista[len(lista)-1]
    del(lista[len(lista)-1])
    sucessor(aux,lista,no)
    if(lista[len(lista)-1]['data'] == objetivo):
      print("achou no nó ", lista[len(lista)-1]['data'])
      break

def buscaProfundidadeLimitada(lista,limite):
  while(len(lista)>0):
    if(lista[len(lista)-1]['data'] == objetivo):
      print("achou no nó ", lista[len(lista)-1]['data'])
      break
    elif((lista[len(lista)-1]['profundidade'])<limite):
      aux=lista[len(lista)-1]['data']
      no=lista[len(lista)-1]
      del(lista[len(lista)-1])
      sucessor(aux,lista,no)
    elif(lista[len(lista)-1]['profundidade']==limite):
      del(lista[len(lista)-1])

def buscaProfundidadeLimitadaIterativa(raiz,lista,limite):
  flag = 0
  while(len(lista)>0):
    if(lista[len(lista)-1]['data'] == objetivo):
      print("achou no nó ", lista[len(lista)-1]['data'], 'na profundidade',lista[len(lista)-1]['profundidade'] )
      flag =1
      break
    elif((lista[len(lista)-1]['profundidade'])<limite):
      aux=lista[len(lista)-1]['data']
      no=lista[len(lista)-1]
      del(lista[len(lista)-1])
      sucessor(aux,lista,no)
    elif(lista[len(lista)-1]['profundidade']==limite):
      del(lista[len(lista)-1])
  if(flag == 0):
    lista=[raiz]
    buscaProfundidadeLimitadaIterativa(raiz,lista,(limite*2))

buscaProfundidadeLimitadaIterativa(raiz,lista,2)
