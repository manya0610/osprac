class Process:
    def __init__(self,name,at,bt):
        self.name=name
        self.at=at
        self.bt=bt
        self.rt=bt
        self.ct=0
        self.tat=0
        self.wt=0
        self.priority=0
    def __init__(self,name,at,bt,p):
        self.name=name
        self.at=at
        self.bt=bt
        self.rt=bt
        self.ct=0
        self.tat=0
        self.wt=0
        self.priority=p
        
        self.isready=False
        self.isrunning=False

    def printdata(self):
        #print(self.name,self.at,self.bt,self.ct,self.tat,self.wt,self.rt,self.isready,self.isrunning)
        print(self.name,"        ",self.at,"       ",self.bt,"         ",self.ct,"       ",self.tat,"      ",self.wt)

