from random import randint

def qselect (index,  myList):
    if myList ==[]:
        return []
    pivot = randint(0,len(myList)-1)
    removePivot = myList[:pivot] + myList[pivot+1:]
    left = [item for item in removePivot if item < myList[pivot]]
    pIndex = len(left)+1
   
    if pIndex== index:
        return myList[pivot]
    elif (pIndex>index):
        return qselect ( index, left)
    else:
        right = [item for item in removePivot if item > myList[pivot]]
        return qselect (index-len(left)-1, right)

a = [2,2,2,2,5,6,8,15,16,17,18]
