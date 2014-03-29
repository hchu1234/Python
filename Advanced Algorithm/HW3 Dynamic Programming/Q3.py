from random import *
import time
def LCS(st1, st2):
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

for i in xrange(1):
    a, b  = '', ''
    for j in xrange(randint(100,200)):
        a += chr(randint(ord('a'), ord('z')))
    for j in xrange(randint(100,200)):
        b += chr(randint(ord('a'), ord('z')))
    
    if (len(LCS(a,b)) is not len(LCSTop(a,b))):
                print 'bad'
print 'done'

"""
bbde
cebb

with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            a = str.split(line, ' ')
            write.write ( fun(a[0], a[1]) +  '\n')
        write.close()
    read.close()
"""
