#ALGORITMO SJF
def sjf ():
        print("PROCESSOS CRIADOS")
        print("ID processo  | Entrada do Processo | Tempo de Execução ")
        for x in range(0,n):
                print("    ",x+1,"               ",tmpEnt[x],"               ",tmpExe[x])
        
        entradas = list(tmpEnt)
        tempos = list(tmpExe)
        identf = list(idproc)
        escolhido = 0
        b=0
        wait=0
        for j in range(0,n): #ORDENA OS TEMPOS(DO MENOR PARA O MAIOR)
                for i in range(0,n-1):
                        if tempos[i]>tempos[i+1]:
                                Aux = tempos[i+1]#TROCA
                                tempos[i+1] = tempos[i]
                                tempos[i] = Aux
                                Auxe = entradas[i+1] #TROCA
                                entradas[i+1] = entradas[i]
                                entradas[i] = Auxe
                                Auxi = identf[i+1]
                                identf[i+1] = identf[i]
                                identf[i] = Auxi
                
                entra.append(entradas[j])
                temp.append(tempos[j])
                identific.append(identf[j])
                          
        for z in range(0,n):
                a = float(entradas[z-1]+tempos[z-1])
                ent = float(entradas[z])
                wait = (a-ent)
                if(z == 0):
                        wait = entradas[z]
                if(wait < 0):
                        wait = 0.0
                tmpEsp.append(wait)
        print("\n")
        print("PROCESSOS ORDENADOS E EXECUTADOS")
        print("ID processo  | Entrada do Processo | Tempo de Execução | Tempo de Espera")
        for o in range(0,n):
                       
                print("     ",identific[o],"             ",entra[o],"               ",temp[o],"              ",tmpEsp[o])

        soma = 0
        relogio = 0
        #calcula turnaround
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

#calcula media espera
def espera_media(lista):
        l = lista
        some = 0 
        for p in range(len(l)): 
                some += l[p]
        media = some/n
        return media

n = int(input ("Informe o numero de processos: "))
print("\n")
tmpExe = []
tmpEnt = []
tmpEsp = []
idproc = []

temp = []
entra = []
identific = []

#Entrada dos processos e seus valores
for x in range(1,n+1):
        print ("Tempo de entrada do processo ", x, ": ")
        tmpEnt.append(float(input()))
        print ("Tempo de execução do processo ", x, ": ")
        tmpExe.append(float(input()))
        idproc.append(x)

print ("\n")
print ("TURNAROUND MEDIO: ", sjf())
print ("TEMPO DE ESPERA MEDIO: ", espera_media(tmpEsp))
