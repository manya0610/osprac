from process import Process
from functions import sortbyat, sortbyrt ,getInput

def sjfp():
    processes=getInput()
    n=len(processes)
    sortbyat(processes)
    processes[0].isrunning=True #firstprocess
    t=0
    complete=0
    #print("t=",t)
    while(complete!=n):
        #print("Process | Arrival | Burst | compelete | Turn Around | Wait |")
        #for j in processes:
            #j.printdata()
        for i in range(n):
            if(processes[i].at<=t):
                processes[i].isready=True
            if((processes[i].isready==True)and(processes[i].rt!=0)and(processes[i].isrunning==True)):
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
        sortbyrt(processes)
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
            

            


