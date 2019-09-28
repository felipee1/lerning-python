from beautifultable import BeautifulTable

table = BeautifulTable()
table.column_headers = ["Processo(s)", "Tempo de Execução", "Prioridade"]

cont = 0
prior = []
aux = 0
aux2 = 0
t = 0

qtd_processos = int(input("Insira a quantidade de processos -> "))
temp_execut = input("Insira o tempo de execução de cada processo -> ")
te = temp_execut.split()
#opcao = input("Como deseja realizar o escalonamento de prioridade? (maior ou menor) ")

#if(opcao == 'menor'):
while(qtd_processos > cont):

    if(cont == 0):
        prior.append(te[cont])
        print(prior[0],'---> primeiro if')
    else:
        if(te[cont] < prior[0]):
            aux = te[cont]
            aux2 = prior[0]
            prior[0] = aux
            prior.insert(1,aux2)
            print(prior,'--> segundo if')
        else:
            if(te[cont] < prior[cont-1]):
                aux = te[cont]
                aux2 = prior[cont-1]
                prior[cont-1] = aux
                prior.append(aux2)
                print(prior,'--> terceiro if')
            else:
                prior.append(te[cont])
                print(prior,'---> else')

    #if(p == te[cont]):
        table.append_row([cont,te[cont],p[cont]])
        cont += 1

print (table)
