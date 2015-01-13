##For loop
from random import *
import time
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


with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            st1, st2 = line.split()
            write.write ( LCSBottom(st1, st2) +  '\n')
        write.close()
    read.close()
