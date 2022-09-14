# Implement Stack using List data type in Python
'''
    isEmpty()
    push()
    pop()
    peek()
    display()
'''
stack = []
top = None

def isEmpty(stk):
    if stk == []:
        return True
    elif len(stk) > 0:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk) - 1
    
def pop(stk):
    if isEmpty(stk):
        return "Stack is underflow"
    else:
        element = stk.pop()
        if len(stk) == 0:
            top = None
        else :
            top = len(stk) - 1
        
        return element," is Deleted!!"

def peek(stk):
    if isEmpty(stk):
        return "Stack is underflow"
    else:
        top = len(stk) - 1
        return stk[top]

def display(stk):
    if isEmpty(stk):
        return "Stack is empty"
    else:
        top = len(stk) - 1
        print(stk[top],'<------ Top')
        for i in range(top-1,-1,-1):
            print(stk[i])


flag = True

while flag:
    print("*********** STACK USING LIST ***********")
    print("Enter 1 :: Push")
    print("Enter 2 :: Pop")
    print("Enter 3 :: See the head element of the Stack")
    print("Enter 4 :: Display the stack")
    print("Enter 0 :: Quit")
    
    user_input = int(input("Enter Your Option :: "))
    if user_input == 1:
        item = int(input("Enter a item to be pushed into Stack ::"))
        push(stack,item)
        print(item,"Inserted Successfull :)")
        continue
    elif user_input == 2:
        element = pop(stack)
        print(element)
        continue
    elif user_input == 3:
        head = peek(stack)
        print(head)
        continue
    elif user_input == 4:
        result = display(stack)
        print(result)
        continue
    elif user_input == 0:
        flag = False
        break