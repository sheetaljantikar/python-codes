def partition(list,start,end):
 pivot=list[end]
 pindex=start
 for i in range(start,end):
     if list[i]<=pivot:
         list[i],list[pindex]=list[pindex],list[i]
         pindex=pindex+1
 list[pindex],list[end]=list[end],list[pindex]
 return(pindex)
     
   



def quicksort(list):
    quicksort2(list,0,len(list)-1)


def quicksort2(list,low,high):
    if low <high:
  
       
        pindex=partition(list,low,high)
        quicksort2(list,low,pindex-1)
        quicksort2(list,pindex+1,high)
  
  

a=[1,3,8,7,2,5]
b=quicksort(a)
