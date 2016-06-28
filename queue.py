class queue():
    def __init__(self):
        self=[]
    def append(self,data):
        return self.append(data)
    

    def enqueue(self,data):
       self.append(data)
       #self[len]=data
        

    def dequeue(self):
        del self[0]


a=queue()
a.enqueue(1)
a.dequeue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.dequeue()
