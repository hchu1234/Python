import sys
from heapdict import *
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
      result = []

      print line
      for i in xrange(line[0]):
        result += [-1]
      
      for i in xrange[line[0]]:
        q[i] = sys.maxint

      q[0] = 0
        
      while (len(q)!= 0 ):
        item = q.popitem()

        for i in neighbor[item[0]]:
          if i in q and table[i , item[0] ]< q[i]:
            q[i] = table[i, item[0]]
            result[i] = item[0]
      
      print result
  read.close()
write.close()