class BTnode():
    def __init__(self , data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
    
class BTree():
    def __init__(self , root):
        self.root = None

    def inorder(self , root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self,root) :
        if root is None:
            return
        else:
            print(root.data)   
            self.preorder(root.left)   
            self.preorder(root.right) 
    
    def postorder(self , root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

class NodeBST:
    def __init__(self , data):
        self.key = data
        self.left = None
        self.right = None

def searchBST(self , k):
        if self is None:
            return print('not found')
        
        if k is self.key:
            return print("True")
        
        if k < self.key:
            return searchBST(self.left,k)
        
        return searchBST(self.right,k)
    
r = NodeBST(5)
r.left = NodeBST(3)
r.left.left = NodeBST(2)
r.left.right = NodeBST(4)
r.right = NodeBST(8)
searchBST(r , 18)



# ex = BTnode(5 , BTnode(7 , BTnode(1) , BTnode(9)) , BTnode(4))

# root2 = BTnode(1 , BTnode(27 , BTnode(32)) , BTnode(56))
# ex2 = BTree(root2)
# ex2.inorder(root2)
