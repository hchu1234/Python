import sys
from operator import *
from heapq import*

def find (ary, target, element):
    if element>len(ary):
        return ary
    a,result = [],[]
        #Tuple of the distance from that element to target, value of element, index of element
    a = [(tuple([abs(ary[i]-target),ary[i],i])) for i in xrange(len(ary))]
    heapify(a)
    #Pop elements time to get the result list, sorted by index and extract the value of ary
    return [i[1] for i in (sorted([heappop(a) for i in xrange(element)], key = itemgetter(2)))]

print find([4,1,3,2,7,4], 5.2, 2)
print find([4,1,3,2,7,4], 6.5, 3)



"""
n, q = map(int, raw_input().split())
a = (int, raw_input().split())
    for i in xrange(len(ary)):
        #Tuple of the distance from that element to target, value of element, index of element
        a.append(tuple([abs(ary[i]-target),ary[i],i]))
"""
