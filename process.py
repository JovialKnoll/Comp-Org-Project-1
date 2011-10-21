#this derp is a derp that can derp derps
import random


class Process():
    
    start=-1
    end=-1
    
    done=0
    
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
        if self.done: return self.end-self.enter
        else: return -1
        
    #returns initial wait time
    def iwait(self):
        if self.start!=-1: return self.start-self.enter
        else: return -1
        
    #returns total wait time
    def twait(self):
        if self.done: return self.end-self.enter-self.duration+1
        else: return -1
    
    #increments the current time.  returns false until the
    #current time is one where the process would be done.
    def timestep(self,t=1):
        self.curtime+=t
        if(self.curtime>=self.duration): self.done=1
        return self.done
            
   
    
    
""""""
#only test code past here



