import random

def ShortestJobFirst():
  def findWaitingTime(processes, n, wt):  
      rt = [0] * n 
    
      # Inserindo burst time na variavel rt
      for i in range(n):  
          rt[i] = processes[i][1] 
      complete = 0
      t = 0
      minm = 999999999
      short = 0
      check = False
      while (complete != n): 
            
          # Procura o processo com menor tempo de execução 
          for j in range(n): 
              if ((processes[j][2] <= t) and 
                  (rt[j] < minm) and rt[j] > 0): 
                  minm = rt[j] 
                  short = j 
                  check = True
          if (check == False): 
              t += 1
              continue
                
          # Executa por um quanta
          rt[short] -= 1
    
          # Atualiza o menor tempo
          minm = rt[short]  
          if (minm == 0):  
              minm = 999999999
    
          # Se completo == executado
          if (rt[short] == 0):  
    
              # variavel que controle se completo ou nao  
              complete += 1
              check = False
    
              # Hora de término de execução do processo 
              fint = t + 1
    
              # calcula o tempo de espera  
              wt[short] = (fint - proc[short][1] -    
                                  proc[short][2]) 
    
              if (wt[short] < 0): 
                  wt[short] = 0
            
          # adiciona mais um no tempo total de espera
          t += 1
    
  # função que calcula turn arround
  def findTurnAroundTime(processes, n, wt, tat):  
        
      for i in range(n): 
          tat[i] = processes[i][1] + wt[i]  
    
  # função que calcula o tempo médio de espera e turn arround  
  def findavgTime(processes, n):  
      wt = [0] * n 
      tat = [0] * n  
    
      # função de tempo médio de espera dos processos
      findWaitingTime(processes, n, wt)  
    
      # função que calcula turn arround médio de todos os processos
      findTurnAroundTime(processes, n, wt, tat)  
    
      # print dos dados recolhidos 
      print("Processos    Burst Time     Waiting",  
                      "Time     Turn-Around Time") 
      total_wt = 0
      total_tat = 0
      for i in range(n): 
    
          total_wt = total_wt + wt[i]  
          total_tat = total_tat + tat[i]  
          print(" ", processes[i][0], "\t\t",  
                    processes[i][1], "\t\t",  
                    wt[i], "\t\t", tat[i]) 
    
      print("\nwaiting time médio = %.5f "%(total_wt /n) ) 
      print("turn around time médio = ", total_tat / n)  

  proc = [] 

#  proc = [[1, 6, 1], [2, 8, 1], 
#       [3, 7, 2], [4, 3, 3]] #exemplo de input de processo caso queira validar


  count = 1
  for z in range(10):
      procgen=[]
      for y in range(2):
          procgen.append(count)
          procgen.append(random.randint(1,10))
      count+=1
      proc.append(procgen)


  n = 10
  findavgTime(proc, n) 
    

print("--------------------------------------------------------------------------")

ShortestJobFirst()

print("--------------------------------------------------------------------------")

