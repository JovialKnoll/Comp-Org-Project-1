from __future__ import division

class Data():

    def __init__(self, n):
        self.n = n
        self.timelist = [n*750000,0,0,n*750000,0,0,n*750000,0,0]
    
    def input(self, inpro):
        #turnaround
        self.timelist[0] = min(self.timelist[0],inpro.turnaround())
        self.timelist[1] += inpro.turnaround()
        self.timelist[2] = max(self.timelist[2],inpro.turnaround())
        #iwait
        self.timelist[3] = min(self.timelist[3],inpro.iwait())
        self.timelist[4] += inpro.iwait()
        self.timelist[5] = max(self.timelist[5],inpro.iwait())
        #twait
        self.timelist[6] = min(self.timelist[6],inpro.twait())
        self.timelist[7] += inpro.twait()
        self.timelist[8] = max(self.timelist[8],inpro.twait())
        
    def timelistPrint(self):
        print "\tTurnaround times:\n\t\tMinimum: %.3f" % (self.timelist[0])
        print "\t\tAverage: %.3f" % (self.timelist[1])
        print "\t\tMaximum: %.3f" % (self.timelist[2])
        print "\tInitial wait times:\n\t\tMinimum: %.3f" % (self.timelist[3])
        print "\t\tAverage: %.3f" % (self.timelist[4]/self.n)
        print "\t\tMaximum: %.3f" % (self.timelist[5])
        print "\tTotal wait times:\n\t\tMinimum: %.3f" % (self.timelist[6])
        print "\t\tAverage: %.3f" % (self.timelist[7]/self.n)
        print "\t\tMaximum: %.3f\n" % (self.timelist[8])
        
