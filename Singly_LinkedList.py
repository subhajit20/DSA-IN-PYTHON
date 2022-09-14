from operator import le


class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Length_of_LinkedList(self):
        if self.head == None:
            return 0
        else:
            count = 0
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next
            return count
    
    def Insert_Begin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
    
    def Insert_End(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            print("Node is inserted Successfully...")
    
    def Insert_Between(self,data,range):
        count = 0
        new_node = Node(data)
        myrange = range-1
        flag = True
        if self.head == None:
            print("LinkedList is empty...")
        else:
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next
                if count == myrange:
                    new_node.next = temp.next
                    temp.next = new_node
                    print("Node is inserted Succesfully ------>",new_node.data) 
                    return
                elif count != myrange:
                    flag = False
            if flag == False:
                print("Node is Not founded...")

    def Display_HeadNode(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        print('\n\n')
        print("HEAD NODE --------> ",temp.data)

    def Display_LinkedList(self):
        if self.head == None:
            print("LinkedList is empty...") 
        else:
            temp = self.head
            print("\n\n")
            print("******* LinkedList Nodes ******")
            while temp is not None:
                print("Node -----> \t",temp.data)
                temp = temp.next

    def Delete_EndNode(self,length):
        linkedlist_length = length-2
        count = 0
        if self.head == None:
            print("LinkedList is empty...")
            return
        else:
            temp = self.head
            flag = True
            while temp != None:
                count = count + 1
                temp = temp.next
                if count == linkedlist_length:
                    print("Deleted --------->",temp.next.data)
                    temp.next = None
                    return
                else:
                    print("Lngth -- ",linkedlist_length)
                    print("Count --- > ",count)
                    self.head.next = None
                    flag = False
            if flag == False:
                print("Node is not founded :)")
    
    def Delete_Node(self,key,len):
        if self.head == None:
            print("LinkedList is empty")
            return
        else:
            temp = self.head
            count = 0
            
            while temp is not None:
                count = count + 1
                if temp.data == key and count == len:
                    break
                prev = temp
                temp = temp.next
            
            print(count)
            if(temp == None):
                return
 
            # # Unlink the node from linked list
            prev.next = temp.next
            temp = None
                

    def Search_Node(self,range,data):
        if self.head == None:
            print("LinkedList is empty...")
            return 
        else:
            count = 0
            myrange = range - 1
            temp = self.head
            flag = True
            while temp != None:
                count = count + 1
                temp = temp.next
                print('\n\n')
                if count == myrange and temp.data == data:
                    print("Node is found -------> ",temp.data)
                    return
                else:
                    flag = False
            if flag == False:
                print("Oh!! Node is Not Found :)")

linkedlist = LinkedList()

flag = True
while flag:
    print('\n\n')
    print("************* LinkedList Program **********\n")
    print("Enter 1: Insert End")
    print("Enter 2: Delete End")
    print("Enter 3: Display LinkedList")
    print("Enter 4: Display Head")
    print("Enter 5: Insert Between")
    print("Enter 6: Insert Begin")
    print("Enter 7: Search Node")
    print("Enter 8: Delete Any Node")
    print("Enter 0: Exit...")
    choise = int(input("Enter Your Choise :: "))
    if choise == 1:
        data = int(input("Enter Data :: "))
        linkedlist.Insert_End(data)
    elif choise == 2:
        len = linkedlist.Length_of_LinkedList()
        if len != 0:
            linkedlist.Delete_EndNode(len)
        else:
            print("LinkedList is empty...")
    elif choise == 3:
        linkedlist.Display_LinkedList()
    elif choise == 4:
        linkedlist.Display_HeadNode()
    elif choise == 5:
            data = int(input("Enter Data :: "))
            len = int(input("Enter Position :: "))
            linkedlist.Insert_Between(data,len)
    elif choise == 6:
        data = int(input("Enter Data :: "))
        linkedlist.Insert_Begin(data)
    elif choise == 7:
            len = int(input("Enter Position :: "))
            data = int(input("Enter Data :: "))
            linkedlist.Search_Node(len,data)
    elif choise == 8:
            data = int(input("Enter Data :: "))
            len = int(input("Enter Position :: "))
            linkedlist.Delete_Node(data,len)
    elif choise == 0:
        flag = False
        break
    
    
    