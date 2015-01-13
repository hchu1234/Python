from heapq import *
from heapdict import *
import sys

print 'Argument List:', str(sys.argv)

with open("output2.txt", "w") as write:
  with open(sys.argv[1] , "r") as  read:


    while (True):
      line = read.readline()
      line = line.split ()
      line = [int(line[0]) , int(line[1])]
      print line
      
      if (line[0] == -1):
        break
      else:
        data = read.readline()
        data = data.split()
        

          #Create adjance table and neighbor
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


        #print neighbor
        #print table
        
        print table , "\n"
        print neighbor , "\n"

        result = [[0, True, 0]]
        for i in xrange(line[0]-1):
          result += [[sys.maxint , False, i+1]]

        
        minResult = result[0]
        print result
        while (True):
          #get adjance
          minResult[1] = True
          #print result
          print minResult 
          for i in neighbor[minResult[0]]:
            result[i][0] = min ( result[i][0] , minResult[0] + table[minResult[0] ,i])

          #get next min
          
          #print "min is " , minResult
          minResult = [sys.maxint , True , -1]
          for i in result:
            if (i[1]):
              continue
            else:
              if (minResult[0] > i[0]):
                minResult = i

          if (minResult[1]):
            print "unreachable"
            break
          else:
            if (minResult[2] is line[0]-1):
              print minResult[0] 
              break
  read.close()
write.close()



"""
Since input is not specify, I wil assume that the input is the simeile as q1 which is and each line represent one graph

0-1:1 0-2:4 1-2:2

"""