def merge(left,right,list):
    nl=len(left)
    nR=len(right)
    i=0
    j=0
    k=0

    while(i<nl and j<nR):
        if (left[i]<right[j]):
            list[k]=left[i]
            k=k+1
            i=i+1
        else:
            list[k]=right[j]
            k=k+1
            j=j+1
    while (i<nl):
        list[k]=left[i]
        i=i+1
        k=k+1
    while(j<nR):
     list[k]=right[j]
     j=j+1
     k=k+1

    return list
      
        
def mergesort(list):
    if len(list)<2:
        return
    else:
        mid=len(list)//2
        left=list[0:mid]
        right=list[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,list)
    return list

a=[3,7,4,1,8,2]
b=mergesort(a)
    
     
