# Implementation of priority queue with array

class Item:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
    
class Priority_Queue:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def enqueue(self,data,priority):
        if len(self.arr) == 0:
            new_priority_queue = Item(data,priority)
            self.size = self.size + 1
            self.arr.append(new_priority_queue)
        elif len(self.arr) > 0:
            new_priority_queue = Item(data,priority)
            self.arr.append(new_priority_queue)
            for i in range(0,len(self.arr)):
                self.size = self.size + i

    def Print_Queue(self):
        if len(self.arr) == 0:
            print("Queue is empty...")
            return 
        else:
            for i in range(0,len(self.arr)):
                print("Item-->",self.arr[i].data)

    def Peek(self):
        i = 0
        if len(self.arr) <= 0:
            print("Queue is empty...")
            return
        else:
            queue = self.arr
            highest_ind = queue[0].priority
            ind = 0
            for i in range(0,len(self.arr)):
                next = i + 1
                if next <= len(self.arr)-1:
                    if highest_ind < self.arr[next].priority:
                        highest_ind = self.arr[next].priority
                        ind = next
            return ind

    def dequeu(self):
        if len(self.arr) <= 0:
            print("Queue is empty...")
            return
        else:
            ind = self.Peek()
            queue = self.arr
            if len(self.arr)-1 == ind:
                del self.arr[ind]
                for i in range(0,len(self.arr)):
                    self.size = self.size + i
            else:
                for i in range(ind,len(self.arr)):
                    next = i + 1
                    if next <= len(self.arr)-1:
                        self.arr[i] = self.arr[next]
                        del queue[next]
                for n in range(0,len(self.arr)):
                    self.size = self.size + n
new_queue = Priority_Queue()

new_queue.enqueue(10,70)
new_queue.enqueue(50,30)
new_queue.enqueue(20,40)
new_queue.Print_Queue()

print(new_queue.size)