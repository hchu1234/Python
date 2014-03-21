
tree= [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
	
def sorted (a):
        if a==[]:
                return []
        else:
                return sorted (a[0] ) + [a[1] ]+ sorted (a[2])

def search (tree, num):
    if tree == []:
            return False
    elif tree[1] == num:
            return True
    elif tree[1]<num:
            return search (tree[2], num)
    elif tree[1]>num:
            return search (tree[0], num)


def insert (tree, num):
    if tree == []:
        return  [[] ,num ,[]]
    elif tree[1] == num:
        return tree;
    elif tree[1] <  num:
        tree[2] = insert (tree[2], num)
    else:
        tree[0] = insert (tree[0],num)
    return tree



































                
        
