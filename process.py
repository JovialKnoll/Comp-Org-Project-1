#derp
import random


class Process():
    
    duration=0
    enter=0
    priority=0
    
    start=-1
    end=-1
    
    #initializes with the duration
    def __init__(self,d,e=0,p=0):
        self.duration=d
        self.enter=e
        self.priority=p
        
    #returns the time between start and end of the program
    #if it has not finished running, it returns -1
    def runtime(self):
        if self.start==-1 or self.end==-1: return -1
        else: return self.end-self.start  
    
    
    
""""""
#only test code past here


#initializes with random duration
p=Process(random.randint(500,7500))
p.start=15
p.end=1000
print p.runtime()
