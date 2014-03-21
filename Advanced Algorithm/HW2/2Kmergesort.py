from heapq import *
import time
from random import randint
import sys
sys.setrecursionlimit(5000)

def kmergesort (myList, ways):
    if (len(myList)==1):
        return myList[0]
    a , b, myHeap, result= [], [], [], []
    for i in xrange(ways):
        b = myList[i::ways]
        if (len(b)>1):
            b = kmergesort(b,ways)
        if (len(b) !=0):
            a.append(b)
    #build K ways heap
    ways = min(ways, len(a))
    #each list in a is already sorted at this point
    #append ways number of element in to each list in myHeap
    myHeap = [tuple([a[i].pop(0), i])for i in xrange(ways)]
    heapify(myHeap)
    while len(myHeap)>0:
        temp = heappop(myHeap)
        result.append(temp[0])
        if (len(a[temp[1]])>0):
            heappush(myHeap, tuple([a[temp[1]].pop(0), temp[1]]))
    return result
"""
What is the complexity? Write down the detailed analysis.
Each split into K list with N elements takes about O(n) time
Get the smallest element by comparing the head of the heap = O(nlog(k)) 
We will have total log(k) level and each level has n elements

total = o(nlog(k))
"""

    
def test(a,b):
    t=time.time()
    a = kmergesort (a, b)
    print "Total" , time.time()-t
    return a

b = [4,1,5,2,6,3,7,0]
c = kmergesort([4,1,5,2,6,3,7,0,9], 4) 


d = []
for i in xrange(500):
    d.append(randint(0,100))

c =test(d, 100)




