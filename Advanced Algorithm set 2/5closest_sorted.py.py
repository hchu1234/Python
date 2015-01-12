import sys
from math import ceil
from bisect import *

def find (ary, target, resultSize):
    #Empty Result, ary with min int and max int wrapped, first element greater than target and last element smaller than target
    result, ary, right = [], [-sys.maxint -1] + ary + [sys.maxint], bisect_right(ary,target)
    left = right-1
    #Conintue only we didn't have resultSize AND we still have element availble in the list
    while ( resultSize !=0) and (left!=0 or right != len(ary)-1):
        #if the left element is closer to target, get left
        if ary[right]- target > -(ary[left]-target):
            result.append(ary[left])
            left = left-1;
        else:
            result.append(ary[right])
            right = right +1
        resultSize -= 1
    return result
 


print find([1,2,3,4,4,7], 5.2, 2)
print find([1,2,3,4,4,7], 6.5, 3)
