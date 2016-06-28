class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head=None

class Hashtable():
    def __init__(self,size):
     self.size=size
     self.table=[0]*size

    def create_ll(self):
        self.ll=[0]*self.size
        for i in range(0,self.size):
            self.ll[i]=Linkedlist()
            self.ll[i].head=None
            
            

    def hashfunction(self,key):
        return key%self.size
    def insert(self,key):
        a=self.hashfunction(key)
        n=Node(key)
        if self.ll[a].head==None:
            self.ll[a].head=n
        else:
            current=self.ll[a].head
            while current.next!=None:
                current=current.next
            current.next=n

h=Hashtable(7)
h.create_ll()
h.insert(21)
h.insert(14)
a=h.ll[0].head.value
b=h.ll[0].head.next.value
c=h.ll[1].head.value



