
'''
 Queue Operations ------->
 Rear, Front
 1. enqueue() --> Insert element at rear
 2. dqueue()  --> Delete element at front
 3. isEmpty()
'''
class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0
    
    def Display_Front(self):
        if self.front == self.rear:
            print("Queue is empty...")
        else:
            print("FRONT Element ----> ",self.front)
            print('\n\n')


    def enqueue(self,data):
        if self.rear == self.front:
            self.queue.append(data)
            self.rear = self.rear + 1
            self.front = self.queue[0]
        else:
            self.queue.append(data)
            self.rear = len(self.queue)
            self.front = self.queue[0]

    def display_Queue(self):
        if self.rear == self.front:
            print("Queue is empty...")
            return
        else:
            print("Display Queue ------> ")
            i = 0
            while i <= len(self.queue)-1:
                print(self.queue[i])
                i = i + 1
            print("\n\n")

    def dequeue(self):
        if self.rear == self.front:
            print("Queue is empty")
            return
        else:
            i = 0
            current = 0
            if len(self.queue)-1 == current:
                del self.queue[current]
                self.front = 0
                self.rear = 0
                return 
            while i < len(self.queue):
                current = current + 1
                self.queue[i] = self.queue[current]
                if current == len(self.queue)-1:
                    del self.queue[current]
                    break
                i = i+1
            self.rear = len(self.queue)
            self.front = self.queue[0]

newQueue = Queue()

newQueue.enqueue(10)
newQueue.enqueue(15)
newQueue.enqueue(13)
newQueue.enqueue(16)

newQueue.display_Queue()
newQueue.dequeue()
newQueue.display_Queue()
newQueue.Display_Front()
print(newQueue.rear)
newQueue.display_Queue()
