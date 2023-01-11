import random
from process import Process
def sortbyrt(processes):
    processes.sort(key = lambda item:(item.rt))
def sortbyat(processes):
    processes.sort(key = lambda item:(item.at))
def sortbybt(processes):
    processes.sort(key = lambda item:(item.bt))
def sortbypr(processes):
    processes.sort(key = lambda item:(item.priority))

#added comment
print("ehllo")
#new comment for slave branch

def getInput():
    n= int(input("Enter number of processes : "))
    processes=[]
    for i in range(n):
        key = "P"+str(i+1)
        a = int(input("Enter arrival time of process"+str(i+1)+": "))
        b = int(input("Enter burst time of process"+str(i+1)+": "))
        processes.append(Process(key,a,b))

    return processes

def getRandomInput():
    n= int(input("Enter number of processes : "))
    processes=[]
    for i in range(n):
        key = "P"+str(i+1)
        a = random.randint(0,10)
        b = random.randint(0,10)
        processes.append(Process(key,a,b))

    return processes

def avgtat(processes):
    n=len(processes)
    avgtat=0
    for i in processes:
        avgtat+=i.tat
    avgtat/=n
    print("average turnaround time",avgtat,"\n")

def avgwt(processes):
    n=len(processes)
    avgwt=0
    for i in processes:
        avgwt+=i.wt
    avgwt/=n
    print("average turnaround time",avgwt,"\n")


