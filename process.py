#this derp is a derp that can derp derps
import random


class Process():
    
    start=-1
    end=-1
    
    #initializes with the duration, process id,
    #the priority of the process, and the time it
    #should enter the system.
    #enter time and priority default to 0
    
    def __init__(self,i,d,p=0,e=0):
        self.id = i
        self.duration=d
        self.priority=p
        self.enter=e
        self.curtime=0
    
    def __lt__(self,other):
        return self.enter<other.enter
    
    #returns the time between start and end of the program
    #if it has not finished running, it returns -1
    def turnaround(self):
        if self.enter==-1 or self.end==-1: return -1
        else: return self.end-self.start
        
    #returns initial wait time
    def iwait(self):
        if self.start==-1 or self.enter==-1: return -1
        else: return self.start-self.enter
        
    #returns total wait time
    def twait(self):
        if self.enter==-1 or self.end==-1: return -1
        else: return self.end-self.enter-self.duration
    
    #increments the current time.  returns false until the
    #current time is one where the process would be done.
    def timestep(self,t=1):
        self.curtime+=t
        return self.curtime>=self.duration
    
    
        
    
    
    
""""""
#only test code past here


#initializes with random duration
p=Process(1,random.randint(500,7500))
p.start=15
p.end=1000
print p.turnaround()
