import time
from random import *
from operator import itemgetter
from heapq import *
import sys
sys.setrecursionlimit (1000000)

def slowCartesian (a,b):
    return  [(i,j,i+j)for i in a for j in b]

"""Method 1 slowest Using built in sorted method and extract the first N elements"""
def nbesta(a,b):
    t=time.time()
    c = slowCartesian(a,b)
    d= [(j[0],j[1]) for j in sorted(c,key = itemgetter(2,1))[:len(a)]]
    print "slowest", time.time() - t
    return d

"""Method 2 Using quick select to find the first N elements"""
def _qselect(n, arr):
    if arr == []:
        return []
    pivot = randint (0, len(arr)-1)
    rest = arr[:pivot] + arr[pivot+1:]
    left = [x for x in rest if x[2] < arr[pivot][2]]
    if (len(left)>n):
        return _qselect(n,left)
    elif (len(left)==n):
        return left
    else:
        right = [x for x in rest if x[2] >= arr[pivot][2]]
        return left + [arr[pivot]] + _qselect(n-len(left)-1,right)
    
def nbestb(a,b):
    t=time.time()
    d = _qselect(len(a),slowCartesian(a,b))
    d = sorted (d, key = itemgetter(2,1))
    print "slow", time.time()-t
    return [(x[0],x[1]) for x in d]

"""Medthod 3 Using Heap """
def nbestc (a,b):
    t=time.time()
    a, b, myHeap, tracker, result  = sorted(a), sorted(b), [], {}, []
    #Base case, first number in heap
    tracker[0,0] = (b[0] + a[0], 0,0)
    heappush(myHeap, tracker[0,0])
    while (len(result) < len(a)):
        temp = heappop(myHeap)
        result.append(temp) 
        if ((temp[1]+1,temp[2]) not in tracker):
            tracker[temp[1]+1, temp[2]] = ( b[temp[1]+1] + a[temp[2]], temp[1]+1,temp[2])
            heappush(myHeap, tracker[temp[1]+1, temp[2]])

        if ((temp[1],temp[2]+1) not in tracker):
            tracker[temp[1], temp[2]+1] = ((b[temp[1]] + a[temp[2]+1]), temp[1],temp[2]+1)
            heappush(myHeap, tracker[temp[1], temp[2]+1])

    result = [(a[i[1][-1]],b[i[1][1]]) for i in enumerate(result)]
    print "fast", time.time()-t
    return result

a, b = [4, 1, 5, 3], [2, 6, 3, 4]

def test (numTrials):
    for trial in range(numTrials):
        a = [randint(0,100) for x in xrange(5000)]
        b = [randint(0,100) for x in xrange(5000)]
        nbesta(a,b)
        nbestb(a,b)
        nbestc(a,b)


"""Comment area
What are the complexities of these algorithms?
Complexity 1:
O(n^2) to get cartesian product
O(2n^2log(n) to sort n^2 list
O(n) to rearrange the print order
Total = O(n^2)

Complexity 2:
O(n^2) to get cartesian product
O(logn) to get the n element in the list
O(nlogn) to sort the n element
Total = O(n^2)

Complexity 3:
O(n) to get n caresian product
O(nlogn) to build heap with n element
O(n) to rearrange the print order
Total = O(nlogn)

Randomly generate two lists of n=5000 and report the running time of each.

"""
