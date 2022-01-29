def Quick_Sort(L,left,right): #TIME COMPLEXITY IS O(N**2) IN  WORST CASE AND O(N*log(N)) IN AVG. CASE
    if((right-left)<=1):
        return

    pivot=L[left]
    lower=left+1
    upper=left+1

    for i in range(left+1,right):
        if(L[i]>pivot):
            upper=upper+1
        else:
            L[i],L[lower]=L[lower],L[i]
            lower=lower+1
            upper=upper+1

    L[left],L[lower-1]=L[lower-1],L[left]
    lower=lower-1

    Quick_Sort(L,left,lower) #SORTING ELEMENTS THAT ARE SMALLER THAN THE PIVOT
    Quick_Sort(L,lower+1,upper) #SORTING ELEMENTS THAT ARE LARGER THAN THE PIVOT

    return L


L=list(map(int,input().split())) # INPUT LIST AS - 3 2 1 4 5

sorted_L=Quick_Sort(L,0,len(L)) #SEGREGATING SMALLER AND LARGER ELEMENTS SEPARATELY W.R.T. PIVOT

print(*sorted_L)

    
