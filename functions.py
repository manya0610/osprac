from process import Process
def sortbyrt(processes):
    processes.sort(key = lambda item:(item.rt))
def sortbyat(processes):
    processes.sort(key = lambda item:(item.at))
def sortbybt(processes):
    processes.sort(key = lambda item:(item.bt))

def getInput():
    n= int(input("Enter number of processes : "))
    processes=[]
    for i in range(n):
        key = "P"+str(i+1)
        a = int(input("Enter arrival time of process"+str(i+1)+": "))
        b = int(input("Enter burst time of process"+str(i+1)+": "))
        processes.append(Process(key,a,b))
    
    return processes


