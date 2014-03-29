#data pass in as an array of data
#Each Iteration should return the longest substring with its self.
#Result is a dictionary
from random import *

def _lcs(data, result):
    if (len(data) == 1):
        #Set longest path
        result.append(data)
    else:
        result = _lcs(data[:-1], result)
        result.append((previousSequence(result, data[-1])) + data[-1])
    #Find longest
    return result


def previousSequence (result, data):
    longest = ''
    for i in result[::-1]:
        if (len(longest)<len(i) and data > i[-1]):
            longest = i
    return longest
    
def topLcs (a):
    result = []
    a = chr(ord('A')-1) + a + chr(ord('z')+1)
    for i in xrange (len(a)):
            result.append((previousSequence(result, a[i])) + a[i])
    return result[-1][1:-1]

def lcs(a):
   return  _lcs (chr(ord('A')-1) + a + chr(ord('z')+1) ,  [])[-1][1:-1]

   with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            write.write ( lcs(line) +  '\n')
        write.close()
    read.close()


def readLongest(a):
    print a
    ans = ''
    current = a[-1]
    while (True):
        if (current[0] == -1):
            return ans[::-1]
        else:
            ans+=current[1]
            current = a[current[0]]
    

print  lcs('aebbcg')
print topLcs('aebbcg')

for i in xrange(10):
    a = ''
    for j in xrange(500):
        a +=  chr (randint(ord('a'), ord('z')))
    if  lcs(a)!= topLcs(a):
        print a
    else:
        print " Good answer"

####################################
'''
def _lcs(data, result):
    if (len(data) == 1):
        #Set longest path
        result.append((-1, data[0]))
    else:
        result = _lcs(data[:-1], result)
        result.append((previousSequence(result, data[-1])+1, data[-1]))
    #Find longest
    return result
def previousSequence (result, data):
    #Result = a list of (Total length, last character)
    #Data = current character
    longest = result[0]
    for i in result[::-1]:
        if (longest[0]<i[0]  and data > i[1]):
            longest = i
    return longest[0]
    
def topLcs (a):
  
    a = chr(ord('A')-1) + a + chr(ord('z')+1)
    print a
    result = [(-1, a[0])]
    for i in xrange (len(a)):
        longest = result[-1]
        for j in result[::-1]: 
            if (j[0]>longest[0]):
                longest = j
        result.append((longest[0]+1, a[i]))
    return result

def lcs(a):
   return  _lcs (chr(ord('A')-1) + a + chr(ord('z')+1) ,  [])
'''








