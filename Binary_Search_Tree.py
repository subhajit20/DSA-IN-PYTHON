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
        
    def inorderTraversal(self,root):
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
                
bst = Binary_Search_Tree()

bst.insert(10)
bst.insert(50)
bst.insert(70)
bst.insert(20)
bst.insert(30)
bst.insert(2)
bst.insert(6)
bst.insert(1)

bst.inorderTraversal(bst.root)