import sys
def matrix2( allMatrix):
    #Base case. 1 Matrix = 0 calculation
    b = {}
    for i  in xrange(len(allMatrix)+1):
        if i == 0:
            continue
        for j  in xrange(len(allMatrix)+1):
            if j == 0:
                continue
            if i == j:
                 b[i,j] = 0
            else:
                b[i,j] ,k = 0, i+1
                minCal = sys.maxint
                for k in xrange(i , j):
                    temp = b[i,k] + b[k+1,j] + allMatrix[i][0]*allMatrix[k][1]*allMatrix[j][1]
                    if (minCal > temp):
                        minCal = temp
                b[i,j] = minCal

            print b    
    return b[1,len(allMatrix)]
'''
def matrix3 (allMatrix):
    b = {}
    for i in xrange(1,len(allMatrix)+1):
        b[i] = {}
        for j in xrange(1, len(allMatrix)+1):
            b[i][j] = 0

    print b

    for l in xrange(2,len(allMatrix)):
        for i in xrange(1, len(allMatrix)-l+2):
            j = i+l-1
            b[i][j] = sys.maxint 
            for k in xrange(i,j):
                temp = b[i][k] + b[k+1][j] + allMatrix[i][0]* allMatrix[k][1]*allMatrix[j][1]
                if temp < b[i][j]:
                    b[i][j] = temp
            print b
    print b 
    #return b[1][len(allMatrix)]
'''
def matrix3 (allMatrix):
    b = {}
    for i in xrange(1, len(allMatrix)+1):
        b[i] = {}
        for j in xrange(1, len(allMatrix)+1):
            b[i][j] = sys.maxint

    for length in xrange(  len(allMatrix)):
        for i in xrange(1, len(allMatrix)-length+1):
            print i , i + length , " is here"
            if length is 0:
                b[i][i] = 0

            
            else:
                for k in xrange(i , len(allMatrix) - length + 1):
                    print i , k , 
                    #temp = b[i][k+1] + b[k+1][j]
                    #temp +=  allMatrix [i][0] * allMatrix[k+1][1]*allMatrix[j][1]
                    #if temp < b[i][j]:
                    #    b[i][j] = temp
    print b 
    
    #return b[1][len(allMatrix)]

def matrix( allMatrix, i , j):
    if (i == j):
        return 0
    minCal = sys.maxint
    for k in xrange(i,j):
        t = matrix(allMatrix,i,k) + matrix (allMatrix,k+1,j) + allMatrix[i][0]* allMatrix[k][1]*allMatrix[j][1]
        if (minCal > t):
            minCal = t
    return minCal



with open("input.txt","r") as read:
    with open("output.txt", "w") as write:        
        total = (int)(read.readline())
        for i in xrange(total):
            a = read.readline()
            a = a.replace ('\n', '').replace('\r','').split(' ')
            a = [j.split('x') for j in a]
            for x in xrange(len(a)):
                for y in xrange(len(a[x])):
                    a[x][y] = int(a[x][y])
            p = [i[0] for i in a]

            #   print matrix(a,0,len(a)-1)
            print matrix3(a)
            #write.write (matrix(a,0,len(a)-1))
    write.close()
read.close()


#http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/


'''

                print i , k , b[i,k]
                print k+1 , j , b[k+1, j]
                print allMatrix[i][0]* allMatrix[k][1]*allMatrix[j][1]


def matrixWeb( p, i , j):
    if (i == j):
        return 0
    minCal = sys.maxint
    for k in xrange(i,j):
        t = matrixWeb(p,i,k) + matrixWeb (p,k+1,j) + p[i-1]* p[k]*p[j]
        print "t is here" + t
        if (minCal > t):
            minCal = t
    print minCal
    return minCal
'''
