#Brett Kaplan and Jeff Johnston

from __future__ import division
import Queue
import random
from process import Process
from data import Data
import copy
import sys



"""
these are the tunable variables for the program.  timerSwitch is the clock time in ms
that it takes for a context switch. t is the timeslice for the round-robin algorithm.
n is the number of processes simulated.
"""
timerSwitch = 8
t=100
n = 20




#printout functions.  pass Processes to these and they will print what they say they will
def createprocess(a):
    print "[time","%.fms] Process" % (a.enter),"%.f created (requiring" % (a.id),"%.fms cpu time)" % (a.duration)
def switchprocess(a,b):
    print "[time","%.fms] Context switch (swapped out process" % (timer),"%.f for process" % (a.id),"%.f)" % (b.id)
def startprocess(a):
    print "[time","%.fms] Process" % (timer),"%.f accessed CPU for the first time (wait time" % (a.id),"%.fms)" % (a.iwait())
def terminateprocess(a):
    print "[time","%.fms] Process" % (timer),"%.f terminated (turnaround time" % (a.id),"%.fms, wait time" % (a.turnaround()),"%.fms)" % (a.twait())


""" """


#initial list of processes, all algorithms will use the same ones
#list of processes, id, time needed for execution,      priority,                                    entry time                                           for n processes
prolist = [Process(i, random.randint(500,7500), random.randint(0,4),random.randint(100,2500)*(i>=n/4)*(len(sys.argv) == 2 and sys.argv[1] == "-PART2")) for i in range(0,n)]
"""
the entry time argument looks mildly terrifying, but all it's doing is setting it to a random int in the range [100.2500]
  iff it is not in the first 25% of the processes created and the -PART2 argument was passed.
if either of those things are not true, then the random integer is multiplied by 0, causing the entry time to be 0.
the len(sys.argv)==2 component ensures that no null pointer exception is thrown when attempting to check argv[1].
"""


"""  """#First-Come, First-Served (FCFS), with no preemption and no time slice

queue = Queue.Queue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0 #processes terminated

incpu =-1 #holds a reference to the current process in cpu
ghost =-1 #holds a reference to the last process in cpu

processes=copy.deepcopy(prolist)
processes.sort()

data = Data(n)

while(procsterminated<len(processes)):
    
    if(pnum<len(processes)):
        a=processes[pnum]
        while(a.enter<=timer):
            queue.put(a)
            createprocess(a)
            pnum+=1
            if(pnum<len(processes)):
                a=processes[pnum]
            else: break
    if incpu == -1:
        incpu = queue.get()
        
        if ghost!=-1:
            switchprocess(ghost,incpu)
            timer+=timerSwitch
        if incpu.start == -1:
            incpu.start = timer
            startprocess(incpu)
    else:
        if incpu.timestep():
            incpu.end=timer
            terminateprocess(incpu)
            procsterminated+=1
            data.input(incpu)
            
            ghost=incpu
            incpu=-1
            
        timer+=1

print "\nFirst-Come, First-Served algorithm results:"
data.timelistPrint()


"""  """#Shortest-Job-First (SJF), with no preemption and no time slice

queue = Queue.PriorityQueue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0

incpu =-1
ghost =-1

processes=copy.deepcopy(prolist)
processes.sort()

data = Data(n)

while(procsterminated<len(processes)):
    
    if(pnum<len(processes)):
        a=processes[pnum]
        while(a.enter<=timer):
            queue.put((a.duration,a))
            createprocess(a)
            pnum+=1
            if(pnum<len(processes)):
                a=processes[pnum]
            else: break
    if incpu == -1:
        incpu = queue.get()[1]
        
        if ghost!=-1:
            switchprocess(ghost,incpu)
            timer+=timerSwitch
        if incpu.start == -1:
            incpu.start = timer
            startprocess(incpu)
    else:
        if incpu.timestep():
            incpu.end=timer
            terminateprocess(incpu)
            procsterminated+=1
            data.input(incpu)
            
            ghost=incpu
            incpu=-1
        
        timer+=1
    
print "\nShortest Job First algorithm results:"
data.timelistPrint()



"""  """#Preemptive Shortest-Job-First (SJF), with preemption and no time slice

queue = Queue.PriorityQueue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0

incpu =-1
ghost =-1

processes=copy.deepcopy(prolist)
processes.sort()

data = Data(n)

while(procsterminated<len(processes)):
    
    if(pnum<len(processes)):
        a=processes[pnum]
        while(a.enter<=timer):
            queue.put((a.duration,a))
            createprocess(a)
            pnum+=1
            
            #preempts the current running process if the one being
            #put in would finish before the current process.
            if(incpu!=-1 and (incpu.duration-incpu.curtime)>a.duration):
                queue.put((incpu.duration,incpu))
                ghost=incpu
                incpu=-1
            
            if(pnum<len(processes)):
                a=processes[pnum]
            else: break
    if incpu == -1:
        incpu = queue.get()[1]
        
        if ghost!=-1:
            switchprocess(ghost,incpu)
            timer+=timerSwitch
        if incpu.start == -1:
            incpu.start = timer
            startprocess(incpu)
    else:
        if incpu.timestep():
            incpu.end=timer
            terminateprocess(incpu)
            procsterminated+=1
            data.input(incpu)
            
            ghost=incpu
            incpu=-1
        
        timer+=1
    
print "\nPreemptive Shortest Job First algorithm results:"
data.timelistPrint()
    


""" """#Round-Robin (RR), with configurable time slice t initially set to 100 milliseconds

queue = Queue.Queue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0

incpu =-1
ghost =-1


ticker=0

processes=copy.deepcopy(prolist)
processes.sort()

data = Data(n)

while(procsterminated<len(processes)):
    
    if(pnum<len(processes)):
        a=processes[pnum]
        while(a.enter<=timer):
            queue.put(a)
            createprocess(a)
            pnum+=1
            if(pnum<len(processes)):
                a=processes[pnum]
            else: break
    if incpu == -1:
        incpu = queue.get()
        
        if ghost!=-1:
            switchprocess(ghost,incpu)
            timer+=timerSwitch
        if incpu.start == -1:
            incpu.start = timer
            startprocess(incpu)
    else:
        ticker+=1
        if incpu.timestep():
            incpu.end=timer
            terminateprocess(incpu)
            procsterminated+=1
            data.input(incpu)
            
            ghost=incpu
            incpu=-1
            ticker=0
        elif ticker>=t:
            queue.put(incpu)
            ghost=incpu
            incpu=-1
            ticker=0
        
        timer+=1

print "\nRound-Robin algorithm results:"
data.timelistPrint()




""" """#Preemptive Priority, with random priority levels 0-4 assigned to processes at the onset

queue = Queue.PriorityQueue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0

incpu =-1
ghost =-1

processes=copy.deepcopy(prolist)
processes.sort()

data = Data(n)

while(procsterminated<len(processes)):
    
    if(pnum<len(processes)):
        a=processes[pnum]
        while(a.enter<=timer):
            queue.put((a.priority,a))
            createprocess(a)
            pnum+=1
            
            #preempts the current running process if the one being
            #put in is of higher priority
            if(incpu!=-1 and (incpu.priority>a.priority)):
                queue.put((incpu.priority,incpu))
                ghost=incpu
                incpu=-1
            
            if(pnum<len(processes)):
                a=processes[pnum]
            else: break
    if incpu == -1:
        incpu = queue.get()[1]
        
        if ghost!=-1:
            switchprocess(ghost,incpu)
            timer+=timerSwitch
        if incpu.start == -1:
            incpu.start = timer
            startprocess(incpu)
    else:
        if incpu.timestep():
            incpu.end=timer
            terminateprocess(incpu)
            procsterminated+=1
            data.input(incpu)
            
            ghost=incpu
            incpu=-1
        
        timer+=1
    
print "\nPreemptive Priority algorithm results:"
data.timelistPrint()




