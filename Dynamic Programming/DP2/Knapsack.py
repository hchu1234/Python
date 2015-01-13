
def knapsack(numberOfItem, totalWeight, items, memory, back):    
    if totalWeight <= 0 or numberOfItem == 0:
        return 0
    elif (totalWeight, numberOfItem) in memory:
        return memory[totalWeight, numberOfItem]
    else:
        biggest, totalItem = 0,0
        for i in xrange(items[numberOfItem-1][-1]+1):
            if (totalWeight >= i*items[numberOfItem-1][0]):
                a = knapsack(numberOfItem-1, totalWeight-items[numberOfItem-1][0]*i, items, memory, back)+items[numberOfItem-1][1]*i
            if (a >= biggest):
                biggest = a
                totalItem = i
        memory[totalWeight, numberOfItem] = biggest
        back[totalWeight, numberOfItem] = totalItem
    return biggest
   
def backtrace(numberOfItem, w, items, back):
    if numberOfItem == 0:
        return []
    if (w, numberOfItem) in back:
        return backtrace(numberOfItem-1, w-items[numberOfItem-1][0]*back[w,numberOfItem], items, back) + [back[w, numberOfItem]]
    else:
        return backtrace(numberOfItem-1, w, items, back) + [0]
         
a = 3
b = 5
items = [[2,4,3],[2,4,3],[2,4,3]]
#Weight Volume, Quantity
memory = {}
back = {}
print knapsack(a,b,items, memory, back)
print backtrace(a,b,items,back)



##
##def topKnapsack(numberOfItem, totalWeight, items):
##    result = {}
##    ##Total weight from 0 to MAX Weight
##    for i in xrange(totalWeight+1):
##        ##Number Of item from 0 to total Item
##        for j in xrange(0, numberOfItem):
##            ##0 copy to n copy of item[j]
##            for l in xrange(items[j][-1]):
##                if (totalWeight > l[1]):
##                            
##                            
                
                


###Read file
    ##        content[i][j] =  int(content[i][j])
##maxWeight = content[0][1]
##maxItem = content[0][0]
##items = content[1:]
##
##print knapsack(maxItem, maxWeight ,items)

"""


item = content[1:]
#Flatten the problem
flatData = []

for i in xrange(len(item)):++
     for j in xrange(item[i][2]):
          flatData.append((item[i][0], item[i][1]))
print flatData
totalItem = len(flatData)

def knapsack (totalWeight, totalItem, allItems):
    print "Call"
    if( totalWeight <= 0 or totalItem == 0 ):
        return 0; #best volume = 0

    a =    max(knapsack(totalWeight, totalItem-1, allItems[:-1:]) , knapsack(totalWeight- allItems[-1][0], totalItem-1, allItems[:-1:])+allItems[-1][1])
    print a
    return a
    #Base case is when totalWeight = 0 or total Item = 0

print knapsack(maxWeight, maxItem, flatData)
    #Either not getting any item remainn the same Weight or get Item and have a lower weight with reward of the volume

        n , w
    Wi, Vi, Ci
    
"""
