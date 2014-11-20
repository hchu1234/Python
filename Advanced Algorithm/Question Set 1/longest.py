import math
def longest (tree):
     a=  _longest (tree)
     return [a[0]-1,a[2]]

def _longest (tree):
    if tree == []:
        return [0,0,[],[]]
    else:
        left = _longest (tree[0])
        right = _longest(tree[2])
            
    if left[0] >= right[0] and left[0] >= left[1]+right[1]+1:
        path = left[2]
    elif right[0]>left[0] and right[0] > left[1]+right[1]+1:
        path = right[2]
    else:
        path = left[3] + [tree[1]] + right[3][::-1]
        #Length of longest path, ??? , Longest path, 
    return [max (left[0], right[0], left[1]+right[1]+1), max(left[1], right[1]) +1, path ,left[3]+ [tree[1]] if left[1] >= right[1] else  right[3] +  [tree[1]]]

print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])


"""
longest path
longest depth
longest path by left, right, or the combinet or left and right depth +1
depth by max of left or right + 1

"""


