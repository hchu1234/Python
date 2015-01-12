from heapq import *
import time
from sys import stdin
from math import *
def fun (size, target, ary):
    result,left,right,ary = 0,0,len(ary)-1, sorted(ary)
    #Find a sum
    #Sum is too big (Left pointer move left)
    #Sum is too small (Right pointer move right)
    while (left <right):
        if (ary[left] + ary[right] > target):
            right-=1
        elif (ary[left] + ary[right] < target):
            left += 1
        else:
            left +=1
            right -=1
            result +=1
    return result
    




print fun (len(a), target , a)

