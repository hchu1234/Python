#data pass in as an array of data
#Each Iteration should return the longest substring with its self.
#Result is a dictionary
from random import *

def _TopLCS(data, result):
    
    if (len(data) == 1):
        #Set longest path
        result.append(data)
    else:
        result = _TopLCS(data[:-1], result)
        result.append((previousSequence(result, data[-1])) + data[-1])
    #Find longest
    return result



def previousSequence (result, data):
    longest = ''
    for i in result[::-1]:
        if (len(longest)<len(i) and data > i[-1]):
            longest = i
    return longest



def TopLCS(a):
   return  _TopLCS (chr(ord('A')-1) + a + chr(ord('z')+1),[])[-1][1:-1]


with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            write.write ( TopLCS(line) +  '\n')
        write.close()
    read.close()









