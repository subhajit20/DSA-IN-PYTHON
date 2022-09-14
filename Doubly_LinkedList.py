class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.Next = next
        self.Prev = prev


class Doubly_LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert a node at the very first  of the linkedlist ...
    def insertFront(self,mydatadata):
        new_node = Node(mydatadata)
        if self.head == None:
            new_node.Prev = None
            self.head = new_node
            return
        else:
            temp = self.head
            next_node = temp
            self.head = new_node
            new_node.Next = next_node
            new_node.Prev = None
            next_node.Prev = new_node
    
     # Insert a node at the end of the linkedlist ...
    def Insert_End(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node.Prev = None
            self.head = new_node
            return
        else:
            last = self.head
            while last.Next is not None:
                last = last.Next
            
            
            last.Next = new_node 
            new_node.Prev = last
            
     # Insert a node after a existing node ...
    def Insert_After(self,data,len,key):
        last = self.head
        new_node = Node(data)
        flag = True
        
        if self.head == None:
            new_node.Prev = None
            self.head = new_node
            return
        else:
            count = 0
            while last is not None:
                if count == len-1 and last.data == key:
                    prev = last
                    break
                else:
                    flag = False
                
                count = count +1
                last = last.Next
            
            if flag == False:
                print("No Node found...")
                return 
            
            new_node.Next = prev.Next
            prev.Next = new_node
            new_node.Prev = prev
            
            
    # Insert a node before a existing node ...
    
    def insertBefore(self,data,len,key):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.Prev = None
            return 
        else:
            temp = self.head
            count = 0
            prev_node = ''
            while temp.Next is not None:
                if count == len-1 and temp.data == key:
                    break
                elif count != len-1 and temp.data != key:
                    flag = False
                count = count + 1
                prev_node = temp
                temp = temp.Next
            
            temp.Prev = new_node
            new_node.Next = temp
            new_node.Prev = prev_node
            prev_node.Next = new_node
            
            if flag == False:
                print("Node is not found...")
    
     # Display LisnkedList ...
    def Display_Node(self):
        if self.head == None:
            print("LinkedList is empty...")
            return
        else:
            last = self.head
            count = 1
            print('<---------- Display  LinkedList ---------->')
            while last is not None:
                print(f'Node[{count}] -----> ',last.data)
            
                count = count + 1
                last = last.Next
    
    def Display_Reverse_LinkedList(self):
        if self.head == None:
            print("LinkedList is empty...")
            return
        else:
            last  = self.head
            last_node = ''
            count = 1
            while last is not None:
                if last.Next == None:
                    last_node = last
                    break
                last = last.Next
            
            print('<---------- Display Reverse  LinkedList ---------->')
            while last_node is not None:
                print(f"Node[{count}] -----> ",last_node.data)
                
                count = count + 1
                last_node = last_node.Prev
    def Display_Sperate_Node(self,len,key):
        if self.head == None:
            print('LinkedList is empty...')
            return
        else:
            temp = self.head
            count = 1
            flag = True
            while temp is not None:
                if count == len and temp.data == key:
                    print("Node is found ---> ",temp.data)
                    break
                else:
                    flag = False

                count = count + 1
                temp = temp.Next

            if flag == False:
                print("Node is not found")
                return

    def Delete_EndNode(self):
        if self.head == None:
            print('LinkedList is empty...')
            return
        elif self.head is not None:
            last = self.head
            prev_node = ''
            if last.Next == None:
                self.head = None
                return
            else:
                while last.Next is not None:
                    if last.Next == None:
                        break
                    prev_node = last
                    last = last.Next
            last.Next = prev_node
            prev_node.Prev = last
            prev_node.Next = None
    
    def Delete_Head(self):
        if self.head == None:
            print('LinkedList is empty...')
            return
        else:
            last = self.head
            count = 0
            head_node = ''
            if last.Next == None:
                self.head = None
            else:
                while last is not None:
                    if count == 1:
                        head_node = last
                        print(head_node.data)
                        break
                    count = count + 1
                    last = last.Next
                
                self.head = head_node
                head_node.Prev = None

            
double_linkedList = Doubly_LinkedList()

double_linkedList.Insert_End(12) 
double_linkedList.Insert_End(17) 
double_linkedList.Insert_End(14) 

# double_linkedList.Display_Reverse_LinkedList()

# double_linkedList.Delete_EndNode()
# double_linkedList.Delete_EndNode()
# double_linkedList.Delete_EndNode()
double_linkedList.Delete_Head()
double_linkedList.Delete_Head()
double_linkedList.Delete_Head()
double_linkedList.Display_Node()