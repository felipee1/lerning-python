import random

def RoundRobin():
  def findWaitingTime(processes, n, bt,  
                          wt, quantum):  
      rem_bt = [0] * n 
      ft = True
    # Inserindo burst time na variavel rt
      for i in range(n):  
          rem_bt[i] = bt[i] 
      t = 0 # tempo atual
    
      # mantem percorrendo os processos enquanto não acabar o burst time de todos
      while(1): 
          done = True
    
          for i in range(n): 
                
              if(ft):
                  if(rem_bt[i]<quantum):
                      quantum = rem_bt[i]

              # mantem processando enquanto o burst time for maior que 0
              if (rem_bt[i] > 0) : 
                  done = False # processo ainda com burst time
                    
                  if (rem_bt[i] > quantum) : 
                    
                      # adicionando quanta ao tempo total decorrido
                      t += quantum  
    
                      # retirando quanta do processo que está a executar 
                      rem_bt[i] -= quantum  
                    
                  #verifica se o burst time é menor ou igual ao quantum, se for menor ou igual executa sua ultima vez  
                  else: 
                    
                      # aumenta o tempo em que o processo executou 
                      t = t + rem_bt[i]  
    
                      # tempo de espera é o tempo atual menos o tempo que o processo executou  
                      wt[i] = t - bt[i]  
    
                      # se terminou de executar coloca 0 no burst time 
                      rem_bt[i] = 0
          
          ft=False
          # verifica se o processo acabou
          if (done == True): 
              return quantum
              break
                
  # função que calcula o turn arround 
  def findTurnAroundTime(processes, n, bt, wt, tat): 
        
       
      for i in range(n): 
          tat[i] = bt[i] + wt[i]  
    
    
  #  função que calcula o tempo médio de espera e turn arround  de todos os processos 
  def findavgTime(processes, n, bt, quantum):  
      wt = [0] * n 
      tat = [0] * n  
    
      #função que calcula o tempo de espera médio de todos os processos
      quantumFinal = findWaitingTime(processes, n, bt,  
                          wt, quantum)  
      #  função que calcula turn arround médio de todos os processos
      findTurnAroundTime(processes, n, bt, 
                                  wt, tat)  
      # mostra tabela com resultados  
      print("Processos    Burst Time     Waiting",  
                      "Time    Turn-Around Time") 
      total_wt = 0
      total_tat = 0
      for i in range(n): 
    
          total_wt = total_wt + wt[i]  
          total_tat = total_tat + tat[i]  
          print(" ", i + 1, "\t\t", bt[i],  
                "\t\t", wt[i], "\t\t", tat[i]) 
    
      print("\nwaiting time médio = %.5f "%(total_wt /n) ) 
      print("turn around médio = %.5f "% (total_tat /n))  
      print("quantum final = ",(quantumFinal))  

  # Driver code  
  proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
  n = 10

  #burst_time = [6, 8, 7, 3, 4, 9, 6, 4, 2, 1]   #exemplo de burst time hard coded
  # Gerador de Burst time dos processos 
  burst_time= []
  for y in range(10):
    burst_time.append(random.randint(1,10))
  # quantum  
  quantum = 5;  
  findavgTime(proc, n, burst_time, quantum) 

print("--------------------------------------------------------------------------")

RoundRobin()

print("--------------------------------------------------------------------------")