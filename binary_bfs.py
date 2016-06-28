class Node():
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
##def bfs(start):
##    if set(nodes)==set(visited):
##        return (visited)
##    else:
##        
##        visited.append(start.val)
##        l=start.left
##        r=start.right
##        if l is not None:
##            queue.append(l.val)
##        if r is not None:
##            queue.append(r.val)
##        start=queue[0]
##        del(queue[0])
##        bfs(start)
def insert(root,key):
    if root is None:
        root=Node(key)
        return root
    else:
        if key<root.val:
            root.left=insert(root.left,key)
        elif key > root.val:
            root.right=insert(root.right,key)
        return root

root=Node(12)
insert(root,5)


          
        
