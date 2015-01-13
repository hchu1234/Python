import sys
from random import *
from heapq import *
import time
def LCSQ(st1, st2, q):
    st1, st2, result = '0' + st1  , '0'+ st2 , {}
    resultList = []
    for i in xrange (len(st1)):
        if (i not in result):
            result[i] = {}   
        for j in xrange (len(st2)):
            if j not in result[i]:
                result[i][j] = []
            if (i == 0 or j == 0):
                result[i][j].append( (0, ''))

                #Get everything from result[i-1][j-1]. Increase state number if st[1] match corrent state.
            elif (st1[i] == st2[j]):
                    for x in result[i-1][j-1]:
                        if (q[x[0]] == st1[i]):
                            result[i][j].append((x[0]+1 ,x[1]+ st1[i]))
                        else:
                            result[i][j].append((x[0],x[1]+ st1[i]))
            else:
                #Get distince copy from result[i-1][j] and result[i][j-1]
                    for x in result[i][j-1]:
                        if (x not in result[i][j]):
                            result[i][j].append(x)
                    for x in result[i-1][j]:
                        if (x not in result[i][j]):
                            result[i][j].append(x)
            
    
    result[i][j] = [(-x[0], -len(x[1]), x[1]) for x in result[i][j]]
    heapify(result[i][j])

    if (result[i][j][0][0] != -len(q)):
            return "NO LCS"
    else:
            return result[i][j][0][-1]
'''
    #print result
    print type(result)
    dictlist = []
    for key, value in result.iteritems():
        temp = [key,value]
        dictlist.append(temp)

    for i in dictlist:
        print i

    def LCS(st1, st2, q):
    st1, st2, result = '0' + st1  , '0'+ st2 , []
    state =  0
    for i in xrange (len(st1)):
        if (len(result) < i):
            result.append([])
        for j in xrange (len(st2)):
            if (len(result[i])<j):
                result.append([]):
            for l in xrange(len(q)):
                if (len(result[j]) < l):
                    result.append([])
                if (st1[i] == st2[j]):
                    result[i][j][l] = 

                    wasxb wsxab ab
'''   

with open("output4.txt", "w") as write:
    for i in sys.stdin.xreadlines():
        st1, st2, q = i.split()
        ans =  LCSQ(st1, st2, q)
        print ans
        write.write(ans  +'\n')
write.close()
 

'''
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            st1, st2, q = line.split()
            write.write( LCSQ(st1, st2, q) + '\n')
        write.close()
    read.close()
    
'''
