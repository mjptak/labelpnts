#!
"""
connecting up labels through fuzzy lines to a label point
also a use of git
Next step.   naming points and then deciding if labels should be associated with a leader or not (some aren't)

"""



#each point is described by name, x_coord, y_coord.
class Ppoint:
    def __init__(self,name,xval,yval):
        self.closest_index=1000000
        self.closest_distance=100000000
        self.close_2_index=1000000
        self.close_2_distance=100000000
        self.coords = [float(xval),float(yval)]
        self.name = name
    def locreport(self):
       return (self.name,self.coords[0],self.coords[1])
    def separation(self,other):
      if len(self)  == len(other):
          return self.dist(other)
    def nspace(self):
        return len(self.coords)
    def dist(self,other):
      return ((self.coords[0]-other.coords[0])**2 + (self.coords[1]-other.coords[1])**2)**0.5
    def setclosest(self,index,distance):
        self.closest_index = index
        self.closest_distance = distance
    def repclosest(self):
        return [self.closest_index, self.closest_distance]

#each edge is given a name and defined by two point objects
class Edge:
    def __init__(self,name,node1,node2):
        self.name = name
        self.start = node1
        self.end = node2
        self.length = dist(self.start,self.end)
        self.dir
    def locreport(self):
        return self.start.selfreport(), self.end.selfreport()
        
#each Pgon is given a name and a list of edges 
class Pgon:
    def __init__(self,name,edgelist):
        self.name = name
        self.edgelist = edgelist
    def locreport(self):
        return len(self.edgelist)
def readLines():
    llist=[]
    lcnt = 0
    plist = []
    pntdict={}
    pntcnt = 0
    lpntdict={}
    with open("2013_leaders.csv") as g:
        linecnt = 0
        pntcnt = 0
        for line in g:
            a = line.split(',')
            try:
                spnt = (float(a[2]),float(a[3]))
                if spnt not in plist:
                    plist.append(spnt)
                    lpntdict[pntcnt] = Ppoint(pntcnt,spnt[0],spnt[1])
                    pntcnt+=1
            except:
                continue
            try:
                epnt = (float(a[4]),float(a[5]))
                if epnt not in plist:
                    plist.append(epnt)
                    lpntdict[pntcnt] = Ppoint(pntcnt,epnt[0],epnt[1])
                    pntcnt+=1
            except:
                continue
            lcnt+=1
    print "total number of leader segments = %s" %lcnt
    return lpntdict # todo:  add in the line library where lines are defined from node# to node #  _check for direction
                    
        

#begin main program
import math
import os
        
pntsdict = {}
with open("2013_labels.csv") as f:
    for line in f:
        #print line
        tmp = line.split(',')
        pnt = Ppoint(tmp[4],tmp[2],tmp[3])
        #check for duplicate labels before storing by cycling through keys
        pntsdict[pnt.locreport()[0]] = pnt

tolerance = 0.1
print len(pntsdict)
lpntdict2 = readLines()  
print len (lpntdict2)



for k,v in pntsdict.iteritems():
    print k,v.locreport()[0]
    continue

for k,v in lpntdict2.iteritems():
    print k,v.locreport()

print "there are %s labels and %s endpoints in leaders" %(len(pntsdict),len(lpntdict2))  #count looks low


#probably a much cleaner way to encapsulate points

if __name__ == "__main__":
    print("ppoint.py is being run directly")
else:
    print("ppoint.py is being imported into another module")
