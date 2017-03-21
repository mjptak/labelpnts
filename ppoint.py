#!
"""
connecting up labels through fuzzy lines to a label point
also a use of git
Next step.   naming points and then deciding if labels should be associated with a leader or not (some aren't)

key variable list:
pntsdict is the label points dictionary
lpntdict2 is the leader endnode points dictionary where the names are auto generated (probably better to name them by location) 
todo need to check for stripping of the whitespace
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
        #self.length = dist(self.start,self.end)
        #self.dir
    def locreport(self):
        return self.start.selfreport(), self.end.selfreport()
        
#each Pgon is given a name and a list of edges 
class Pgon:
    def __init__(self,name,edgelist):
        self.name = name
        self.edgelist = edgelist
    def locreport(self):
        return len(self.edgelist)

#readLines brings in the leader lines       
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
                    if pntcnt not in lpntdict:
                        lpntdict[pntcnt] = Ppoint(pntcnt,epnt[0],epnt[1])
                    else:
                        print "%s has a duplicate label" %pntcnt
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

#read and process labels file for insertion points and values of labels
#store them in pntsdict
#probably better to move to a function!
with open("2013_labels.csv") as f:
    for line in f:
        #print line
        tmp = line.split(',')
        pnt = Ppoint(tmp[4].strip(),tmp[2],tmp[3])
        #check for duplicate labels before storing by cycling through keys
        pntsdict[pnt.locreport()[0]] = pnt


lpntdict2 = readLines()  






for k,v in lpntdict2.iteritems():
    #print k,v.locreport()
    continue

print "there are %s labels and %s endpoints in leaders" %(len(pntsdict),len(lpntdict2))  #count looks low
#not just build flatter lists
clabs =[]
cpnts = []

#clabs and cpnts are lists of label points and leader nodes
for k,v in pntsdict.iteritems():
    clabs.append(v)
for k,v in lpntdict2.iteritems():
    cpnts.append(v)
""" 
#move this till after figuring out the dangling nodes
for each in clabs:
    icnt = 0
    for indv in cpnts:
        if each.dist(indv) < each.closest_distance:
            each.setclosest(icnt,each.dist(indv))
        icnt +=1
            
for each in clabs:
    print each.name, each.closest_distance#this should be the distance to the closest leader endpoint
"""
#probably a much cleaner way to encapsulate points
#looping through a set of lines and looking for things that connect until you reach the end.
#for not just reopen the line file and cycle through defining the endpoints by the name

#poor implementation but reopen the leader files in order to tie lines to nodes
#edgelist is a list of all the leader lines defined by beginning and ending nodes.
edgelist=[]
with open("2013_leaders.csv") as g:
    for line in g:
        a = line.split(',')
        tpnt = (float(a[2]),float(a[3]))
        for k,v in lpntdict2.iteritems():
            dist = ((v.locreport()[1] - tpnt[0])**2 + (v.locreport()[2]-tpnt[1])**2)**0.5
            if dist < 0.01:
                startnode = lpntdict2[k]
           
        tpnt = (float(a[4]),float(a[5]))
        for k,v in lpntdict2.iteritems():
            dist = ((v.locreport()[1] - tpnt[0])**2 + (v.locreport()[2]-tpnt[1])**2)**0.5
            if dist < 0.01:
                endnode = lpntdict2[k]
        print a[0],startnode.name,endnode.name
        a = Edge(a[0],startnode,endnode)
        edgelist.append(a)
print "there are %s edges of varying lengths in the leader file" %len(edgelist)
"""
#no need to do the connect list until you have the dangling nodes
connectlist =[]
for each in edgelist:
    for inv in edgelist:
        if each.start == inv.start or each.start == inv.end:
            if each.start == inv.start and each.end == inv.end:
                continue
            else:
                connectlist.append([each,inv])
"""
                
                #build just the endpoints
#go through and count the occurences of each node name
nodekeydict ={}
for each in edgelist:
    if each.start.name not in nodekeydict:
        nodekeydict[each.start.name] = 1
    else:
        nodekeydict[each.start.name] = nodekeydict[each.start.name] + 1
    if each.end.name not in nodekeydict:
        nodekeydict[each.end.name] = 1
    else:
        nodekeydict[each.end.name] = nodekeydict[each.end.name] + 1
hanglist=[]
endcnt= 0
for k,v in nodekeydict.iteritems():
    if v < 2:
        endcnt+=1
        hanglist.append(k)
        
#might be useful to delete or flag nodes that are connected to more than 3 links
#hanglist is a list of the leader point nodes that are connected to a single link
hanglist.sort()
firstnode ={}
for k,v in pntsdict.iteritems():
    mindist = 1000000
    minnode = 9999
    for each in hanglist:
        checkdist = v.dist(lpntdict2[each])
        if checkdist < mindist:
            mindist = checkdist
            minnode = each
    if mindist < 10000:
        firstnode[k.strip()] = [minnode, mindist]
    else:
        print "label %s does not have a leader nearby" %k
for k,v in firstnode.iteritems():
    print pntsdict[k].locreport()[1:3], lpntdict2[v[0]].locreport()[1:3]      
        
#print len(nodekeydict), len(edgelist), len (pntsdict), endcnt
        
if __name__ == "__main__":
    print("ppoint.py is being run directly")
else:
    print("ppoint.py is being imported into another module")

