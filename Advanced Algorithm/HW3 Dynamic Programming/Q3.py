"""
def fun (st1, st2):
    if (len(st1) == 1 or len(st2) == 1):
        return ''
    elif (

"""

def fun(st1, st2):
    st1 = '0' + st1
    st2 = '0' + st2
    result = {}
    for i in xrange (len(st1)):
        if (i not in result):
            result[i] = {}
        for j in xrange (len(st2)):
            if (i == 0 or j == 0):
                result[i][j] = ''
            elif (st1[i] == st2[j]):
                result[i][j] = result[i-1][j-1]+ st1[i]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])

    if (result[len(st1)-1][len(st2)-1] == ''):
        return 'No LCS'
    else:
        return result[len(st1)-1][len(st2)-1]

resultList = {{}}
def fun2(st1, st2):
    if len(st1) len(st2) in resultList:
        return result[st1][st2]
    if (len(st1) == 0 or len(st2) ==0):
        print 'a = ' + st1
        print 'b= ' + st2
        return 0
    else:
        if (st1[-1] == st2[-1]):
            result[len(str1)][len(str2)] = (fun2(st1[:-1], st2[:-2])+1)
        else:
            result[len(str1)][len(str2)] =  max (fun2(st1[:-1], st2), fun2(st1, st2[:-1]))
        resutn

def _fun2(st1, st2):
    return fun2('0'+ st1, '0'+st2)





print _fun2('abcbdab' ,'bdcaba')
print fun('abcbdab' ,'bdcaba')
            
with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        for line in read.xreadlines():
            a = str.split(line, ' ')
            write.write ( fun(a[0], a[1]) +  '\n')
        write.close()
    read.close()
