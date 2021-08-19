def Selection_Sort(L):
    n=len(L)
    
    for i in range(0,n-1):
        for j in range(i+1,n):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Selection_Sort(L)

print(*sorted_L)

       
