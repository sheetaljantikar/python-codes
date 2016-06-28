def bubblesort(list):
    n=len(list)
    for k in range(0,n-1):
        for i in range(0,n-1):
    
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                
            
                
    return list

a=[3,6, 1, 2 ,9 ,0]
b=print(bubblesort(a))
            
        
    
    
