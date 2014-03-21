from math import *

def fun2 (size, target, ary):
    tracker, result = {},0
    #Put everything into a hashtable
    for i in xrange(len(ary)):
       tracker[ary[i]] = 1  if (ary[i]) not in tracker else tracker[ary[i]]  +1
    #Find all the possible pair  (0, target), (1,target-1)....
    for i in xrange((int)(ceil(target/2.0))):
        if (i in tracker and target-i in tracker):
            result += min (tracker[i], tracker[target-i])
    #Encounter special case, when target is an even number
    if (target % 2 == 0 and target/2 in tracker):
        result += int(floor(tracker[target/2]/2))        
    return result

print fun2(5,8,[0,8,5,2,4,4,3])


