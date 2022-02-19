import sys
from process import Process
from functions import sortbyat ,getInput,getRandomInput,avgtat,avgwt

def fcfs():
    choice=int(input("enter 1 for random input and 2 for user input"))
    if choice not in [1, 2 ]:
        print("Invalid choice!!")
        sys.exit(-1)
    if choice==1:
        processes=getRandomInput()
    elif choice==2:     
        processes=getInput()
    n=len(processes)
    sortbyat(processes)
    processes[0].isrunning=True
    completed=[]
    ready=[]
    gnattchart=""
    t=0
    complete=0
    while(complete!=n):
        if(processes):
            i=0
            while((i<len(processes))and(len(processes)!=0)):    
                if(processes[i].at<=t):
                    ready.append(processes.pop(i))
                    sortbyat(ready)
                    i=0
                else:
                    i+=1
                        
        
        if(len(ready)!=0):
            if((ready[0].rt!=0)):
                    ready[0].rt-=1
                    t+=1
                    gnattchart+=ready[0].name
        if(len(ready)!=0):
            if((ready[0].rt==0)):
                complete+=1
                ready[0].ct=t
                completed.append(ready.pop(0))
        else:
            t+=1
    if(complete==n):
        print("Process | Arrival | Burst | compelete | Turn Around | Wait |")
        for j in completed:
            j.tat=j.ct-j.at
            j.wt=j.tat-j.bt
            
            j.printdata()
        print(gnattchart)
        avgtat(completed)
        avgwt(completed)