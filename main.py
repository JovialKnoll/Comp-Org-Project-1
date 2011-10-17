import Queue
import random
from process import Process

timer = 0

timerSwitch = 8

#q=q.q()  qqqqqqq
queue = Queue.Queue(0)


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
