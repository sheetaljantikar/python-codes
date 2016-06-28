class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class circular_list():
    def __init__(self):
        self.head=None

    def insert(self,key):
        new_node=Node(key)

        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            current=self.head
            while current.next is not self.head:
                current=current.next
            current.next=new_node
            new_node.next=self.head
    def printlist(self):
         if self.head is None:
             return
         else:
             current=self.head

             while (True):
                 print('%d' %current.value)
                 if current.next is self.head:
                     break
                 else:
                     current=current.next
     def split(self,head1,head2):
         if self.head is None:
             return
         else:
             current=head1
             while current.next is not head2:
                 current=current.next
             next=current.next
             current.next=self.head

             current=next
             while currrent.next is not self.head:
                 currrent=current.next

                 

            
        
a=circular_list()
a.insert(1)
a.insert(2)
a.insert(4)
a.insert(5)
a.printlist()

