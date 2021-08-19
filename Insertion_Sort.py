def Insertion_Sort(L): #TIME COMPLEXITY IS O(N^2)
    if(len(L)==0):
        return []
    else:
        head=L[0]
        tail=L[1:]
        return insert(head,Insertion_Sort(tail))

def insert(head,seq):
    if(len(seq)==0):
        return [head]
    elif(head<=seq[0]):
        return [head]+seq
    else:
        result=seq[:1]
        result.extend(insert(head,seq[1:]))
        return result


L=list(map(int,input().split())) #INPUT LIST AS - 3 2 1 4 5

sorted_L=Insertion_Sort(L)

print(*sorted_L)
