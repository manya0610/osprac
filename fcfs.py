from process import Process
from functions import sortbyat, sortbyrt ,getInput

def fcfs():
    processes=getInput()
    n=len(processes)
    sortbyat(processes)
    processes[0].isrunning=True
    t=0
    complete=0
    #print("t=",t)
    while(complete!=n):
        #print("Process | Arrival | Burst | compelete | Turn Around | Wait |")
        #for j in processes:
            #j.printdata()
        for process in processes:
            if(process.at<=t):
                process.isready=True
        for i in range(n):
            if((processes[i].isready==True)and(processes[i].isrunning==True)):
                processes[i].rt-=1
                #print(processes[i].name,"executed")
                if(processes[i].rt==0):
                    complete+=1
                    processes[i].ct=t+1
                    processes[i].isrunning=False
                    processes[i].isready=False
                    #print(processes[i].name,"completed")
                break
        t+=1
        for process in processes:
            process.isready=False
        #print("t=",t)
        for i in processes:
            if((i.rt!=0)and(i.at<=t)):
                i.isrunning=True
                break
    if(complete==n):
        print("Process | Arrival | Burst | compelete | Turn Around | Wait |")
        for j in processes:
            j.tat=j.ct-j.at
            j.wt=j.tat-j.bt
            
            j.printdata()