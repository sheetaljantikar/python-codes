class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublelink():
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=None   
            new_node.prev=None
        else:
            new_node.next=self.head
            new_node.prev=None
            self.head=new_node
    def insert(self,prev_node,data):
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
    def print(self):
        temp=self.head
        while (temp):
            print('%d' %temp.data)
            temp=temp.next

    def delete(self,k): ##k is the index of the node
        if k<0:
            return
##        if k==0:
##            temp=self.head.next
##            self.head.next=None
##            temp.prev=None
##            self.head=temp
##        else:
        i=1
        current=self.head
        while(i<k):
            current=current.next
            i+=1
        p_node=current.prev
        n_node=current.next
        if current==self.head:
            self.head=current.next
        if p_node is not None:
            p_node.next=n_node
        if n_node is not None:
            n_node.prev=p_node
            
    def reverse(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        while(temp):
            print(temp.data)
            temp=temp.prev
            

a=doublelink()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
#a.reverse()
a.print()
b=a.push(7)
a.insert(b,8)

                
            
            
    
