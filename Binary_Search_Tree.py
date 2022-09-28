class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            prev = None
            last = self.root
            
            while last != None:
                if last.data > data:
                    prev = last
                    last = last.left
                else:
                    prev = last
                    last = last.right
            
            if prev.data < data:
                prev.right = Node(data)
            else:
                prev.left = Node(data)
        
    def inorderTraversal(self):
        if self.root == None:
            return
        else:
            temp = self.root
            stack =  []
            while (temp != None or len(stack) != 0) :
                if (temp != None) :
                    stack.append(temp)
                    temp = temp.left
                else:
                    temp = stack.pop()
                    print(temp.data)
                    temp = temp.right
    
    def preorderTraversal(self):
        if self.root == None:
            return
        else:
            stack = []
            stack.append(self.root)
            
            while len(stack) > 0:
                node = stack.pop()
                print(node.data)
                
                if node.right is not None:
                    stack.append(node.right)
                elif node.left is not None:
                    stack.append(node.left)
                    
                    
bst = Binary_Search_Tree()

bst.insert(10)
bst.insert(7)
bst.insert(3)
bst.insert(12)
bst.insert(13)
bst.insert(8)

bst.preorderTraversal()