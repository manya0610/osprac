from audioop import reverse
from process import Process
from functions import sortbyat ,getInput


def priority():

    n= int(input("Enter number of processes : "))
    processes=[]
    completed=[]
    ready=[]
    gnattchart=""
    t=0
    complete=0
    for i in range(n):
        key = "P"+str(i+1)
        a = int(input("Enter arrival time of process"+str(i+1)+": "))
        b = int(input("Enter burst time of process"+str(i+1)+": "))
        c = int(input("Enter priority  of process"+str(i+1)+": "))
        processes.append(Process(key,a,b,c))


    def sortbypr(processes):
        processes.sort(key = lambda item:(item.priority), reverse=True)
    def sortbyat(processes):
        processes.sort(key = lambda item:(item.at))
    sortbyat(processes)

    print("t=",t)
    while(complete!=n):
        if(processes):
            i=0
            while((i<len(processes))and(len(processes)!=0)):    
                if(processes[i].at<=t):
                    ready.append(processes.pop(i))
                    sortbypr(ready)
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
                

                



                

                


