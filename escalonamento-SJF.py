

#FUNÇÃO DO ALGORITMO SJF
def sjf ():
        entradas = list(tmpEnt)
        tempos = list(tmpExe)
        escolhido = 0
        b=0
        wait=0
        for j in range(0,n): #ORDENA OS TEMPOS(DO MENOR PARA O MAIOR)
                for i in range(0,n-1):
                        if tempos[i]>tempos[i+1]: 
                                Aux = tempos[i+1]#TROCA
                                tempos[i+1] = tempos[i]
                                tempos[i] = Aux
                                temp.append(tempos[i]) 
                                Auxe = entradas[i+1] #TROCA
                                entradas[i+1] = entradas[i]
                                entradas[i] = Auxe
                        entra.append(entradas[j])
                        print(entra,"entro")

        for z in range(0,n):
                a = float(entradas[z-1]+tempos[z-1])
                print(a,"soma")
                print(tempos[z])
                ent = float(entradas[z])
                print(ent,"entrada atual")
                wait = (a-ent)
                print(z)
                if(z == 0):
                        wait = entradas[z]
                if(wait < 0):
                        wait = 0.0
                print(wait,"espera")
                tmpEsp.append(wait)

        soma = 0
        relogio = 0
        for x in range(0,n):
                for y in range(0,n):
                        if entradas[y] <= relogio and entradas[y]>=0:
                                escolhido = y
                                break
                        pass
                relogio += tempos[escolhido] 
                soma += relogio - entradas[escolhido]
                entradas[escolhido]=-1
        return float(soma/n)

def espera_media(lista):
        l = lista
        some = 0 #iniciando a variavel soma
        for p in range(len(l)): #variacao de i de acordo com o tamanho de l
                some += l[p] #soma dos elemenos relacionados ao indice i do laço for
        media = some/n
        return media

n = int(input ("Informe o numero de processos: "))
tmpExe = []
tmpEnt = []
tmpEsp = []
temp = []
entra = []

#LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
for x in range(1,n+1):
        print ("Tempo de entrada do processo ", x, ": ")
        tmpEnt.append(float(input()))
        print ("Tempo de execução do processo ", x, ": ")
        tmpExe.append(float(input()))
        
print ("TURNAROUND MEDIO: ", sjf())
print ("TEMPO MEDIO DE ESPERA", espera_media(tmpEsp))

for x in range(0,n):
        print("ID processo  | Entrada do Processo | Tempo de Execução | Tempo de Espera")
        print("    ",x+1,"               ",tmpEnt[x],"               ",tmpExe[x],"               ",tmpEsp[x])
        print()

pass

