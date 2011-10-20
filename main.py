import Queue
import random
from process import Process
import copy
import sys


#so far, just printout functions.  pass Processes to these
def createprocess(a)
    print "[time",timer,"ms] Process",a.id,"created (requiring",duration,"ms cpu time)"
def switchprocess(a,b)
    print "[time",timer,"ms] Context switch (swapped out process",a.id,"for process",b.id,")"
def startprocess(a)
    print "[time",timer,"ms] Process",a.id,"addessed CPU fot the first time (wait time",a.iwait(),"ms)"
def terminateprocess(a)
    print "[time",timer,"ms] Process",id,"terminated (turnaround time",a.turnaround(),"ms, wait time",a.twait(),"ms)"


""" """


timer = 0

timerSwitch = 8

n = 20

#initial list of processes, all algorithms will use the same ones
#list of processes, id, time needed for execution,      priority,                                    entry time                                           for n processes
prolist = [Process(i, random.randint(500,7500), random.randint(0,4),random.randint(100,2500)*(i>=n/4)*(len(sys.argv) == 2 and sys.argv[1] == "-PART2")) for i in range(0,n)]
"""
the entry time argument looks mildly terrifying, but all it's doing is setting it to a random int in the range [100.2500]
  iff it is not in the first 25% of the processes created and the -PART2 argument was passed.
if either of those things are not true, then the random intiger is multiplied by 0, causing the entry time to be 0.
the len(sys.argv)==2 component ensures that no null pointer exception is thrown when attempting to check argv[1].
"""


#q=q.q()  qqqqqqq
queue = Queue.Queue(0)

processes=copy.deepcopy(prolist)
sorted(processes, key=lambda process: process.id)
"""  """
running = true
#First-Come, First-Served (FCFS), with no preemption and no time slice
while(running):
    
    #output during simulation
    

"""  """
running = true
#Shortest-Job-First (SJF), with no preemption and no time slice
while(running):
    
    #output during simulation
    
    
"""  """
running = true
#Preemptive Shortest-Job-First (SJF), with preemption and no time slice
while(running):
    
    #output during simulation
    
    
"""  """
running = true
#Round-Robin (RR), with configurable time slice t initially set to 100 milliseconds
while(running):
    
    #output during simulation


"""  """
running = true
#Preemptive Priority, with random priority levels 0-4 assigned to processes at the onset (low numbers indicate high priority); processes with the same priority are processed in FCFS order with no time slice; higher-priority processes entering the system interrupt and preempt a running process
while(running):
    
    #output during simulation
    
    
"""  """
#output for each scheduling algorithm:
#Minimum, average, and maximum turnaround times
#Minimum, average, and maximum initial wait times
#Minimum, average, and maximum total wait times
