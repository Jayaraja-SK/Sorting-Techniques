def Merge_Sort(L): #TIME COMPLEXITY IS O(N*Log(N))
    n=len(L)
    
    if n<2:
        return L[:] #SIMILAR TO RETURN L
    else:
        mid=n//2
        return merge(Merge_Sort(L[:mid]),Merge_Sort(L[mid:]))

def merge(L1,L2):
    i,j=0,0
    res=[]

    while(i<len(L1) and j<len(L2)):
        if L1[i]<L2[j]:
            res.append(L1[i])
            i=i+1
        else:
            res.append(L2[j])
            j=j+1

    if i<len(L1):
        res.extend(L1[i:])
    else:
        res.extend(L2[j:])

    return res


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Merge_Sort(L)

print(*sorted_L)
