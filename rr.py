import random
import sys
from process import Process
from functions import sortbyat ,getInput,getRandomInput,avgwt,avgtat

def rr():
    choice=int(input("enter 1 for random input and 2 for user input"))
    if choice not in [1, 2 ]:
        print("Invalid choice!!")
        sys.exit(-1)
    if choice==1:
        processes=getRandomInput()
        timeslice=random.randint(0,5)
    elif choice==2:     
        processes=getInput()
        timeslice=int(input("enter timeslice"))
    n=len(processes)
    sortbyat(processes)
    t=0
    tmpts=0
    tmp=0
    complete=0
    completed=[]
    ready=[]
    gnattchart=""
    print("t=",t)
    while(complete!=n):
        if(processes):
            i=0
            while((i<len(processes))and(len(processes)!=0)):    
                if(processes[i].at<=t):
                    ready.append(processes.pop(i))
                    i=0

                else:
                    i+=1

        if(len(ready)!=0):
            if((ready[0].rt==0)):
                complete+=1
                tmpts=0
                ready[0].ct=t
                completed.append(ready.pop(0))
        if(len(ready)!=0):
            if(tmpts==timeslice):
                            tmpts=0
                            tmp=ready.pop(0)
                            ready.append(tmp)
            if((ready[0].rt!=0)):
                    ready[0].rt-=1
                    tmpts+=1
                    gnattchart+=ready[0].name
                                       
        t+=1
    if(complete==n):
        print("timeslice=",timeslice)
        print("Process | Arrival | Burst | compelete | Turn Around | Wait |")
        for j in completed:
            j.tat=j.ct-j.at
            j.wt=j.tat-j.bt
            
            j.printdata() 
    print(gnattchart)
    avgtat(completed)
    avgwt(completed)