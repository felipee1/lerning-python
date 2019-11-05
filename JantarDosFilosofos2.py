import random as r
import time as t
import os

def neighborhood(a,b):
    if((a-b) == (1) or (b-a) == (-1) or (b-a) == (1) or (a-b) == (-1) or
       (a-b) == (4) or (b-a) == (-4) or (b-a) == (4) or (a-b) == (-4)):
        return True
    return False
garfos={
        1:True,
        2:True,
        3:True,
        4:True,
        5:True,        
        }

philos={
        1:{'status':'THINKING','left':1,'rigth':2,'hungry':100,'count':0},
        2:{'status':'THINKING','left':2,'rigth':3,'hungry':100,'count':0},
        3:{'status':'THINKING','left':3,'rigth':4,'hungry':100,'count':0},
        4:{'status':'THINKING','left':4,'rigth':5,'hungry':100,'count':0},
        5:{'status':'THINKING','left':5,'rigth':1,'hungry':100,'count':0},
        }

a=1

def eating(philos,index,garfos):    
    philos[index]['status']='EATING'
    left=philos[index]['left']
    rigth=philos[index]['rigth']
    garfos[left]=False
    garfos[rigth]=False
    
    

def thinking(philos,index,garfos):
    philos[index]['status']='THINKING'
    philos[index]['count']=0
    left=philos[index]['left']
    rigth=philos[index]['rigth']
    garfos[left]=True
    garfos[rigth]=True

def loop(philos,garfos):
    a=1
    b=3
    while(True):
        for i in range(5):
            if(philos[i+1]['status']=='EATING'):
                philos[i+1]['hungry']=philos[i+1]['hungry']+1
                philos[i+1]['count']=philos[i+1]['count']+1
                if(philos[i+1]['count']>=5 or philos[i+1]['hungry'] >= 100):
                    thinking(philos,(i+1),garfos)
            if(philos[i+1]['status']=='THINKING'):
                philos[i+1]['hungry']=philos[i+1]['hungry']-1
        for i in range(5):
            if(philos[i+1]['hungry']<=philos[a]['hungry']):
                if( garfos[(philos[i+1]['left'])]== True and garfos[(philos[i+1]['rigth'])]== True ):
                    a=i+1
                    
        if(philos[a]['status']=='THINKING'):
            if( garfos[(philos[a]['left'])]== True and garfos[(philos[a]['rigth'])]== True ):
                eating(philos,a,garfos)
            for i in range(5):
                if(philos[i+1]['status']=='THINKING' ):
                    if( garfos[(philos[i+1]['left'])]== True and garfos[(philos[i+1]['rigth'])]== True ):
                        eating(philos,i+1,garfos)
                    

                    
        if(philos[b]['status']=='THINKING'):
            if( garfos[(philos[b]['left'])]== True and garfos[(philos[b]['rigth'])]== True ):
                eating(philos,b,garfos)
                        
        t.sleep(0.1)
        print(".//////////////////////////////////////////////////.")
        print("Aristoteles:",philos[1])
        print("Platão:",philos[2])
        print("Nietzsche:",philos[3])
        print("Confúcio:",philos[4])
        print("Sócrates:",philos[5])
    


loop(philos,garfos)
