def createstack():
     stack=[]
     return stack
    
        
def push(stack,data):
    stack.append(data)

def pop(stack):
    return stack.pop()

def printstack(stack):
    for i in stack:
        print (i)
def peep(stack):
    print(stack[len(stack)-1])

a=createstack()
b='sheetal'
n=len(b)
for i in range(0,n,1):
    push(a,b[i])

string=""
for i in range(0,n,1):
    string+=pop(a)

print(string)
##push(a,1)
##push(a,2)
##push(a,3)
##push(a,4)
##printstack(a)
##pop(a)
##printstack(a)
##peep(a)


##class node():
##    def __init__(self,data):
##        self.data=data
##        self.next=None
##
##class linkedlist():
##    def __init__(self):
##        self.head=None
##
##    def push(self,data):
##        new=node(data)
##        if self.head is None:
##            self.head=new
##        else:
##            temp=self.head
##            self.head=new
##            new.next=temp
##
##    def pop(self):
##        temp=self.head
##        while (temp.next):
##            current=temp.next
##            temp=current.next
##        current.next=None
##    
##        
##
##    def printlist(self):
##        temp=self.head
##        while(temp):
##            print(temp.data)
##            temp=temp.next
##a=linkedlist()
##a.push(1)
##a.push(2)
##a.push(3)
##a.pop()
##a.printlist()
b='sheetal'
n=len(b)

        
            

