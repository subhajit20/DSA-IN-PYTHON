'''
 Stack Using Singly LinkedList ------
 
 **** Operations ****
 1. push()
 2. pop()
 3. peek()
 4. display() 
'''


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack_LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node
    def pop(self):
        if self.head == None:
            print("Stack is underflow...")
            return
        else:
            temp = self.head
            if temp.next == None:
                self.head = None
            else:
                last_node = ''
                while temp is not None:
                    if temp.next == None:
                        break
                    last_node = temp
                    temp = temp.next
                last_node.next = None
                
    def display(self):
        if self.head == None:
            print("Stack is underflow...")
            return
        else:
            temp = self.head
            while temp is not None:
                print("Stack Element",temp.data)
                temp = temp.next
            
    def peek(self):
        if self.head == None:
            print("Stack is underflow")
            return 
        else:
            print("\n")
            print("HEAD --------> ",self.head.data)
stack = Stack_LinkedList()

stack.push(12)
stack.push(32)
stack.push(92)
stack.push(192)
stack.display()

stack.peek()