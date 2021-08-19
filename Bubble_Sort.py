def Bubble_Sort(L): #TIME COMPLEXITY IS O(N^2)
    n=len(L)
    
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Bubble_Sort(L)

print(*sorted_L)


