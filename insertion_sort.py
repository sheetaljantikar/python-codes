def insertion(list,n):
    for i in range(1,n-1):
        value=list[i]
        hole=i
        while hole>1 and list[hole-1]>value:
            list[hole]=list[hole-1]
            hole=hole-1
        list[hole]=value
    return list


a=[5,2,8,1,3]
n=len(a)
b=insertion(a,n)
