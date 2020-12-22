class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node

    def pop(self):
        if self.head != None:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None      
        else:
            print("Stack is empty")
            

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next



stack = Stack()
stack.push(7)
stack.push(9)
stack.push(12)
stack.push(34)
stack.push(36)
stack.push(37)
print("Stack:")
stack.print()
stack.pop()
stack.pop()
print("Stack after pop():")
stack.print()

