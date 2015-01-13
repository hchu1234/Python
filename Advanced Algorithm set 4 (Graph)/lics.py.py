import sys
import heapq
##For loop

from random import *
import time
import heapq
def LICS(st1, st2):
    st1, st2, result = '0' + st1  , '0'+ st2 , {}
    for i in xrange (len(st1)):
        for j in xrange (len(st2)):
            result [i,j]= []
            if (i == 0 or j == 0):
                result[i , j] = []
            #Append st1[i] in to all item in result [i-1, j-1].. only those who are increaing.
            elif (st1[i] == st2[j]):
                for k in result[i-1,j-1]:
                    if (k[-1] < st1[i]):
                        result[i,j].append(k+st1[i])
                    else:
                        result[i,j].append(k)
                        
                result[i,j].append(st1[i])
        		
                    
            #get all distince value from result[i-1,j] and result[i,j-1]
            else:
                for k in result[i-1,j]:
                    if (k not in result[i,j]):
                        result[i,j].append(k)

                for k in result[i,j-1]:
                    if (k not in result[i,j]):
                        result[i,j].append(k)

    if (result[len(st1)-1,len(st2)-1] == []):
        return 'No LICS'
    else:
        return max(result[len(st1)-1,len(st2)-1], key = len)
    
with open("output.txt", "w") as write:
    for i in sys.stdin.xreadlines():
        st1, st2 = i.split()
        ans =  LICS(st1, st2)
        print ans
        write.write(ans  +'\n')
    write.close()

''' 
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            st1, st2 = line.split()
            print LICS(st1, st2)
        write.close()
    read.close()
'''
