class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enque(self,data):
        new_node = Node(data)

        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            temp = self.rear
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            self.rear = temp.next

    def deque(self):

        if self.front == None:
            print("Queue is empty")
        else:
            self.front = self.front.next
    
    def display(self):
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.next

    
queue = Queue()
queue.enque(44)
queue.enque(55)
queue.enque(66)
queue.enque(77)
queue.enque(88)
print("Queue after Enque:")
queue.display()
queue.deque()
queue.deque()
print("Queue after Deque")
queue.display()


