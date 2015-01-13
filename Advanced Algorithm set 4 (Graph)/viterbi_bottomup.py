import sys
def toGraph ( n , b ):
    result = {}
    for i in xrange(1,n+1):
        result[i] = []
    for i in b:
        #from
        result [int(i[i.find('(')+1:i.find(',')])].append(int (i[i.find(',')+2:]))
    return result

#It is a cyclic when it hit a path you already went
def viterbi (n, path, result, corNode, finalNode):
    for i in n[corNode]:
        if i in path:
            return -1
    if corNode == finalNode:
        return 1
    b = 0
    for i in n[corNode]:
        a = viterbi (n, path+[corNode], result, i, finalNode)
        if a == -1:
            return -1
        else:
            b +=a
    return b


def isCycle (n, path, corNode):
    print path
    print corNode
    for i in n[corNode]:
        if i in path:
            return True
    for i in n[corNode]:
        a = isCycle (n, path+[corNode], i)
        if a is True:
            return True
    return False

def viterbi1 (n, path,finalNode):
    result = 0
    for i in path:
        for j in n[i]:
            path.append(j)
            if (j == finalNode):
                result +=1
    return result


with open("output1.txt", "w") as write:
    total = (int)(sys.stdin.readline())
    for i in xrange(total):
        n = [ int(i) for i in sys.stdin.readline().split()]
        b = sys.stdin.readline().replace ('\r\n', '').split(')')[:-1]
        g = toGraph(n[0],b)
        result = viterbi (g, [], 0, 1 , n[0])
        if (result == -1):
            write.write('CYCLIC\n')
            print 'CYCLIC'
        else:
            write.write(str(result))
            write.write('\n')
            print (str(result))
write.close()

'''
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:        
        total = (int)(read.readline())

        for i in xrange(total):
            n = [int(j) for j in read.readline().replace ('\r\n' , '').split()]
            b = read.readline().replace ('\r\n', '').split(')')[:-1]
            g = toGraph(n[0],b)
            result = viterbi (g, [], 0, 1 , n[0])
            if (result == -1):
                write.write('CYCLIC\n')
            else:
                write.write(str(result))
                write.write('\n')
            print isCycle(g, [], 0, 1 , n[0])
            #print viterbi1 (g, [1], n[0])
            #Record number of out degree

    write.close()
read.close()
'''
