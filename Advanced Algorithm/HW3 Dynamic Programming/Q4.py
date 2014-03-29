from heapq import heapify
import sys
def fun(st1, st2, v):
    st1 = '0' + st1
    st2 = '0' + st2
    result = {}
    for i in xrange (len(st1)):
        if (i not in result):
            result[i] = {}
        for j in xrange (len(st2)):
            if (i == 0 or j == 0):
                result[i][j] = ''
            elif (st1[i] == st2[j]):
                result[i][j] = result[i-1][j-1]+ st1[i]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
    a = []
    for i in result:
        for j in result[i]:
            if (result[i][j] != ''):
                a.append((-len(result[i][j]), result[i][j]))
    heapify(a)
    if (len(a) == 0):
        return 0
    else:
        for i in xrange(len(a)):
            ans = heappop(a)
            if ( v in ans[1]):
                continue
            else:
                return -ans[0]
        return 0

            
fun(sys.stdin,sys.stdin,sys.stdin)

'''
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            a = str.split(line, ' ')
            write.write ( fun(a[0], a[1]) +  '\n')
        write.close()
    read.close()
'''

