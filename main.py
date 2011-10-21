from __future__ import division
import Queue
import random
from process import Process
from data import Data
import copy
import sys


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

timerSwitch = 8

n = 20

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

#q=q.q()  qqqqqqq
queue = Queue.Queue(0)

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

#q=q.q()  qqqqqqq
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



"""  
running = 1
#Preemptive Shortest-Job-First (SJF), with preemption and no time slice
while(running):
    
    #output during simulation
    timer+=1
    
"""  #Round-Robin (RR), with configurable time slice t initially set to 100 milliseconds

#q=q.q()  qqqqqqq
queue = Queue.Queue(0)

timer = 0
pnum = 0 #the location of the next process that will be added to the queue
procsterminated=0

incpu =-1
ghost =-1

t=100
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
            #print procsterminated
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

"""
running = 1
#Preemptive Priority, with random priority levels 0-4 assigned to processes at the onset (low numbers indicate high priority); processes with the same priority are processed in FCFS order with no time slice; higher-priority processes entering the system interrupt and preempt a running process
while(running):
    
    #output during simulation
    timer+=1
        
"""  """
#output for each scheduling algorithm:
#Minimum, average, and maximum turnaround times
#Minimum, average, and maximum initial wait times
#Minimum, average, and maximum total wait times
"""
