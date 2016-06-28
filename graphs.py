from collections import defaultdict
class Node():
    def __init__(self,id):
        self.id=id

class Graph():
    def __init__(self):
        self.dict={}
        self.n=0
        self.w=0
        self.visited=[]
        self.stack=[]
        self.queue=[]
        self.matrix=[]
        self.dict1=defaultdict(dict)
        self.rec_stack=[]

    

    
    def add_vertex(self,node):
        self.n=self.n+1
        new_vertex=Node(node)
        self.dict[new_vertex.id]=[]
        return self.dict
    def add_edge(self,node1,node2):    ##undirected graph
        self.dict[node1].append(node2)
        self.dict[node2].append(node1)
        return self.dict
    def count(self):
        count=0
        for key in self.dict.keys:
            count=count+1
        return count    

    
        
        

##    def directed_edge(self,node1,node2,w): ## directed and weighted
##            
##        self.dict1[node1][node2]=w
##        
##        return self.dict
##    def depthfirst(self,start):
##        
##        if set(self.dict.keys())==set(self.visited):
##            print(self.visited)
##            return
##        else:
##            if start not in stack:
##             self.stack.append(start)
##            if start not in self.visited:  
##             self.visited.append(start)
##          
##          pull=self.dict[start]
##          
##          for i in range(0,len(pull)):
##            if pull[i] not in self.visited:
##                nex=pull[i]
##                break
##                  
##            self.depthfirst(nex)
##          self.stack.pop()  
##          self.depthfirst(self.stack.pop())
##                
          

    def breadthfirst(self,start):
         if set(self.dict.keys())==set(self.visited):
             print(self.visited)
             return
         else:
             self.visited.append(start)
             pull=self.dict[start]
             for i in range(0,len(pull)):
                 if pull[i] not in self.visited:
                     self.queue.append(pull[i])
                     start=self.queue[0]
                     del(self.queue[0])
                     self.breadthfirst(start)
        
            
            
        
        


g=Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A','B')
g.add_edge('A','E')
g.add_edge('E','B')
g.add_edge('B','C')
g.add_edge('D','C')
#g.add_edge('D','E')

print(g.dict.keys())
print(g.dict.values())

g.breadthfirst('B')

    
 
