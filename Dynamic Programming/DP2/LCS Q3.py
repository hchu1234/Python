##Bottom up Recursion 

from random import *
import time



#####################################################################################################################

def _LCSTop(st1, st2, resultList):
    if len(st1) in resultList and len(st2) in resultList[len(st1)]:
        return resultList
    if len(st1) not in resultList:
        resultList[len(st1)] = {}        
    if (len(st1) == 0 or len(st2) ==0):
        resultList[len(st1)][len(st2)] = (0, '')
    else:
        if (st1[-1] == st2[-1]):
            resultList = _LCSTop(st1[:-1], st2[:-1], resultList)
            resultList[len(st1)][len(st2)] = (resultList[len(st1)-1][len(st2)-1][0]+1, resultList[len(st1)-1][len(st2)-1][1] + st1[-1])
        else:
            resultList = _LCSTop(st1[:-1], st2, resultList)
            resultList = _LCSTop(st1, st2[:-1], resultList)
            resultList[len(st1)][len(st2)] =  max (resultList[len(st1)-1][len(st2)], resultList[len(st1)][len(st2)-1] )
    return resultList

def LCSTop(st1, st2):
    resultList = {}
    _LCSTop( st1, st2, resultList)
    return resultList[len(st1)][len(st2)][1] if resultList[len(st1)][len(st2)][1] is not  '' else 'No LCS'



with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            st1, st2 = line.split()
            write.write ( LCS(st1, st2) +  '\n')
        write.close()
    read.close()


"""
top down is about 5 times faster when both input is the same.
a = 'a'*100
b = a
0.125
0.0149998664856

Bottom top  is about 5 times faster when the result is No CLS
a = 'a'*100
b = 'b'*100



def LCSBottom(st1, st2):
    st1, st2, result = '0' + st1  , '0'+ st2 , {}
    for i in xrange (len(st1)):
        if (i not in result):
            result[i] = {}   
        for j in xrange (len(st2)):
            if (i == 0 or j == 0):
                result[i][j] = ''
            elif (st1[i] == st2[j]):
                result[i][j] = result[i-1][j-1]+ st1[i]
            else:
                result[i][j] = result[i-1][j] if (len(result[i-1][j]) > len ( result[i][j-1])) else result[i][j-1]

    if (result[len(st1)-1][len(st2)-1] == ''):
        return 'No LCS'
    else:
        return result[len(st1)-1][len(st2)-1]
for i in xrange(1):
    a, b  = '', ''
    for j in xrange(randint(300,300)):
        a += chr(randint(ord('a'), ord('i')))
    for j in xrange(randint(300,300)):
        b += chr(randint(ord('a'), ord('i')))
        
    print a, b

    t = time.time()
    print LCSBottom(a,a)
    print time.time() - t

    t = time.time()
    print LCSTop(a,a)
    print time.time() - t
    print '\n\n'

    a = 'a'*300
    b = 'b'*300
    t = time.time()
    print LCSBottom(a,b)
    print time.time() - t

    t = time.time()
    print LCSTop(a,b)
    print time.time() - t
    print '\n\n'

"""
