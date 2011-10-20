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
        print "\tTurnaround times:"
        print "\t\tMinimum:", round(self.timelist[0],3)
        print "\t\tAverage:", round(self.timelist[1]/self.n,3)
        print "\t\tMaximum:", round(self.timelist[2],3)
        print "\tInitial wait times:"
        print "\t\tMinimum:", round(self.timelist[3],3)
        print "\t\tAverage:", round(self.timelist[4]/self.n,3)
        print "\t\tMaximum:", round(self.timelist[5],3)
        print "\tTotal wait times:"
        print "\t\tMinimum:", round(self.timelist[6],3)
        print "\t\tAverage:", round(self.timelist[7]/self.n,3)
        print "\t\tMaximum:", round(self.timelist[8],3), "\n"
        