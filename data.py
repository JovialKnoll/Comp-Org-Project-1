
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
        print "Turnaround times:"
        print "\nMinimum:", self.timelist[0]
        print "\nAverage:", self.timelist[1]/self.n
        print "\nMaximum:", self.timelist[2]
        print "Initial wait times:"
        print "\nMinimum:", self.timelist[3]
        print "\nAverage:", self.timelist[4]/self.n
        print "\nMaximum:", self.timelist[5]
        print "Total wait times:"
        print "\nMinimum:", self.timelist[6]
        print "\nAverage:", self.timelist[7]/self.n
        print "\nMaximum:", self.timelist[8]