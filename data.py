
class Data():

    def __init__(self, n):
        self.n = n
        timelist = [n*750000,0,0,n*750000,0,0,n*750000,0,0]
    
    def input(self, inpro):
        #turnaround
        timelist[0] = min(timelist[0],inpro.turnaround())
        timelist[1] += incpu.turnaround()
        timelist[2] = max(timelist[2],inpro.turnaround())
        #iwait
        timelist[3] = min(timelist[3],inpro.iwait())
        timelist[4] += incpu.iwait()
        timelist[5] = max(timelist[5],inpro.iwait())
        #twait
        timelist[6] = min(timelist[6],inpro.twait())
        timelist[7] += incpu.twait()
        timelist[8] = max(timelist[8],inpro.twait())
        
    def timelistPrint(self):
        print "Turnaround times:"
        print "\nMinimum:", timelist[0]
        print "\nAverage:", timelist[1]/self.n
        print "\nMaximum:", timelist[2]
        print "Initial wait times:"
        print "\nMinimum:", timelist[3]
        print "\nAverage:", timelist[4]/self.n
        print "\nMaximum:", timelist[5]
        print "Total wait times:"
        print "\nMinimum:", timelist[6]
        print "\nAverage:", timelist[7]/self.n
        print "\nMaximum:", timelist[8]