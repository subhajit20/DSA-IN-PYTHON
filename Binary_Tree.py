'''
Binary Tree Implement with Pre,post and inorder traversal...
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class Tree:
    def __init__(self):
        self.root = None
        
    def preOrder_Traverse(self,root):
        if root != None:
            print("Preorder Traversal ----> ",root.data)
            self.preOrder_Traverse(root.left)
            self.preOrder_Traverse(root.right)
        
    def postOrder_Traverse(self,root):
            if root != None:
                self.postOrder_Traverse(root.left)
                self.postOrder_Traverse(root.right)
                print("Post Order Traversal ----> ",root.data)

    def InOrder_Traverse(self,root):
            if root != None:
                self.InOrder_Traverse(root.left)
                print("Inorder Traversal ----> ",root.data)
                self.InOrder_Traverse(root.right)
            
    
                

newTree = Tree()
newTree.root = Node(10)
newTree.root.left = Node(76)
newTree.root.right = Node(66)
newTree.root.left.right = Node(102)
newTree.root.left.left = Node(132)

newTree.preOrder_Traverse(newTree.root) # Root -> Left -> Right
# newTree.postOrder_Traverse(newTree.root) # Left -> Right -> Root
# newTree.InOrder_Traverse(newTree.root) # Left -> Root -> Right