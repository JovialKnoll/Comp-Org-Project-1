#this derp is a derp that can derp derps
import random


class Process():
    
    duration=0
    enter=0
    priority=0
    
    start=-1
    end=-1
    
    #initializes with the duration, the time it entered the system, and
    #the priority of the process. enter time and priority default to 0
    
    #they should enter the ready queue at the same time,
    #the time of process creation should be put in later
    def __init__(self,i,d,p=0):
        self.id = i
        self.duration=d
        #self.enter=e
        self.priority=p
    
    
    
    #returns the time between start and end of the program
    #if it has not finished running, it returns -1
    def turnaround(self):
        if self.start==-1 or self.end==-1: return -1
        else: return self.end-self.start
        
    #returns initial wait time
    def iwait(self):
        if self.start==-1 or self.enter==-1: return -1
        else: return self.start-self.enter
        
    #returns total wait time
    def twait(self):
        if self.start==-1 or self.end==-1: return -1
        else: return self.end-self.enter-self.duration
    
    
""""""
#only test code past here


#initializes with random duration
p=Process(random.randint(500,7500))
p.start=15
p.end=1000
print p.runtime()
