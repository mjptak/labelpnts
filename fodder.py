#!
"""
connecting up labels through fuzzy lines to a label point
also a use of 

"""
import math
import os


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

        
class Edge:
    def __init__(self,name,node1,node2):
        self.name = name
        self.start = node1
        self.end = node2
        self.length = dist(self.start,self.end)
        self.dir
    def locreport(self):
        return self.start.selfreport(), self.end.selfreport()
        
class Pgon:
    def __init__(self,name,edgelist):
        self.name = name
        self.edgelist = edgelist
    def locreport(self):
        return len(self.edgelist)
        
        
pnts = []
with open("labels.csv") as f:
    for line in f:
	    tmp = line.split(',')
	    pnt = Ppoint(tmp[0],tmp[1],tmp[2]) 
        #pnts.append(pnt)
tolerance = 0.1
print len(pnts)

"""
#edit out the input of b
tdist=1000000
i = 0
for oloop in a:
  tdist = 1000000
  i = 0
  for each in b:
      tdist=each.dist(oloop)
      #print pnt5.repclosest()[1],tdist
      if oloop.repclosest()[1] > tdist and tdist <> 0 :  # need to make sure that it does not select itself for the closest value
      #need to check and account for equal distance objects
          #print "caughtit"
         # print tdist
          oloop.setclosest(i,tdist)
         # print  oloop.repclosest()[1]
      i+=1
for each in a:
    print each.repclosest()[0]
"""
#c will be the area list
c=[]
#d will be the label list
#to vary what you want to pair you need to play around with arrays c and d.
d=[]
#


#need to add in checks/exemptions on inputs
#example line from labels file is described as Name, x_coord, y_coord
#  12D::RY826::001,1815308.579938647,17376387.357592974
with open("MINN2016_LABELS.csv") as f:
    for line in f:
        tmp=line.split(',')
        pnt = Ppoint(tmp[0],tmp[1],tmp[2])
        d.append(pnt)
print "The label file is %d lines long" %len(d)

# example line from areas file is described as dummy,description, area, x_coord, y_coord, Drawing_name, Layer
# 1,Hatch,26191.6985,1814374.5616,17376670.4284,Tower_12D_2016.dwg,2016 PCI
with open("MINN2016_AREAS.CSV") as f:
    for line in f:
        tmp=line.split(',')
        pnt = Ppoint(tmp[2],tmp[3],tmp[4])
        c.append(pnt)
print "The area file is %d lines long" %len(c)

for each in c:
    print "x = %s and y=%s" %(each.locreport()[0],each.locreport()[1])
tdist=1000000
i = 0
"""

"""
for oloop in c:
  tdist = 1000000
  i = 0
  for each in d:
      tdist=each.dist(oloop)
      #print pnt5.repclosest()[1],tdist
      if oloop.repclosest()[1] > tdist and tdist <> 0 :  # need to make sure that it does not select itself for the closest value
      #need to check and account for equal distance objects
      #need to work on 2-4 th closest for the flocking algorithm.  (question of ties)
          #print "caughtit"
         # print tdist
          oloop.setclosest(i,tdist)
         # print  oloop.repclosest()[1]
      i+=1

#TODO add in a filter for things that seem a bit distant.
#TODO add in a way to automatically assign the network based on a distance to another set of location points.
#TODO add in a "autocad script generator to change colors based on PCI by using the change command and the point of the label
#TODO revise the label point dxf scrubber to also include a vector direction (used in calculating the offset)
f=open('temp.out','w')
for each in c:
    print each.name, d[each.repclosest()[0]].name,each.closest_distance
    tmptext = each.name+ "," + d[each.repclosest()[0]].name + "," + str(each.closest_distance)+"\n"
    f.write(tmptext)
f.close()

#Need to report out the area, name of closest, picpoint , label point and distance between with some flag to signal potential error
#disconnect between cad areas and esri areas will signal those sections that are either multipart of have an island.
#add in libraries to deal with lat long
