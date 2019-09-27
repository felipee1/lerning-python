from beautifultable import BeautifulTable
 
table = BeautifulTable()
table.column_headers = ["Processo(s)", "Tempo de Execução", "Tempo de Espera", "Tempo de Resposta"]

cont = 0
temresp = 0

qtd_processos = int(input("Insira a quantidade de processos -> "))

temp_execut = input("Insira o tempo de execução de cada processo -> ")
te = temp_execut.split()

while(qtd_processos > cont):
    if(cont == 0):
        tesp = 0
    else:
        tesp += int(te[cont-1])

    temresp += int(te[cont])
    
    table.append_row([cont,te[cont],tesp,temresp])
    cont += 1

print (table)

    
