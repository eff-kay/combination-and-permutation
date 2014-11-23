def permutation(s):
    if len(s) == 1:
     return [s]
    perm_list = [] # resulting list
    for a in s:
        remaining_elements = [x for x in s if x != a]
        print "remaining elements", remaining_elements
        z = permutation(remaining_elements) # permutations of sublist
        print "z",z
        for t in z:
            perm_list.append([a] + t)
            print "t",t,"  permlist",perm_list

    print"permalink", perm_list
    return perm_list

print len(permutation("abc"))


def xuniqueCombinations(items, n):
    if n==0:
        print "n==0"
        yield []
    else:
        for i in xrange(len(items)):
            print "i",i,"items[i+1:]",items[i+1:]," n-1",n-1
            print "items",items,'n',n
            for cc in xuniqueCombinations(items[i+1:],n-1):
                print "cc",cc,"[items[i]]",[items[i]]
                yield [items[i]]+cc

for x in xuniqueCombinations([1,2,3,4],2):
    print x
