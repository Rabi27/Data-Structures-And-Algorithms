class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    #Append method add elements to the end of the list
    def append(self,value):
        new_Node = Node(value)

        if  self.head == None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_Node
    
    #insert method adds element at the specified index. 
    #If the index is 0,then element is added at the start and is made the head
    #If the index is greater than equal to the size of the list then element is added at the last
    def insert(self,index,value):
        new_Node = Node(value)
        temp = self.head

        if index == 0:
            new_Node.next = self.head
            self.head = new_Node

        elif index >= self.size_of_list():
            self.append(value)
        else:
            for i in range(index-1):
                temp = temp.next
            
            new_Node.next = temp.next
            temp.next = new_Node

    #push method inserts element at the start of the list
    def append_at_start(self,value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node

    #removes element at the specified index
    def pop(self,index):
        temp = self.head
        if index == 0:
            self.head = self.head.next
        elif index >= self.size_of_list():
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        else:
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next


    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

    def display_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def size_of_list(self):
        temp = self.head
        size = 0
        while temp != None:
            size = size + 1
            temp = temp.next
        return size
    


l1 = LinkedList()
l1.append(23)
l1.append(32)
l1.append(44)
l1.append(55)
l1.insert(0,333)
l1.insert(1,133)
l1.insert(3,533)
l1.append_at_start(1222)
l1.append_at_start(90)
print("List:")
l1.display_list()
print("List after Pop:")
l1.pop(1)
l1.pop(2)
l1.pop(9)
l1.pop(10)
l1.display_list()
print("List after Reversing:")
l1.reverse()
l1.display_list()
print("Size of List:",l1.size_of_list())





