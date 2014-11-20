
def knapsack(numberOfItem, totalWeigh, items):

    if totalWeigh <= 0 or len(items)==0:
        return 0
    else: 
        if (items[-1][2]==1):
            result =  max((knapsack(numberOfItem-1, totalWeigh-items[-1][0], items[:-1])+items[-1][1]), knapsack(numberOfItem-1, totalWeigh, items[:-1]))
            return result
        elif (items[-1] >= 2):
            items[-1][2] = items[-1][2]-1
            result =  max((knapsack(numberOfItem, totalWeigh-items[-1][0], items)+items[-1][1]), knapsack(numberOfItem, totalWeigh, items))
            return result
                         
    



#Read file
with open ("input.txt") as infile:
    content  = infile.readlines();
    content = [i.replace('\n', '').split( ' ') for i in content]

for i in xrange(len(content)):
    for j in xrange(len(content[i])):
        content[i][j] =  int(content[i][j])
maxWeight = content[0][1]
maxItem = content[0][0]
items = content[1:]

print knapsack(maxItem, maxWeight ,items)


"""
a = 2
b = 3
items = [[2,4,1],[2,5,1]]

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
