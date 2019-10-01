from beautifultable import BeautifulTable

table = BeautifulTable()
table.column_headers = ["Processo(s)", "Tempo de Execução", "Ordem por tempo de Prioridade","Tempo de espera"]

processo = []
tesp = 0

qtd_processos = int(input("Insira a quantidade de processos -> "))
temp_execut = input("Insira o tempo de execução de cada processo -> ")
forma = input("Qual forma de tempo de prioridade deseja? (maior ou menor) -> ")
te = temp_execut.split()

if(forma == 'menor'):

    temp = sorted(te, key=int)
    
    for index, i in enumerate(te):

        if(index == 0):
            tesp = 0
        else:
            tesp += int(temp[index-1])

        table.append_row([index,i,temp[index],tesp])
else:
    temp = sorted(te, key=int, reverse=True)
    
    for index, i in enumerate(te):
        
        if(index == 0):
            tesp = 0
        else:
            tesp += int(temp[index-1])

        table.append_row([index,i,temp[index],tesp])
        
print (table)
