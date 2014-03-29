from heapq import heapify
from heapq import heappop
import sys

def fun(st1, st2, v):
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
#Try to use deafultdict
    a = []
    for i in result:
        for j in result[i]:
            if (result[i][j] != ''):
                a.append((-len(result[i][j]), result[i][j]))
    return a
    if (len(a) == 0):
        return 0
    else:
        heapify(a)
        for i in xrange(len(a)):
            ans = heappop(a)
            if ( v in ans[1]):
                continue
            else:
                return ans[1]
        return 0

            
a = 'QNHRPFYMAAPJDUHBAEXNEEZSTMYHVGQPYKNMVKMBVSVLIYGUVMJHEFLJEPIWFHSLISTGOKRXNMSCXYKMAXBPKCOCNTIRPCUEPHXM'
b = 'RRFCZUGFDRKKMQTOETNELXMEWGOCDHFKIXOPVHHEWTCDNXVFKFKTKNWKEIKTCMHMHDNCLLVQSGKHBCDDYVVVQIRPZEOPUGQUGRHH'
c = 'R'
'''.
AJKEQSLOBSROFGZ
OVGURWZLWVLUXTH
OZ
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            a = str.split(line, ' ')
            write.write ( fun(a[0], a[1]) +  '\n')
        write.close()
    read.close()
'''

