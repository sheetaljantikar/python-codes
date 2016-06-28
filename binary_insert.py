class Node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
        

    def insert(self,node,key):
        
        if node is None:
            node=Node(key)
            return
        else:
            if key>node.value:
                if node.right is None:
                    node.right=Node(key)
                    return
                else:
        
                    self.insert(node.right,key)


            else:
                if node.left is None:
                   node.left=Node(key)
                   return
                else:
                    
                    self.insert(node.left,key)

    def search(self,root,key):
        if root.value==key:
            print('found')
            return
        elif key>root.value:
            self.search(root.right,key)
        elif key<root.left.value:
            self.search(root.left,key)
        else:
            print('element not present')
            return

    def delete(self,root,key):
        if root is None:
            return
        elif key>root.value:
            root.right=self.delete(root.right,key)
        elif key<root.value:
            
                root.left=self.delete(root.left,key)
        else:
            if root.left is None:
                temp=root.right
                
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                
                root=None

            temp=self.min_node(root.right)
            root.value=temp.value
            root.right=self.delete(root.right,temp.value)
    def min_node(self,node):
        if node is None:
            return node
        else:
            current=node
            while(current.left is not None):
                current=current.left
            return current
        
root=Node(20)
#a.root=root
root.insert(root,10)
root.insert(root,5)
root.insert(root,15)
root.insert(root,12)
root.insert(root,4)
root.search(root,10)
a=(root.left).right.value
root.delete(root,12)

            
