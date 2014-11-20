from heapq import *
import time
from sys import stdin
#Everything is negated because we want to track the largest element in a min heap. - large number makes it a small number
def dataStream ():
    size = (int)(stdin.next())
    a = [int(stdin.next())*-1 for _ in xrange(size)]
    heapify(a)
    
    for line in stdin:
        if (a[0]<((int)(line)*-1)):
            heappushpop(a,((int)(line)*-1))
    return sorted([x*-1 for x in a])

print dataStream()

        

"""
What is the complexity? Write down the detailed analysis.
O(K)
    Time to create a heap with the first K elements in the stream
    (All of the elements are * -1 so we can get the largest element in the heap in O(1) time
O(nlogk)
    Read the rest of the N-K elements one by one and replace with the smaller element if found.
    Use Heappushpop to swap the first element with the new element, this way heap property will maintain

Final Complexity is O(nlogk)
 for i in xrange(size):
        a.append()
"""


