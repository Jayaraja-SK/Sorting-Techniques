def Max_Heapify(L,size,k):
    left=2*k+1
    right=2*k+2

    largest=k

    if(left<size and L[left]>L[largest]):
        largest=left
    if(right<size and L[right]>L[largest]):
        largest=right
    if(largest!=k):
        L[largest],L[k]=L[k],L[largest]
        Max_Heapify(L,size,largest)

    return L


def Heapify(L):
    n=(len(L)//2)-1

    for i in range(n,-1,-1):
        L=Max_Heapify(L,len(L),i)

    return L


def Heap_Sort(L):
    L=Heapify(L)

    n=len(L)

    for i in range(n-1,-1,-1):
        L[0],L[i]=L[i],L[0]
        L=Max_Heapify(L,i,0)

    return L
    


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Heap_Sort(L)

print(*sorted_L)
