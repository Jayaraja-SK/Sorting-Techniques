def Shell_Sort(L): #TIME COMPLEXITY IS O(N^2)
    n=len(L)

    interval=n//2

    while(interval>0):
        for i in range(interval,n):
            temp=L[i]
            j=i
            
            while(j>=interval and L[j-interval]>temp):
                L[j]=L[j-interval]
                j=j-interval

            L[j]=temp

        interval=interval//2

    return L


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Shell_Sort(L)

print(*sorted_L)
