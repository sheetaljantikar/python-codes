class node():
 def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value


def insert(node,key):
     if node is None:
         return node(key)
     if key<node.value:
         node.left=insert(node.left,key)
     else:
        node.right=insert(node.right,key)
     return node

def minvalue(node):
    current=node

    while current.left is not None:
        current=current.left

    return current
def deletenode(root,key):
    if root is None:
        return root
    if key< root.key:
        root.left=deletenode(root.left,key)

    elif key>root.key:
        root.right=deletenode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
    temp=minvalue(root.right)
    root.key=temp.key
    root.right=deletenode(root.right,temp.key)

    return root
root=None
root=insert(root,50)
