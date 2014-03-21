import sys;
sys.setrecursionlimit (1000000)

cache = {}
def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1, A(m,n-1))

def A2 (m,n):
    if m in cache and n in cache[m]:
        return cache[m][n]
    else:
        if m not in cache:
            cache[m] = {}
        if m==0:
            return n+1
        elif m>0 and n==0:
            cache[m][n] = A2(m-1,1)
        elif m > 0 and n > 0:
            cache[m][n] = A2(m-1, A2(m,n-1))
        return cache[m][n]

print "A(3,10)"
print A(3,10)

print"A2(3,10)"
print A2(3,10)

print "A(4,0)"
print A(4,0)

print "A2(4,1)"
print A2(4,1)


"""
3,5
Non cache = 42438
Cached = 766
"""
