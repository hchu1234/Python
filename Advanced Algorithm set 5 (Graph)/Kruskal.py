from heapq import *
from heapdict import *
import sys


with open("output2.txt", "w") as write:
  with open(sys.argv[1] , "r") as  read:


    while (True):
      line = read.readline()
      line = line.split ()
      line = [int(line[0]) , int(line[1])]
      #print line
      
      if (line[0] == -1):
        break
      else:
        data = read.readline()
        data = data.split()

        table = []
        neighbor = {}
        for i in xrange(line[0]):
          neighbor[i] = []

        for i in xrange(len(data)):
          data[i] = data[i].split(":")
          data[i][0] = data[i][0].split("-")
          data[i][0] = [int(data[i][0][0]) , int(data[i][0][1])]

          neighbor[data[i][0][0]] = neighbor[data[i][0][0]] + [data[i][0][1]]
          neighbor[data[i][0][1]] = neighbor[data[i][0][1]] + [data[i][0][0]]

          table  += [[int(data[i][1]) , (data[i][0][0] , data[i][0][1])]]
          #table [data[i][0][1] , data[i][0][0]] = int(data[i][1])

          #weigh, edge
        #print len(table)  , "This should be total edge"
        heapify (table)
        #all set
        result = []
        total = 1
        for i in xrange(line[0]):
        	result +=[[i,{}]]
        #print result , " result DONE"
        #MSP is a free tree. Free tree has Node -1 edge

        while (True):
        	#minEdge = cast , (e1 , e2)
        	minEdge = heappop(table)
        	
        	#print minEdge
        	##Yes Cycle

        	if (result[minEdge[1][1]][0] is result[minEdge[1][0]][0] ):
        		True == True
        		#print "Cycle"
        		#print len(table) , "LENGTH OF TABLE"
        		#print total  , "TOTAL "
        		

        	else:
        		##not cycle
        		##Copy everythong over.

        		temp = [ result[minEdge[1][1]][0] ,{}]

        		temp[1][ minEdge[1][0] , minEdge[1][1] ] = minEdge[0]
        		#print "temp is " , temp
        		for i in result[minEdge[1][1]][1]:
        			if i not in temp[1]:
        				temp[1][i] = result[minEdge[1][1]][1][i]
        		for i in result[minEdge[1][0]][1]:
        			if i not in temp[1]:
        				temp[1][i] = result[minEdge[1][0]][1][i]

        		#print "after copy  temp is ", temp
        		#Update all with the temp color

        		color = result[minEdge[1][1]][0]
        		color2 = result[minEdge[1][0]][0]
        		#print color  , "Left color is "
        		#print color2 , "Right color is "

        		for i in xrange(len(result)):        			
        			if result[i][0] == color or color2  == result[i][0] :
        				result[i] = temp
        				

        		total +=1
        	#print len(table) , "LENGTH OF TABLE"
        	#print total  , "TOTAL "
        	
        	if total is line[0]:
        		totalCost = 0
        		print result[minEdge[1][0]]
        		q = heapdict()
        		for i in result[minEdge[1][0]][1]:
        			totalCost += result[minEdge[1][0]][1][i]
        			print result[minEdge[1][0]][1][i]
        			q[i] =  result[minEdge[1][0]][1][i]

        		result = "" 
        		while (len(q) >1):
        			item = q.popitem()
        			result += ("%s %s" % (item[0], item[1])).replace (", " , "-").replace (") ", ":").replace("(" , " ")
        		print totalCost , result
        		break
        	elif (len(table) == 0):
        		print "NO SPANNING TREE"
        		break
  read.close
write.close




        		
        	











