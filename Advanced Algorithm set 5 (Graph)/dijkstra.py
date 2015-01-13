from heapq import *
from heapdict import *
import sys

#print 'Argument List:', str(sys.argv)

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

        table = {}
        neighbor = {}
        for i in xrange(line[0]):
          neighbor[i] = []

        for i in xrange(len(data)):
          data[i] = data[i].split(":")
          data[i][0] = data[i][0].split("-")
          data[i][0] = [int(data[i][0][0]) , int(data[i][0][1])]

          neighbor[data[i][0][0]] = neighbor[data[i][0][0]] + [data[i][0][1]]
          neighbor[data[i][0][1]] = neighbor[data[i][0][1]] + [data[i][0][0]]

          table [data[i][0][0] , data[i][0][1]] = int(data[i][1])
          table [data[i][0][1] , data[i][0][0]] = int(data[i][1])

        q = heapdict()
        q[0] = 0
        for i in xrange(1, line[0]):
          q[i] = sys.maxint

        while (True):
          item = q.popitem()



          if (item[0] is line[0]-1):
            if (item[1] is sys.maxint):
              print "unreachable"
            else:
              print item[1]
            break;

          #Check all neighbor:
          for i in neighbor[item[0]]:
            if i in q and (item[0] , i) in table:
              q[i] = min (item[1] + table[item[0] , i] , q[i])
                  
  read.close()
write.close()



"""
Since input is not specify, I wil assume that the input is the simeile as q1 which is and each line represent one graph

0-1:1 0-2:4 1-2:2

"""