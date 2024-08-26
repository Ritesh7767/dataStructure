class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class doublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        newnode = Node(data)
        self.size += 1

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def prepend(self, data):
        newnode = Node(data)
        self.size += 1

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insertByPosition(self, data, position):

        if position > self.size:
            print("Position is greater than size of the linked list, please provide valid position")
            return

        if position == 1:
            return self.prepend(data)
        
        currentNode = self.head
        while position-1:
            currentNode = currentNode.next
            position -= 1

        newnode = Node(data)
        newnode.prev = currentNode.prev
        newnode.next = currentNode

        currentNode.prev.next = newnode
        currentNode.prev = newnode
        self.size += 1

    def deleteByData(self, data):

        if self.head is None:
            return
        
        if self.head.data == data:
            if self.head.next is None:
                self.head, self.tail = None, None
                return 
            temp = self.head.next
            self.head.next = None
            self.head = temp

        currentNode = self.head

        while currentNode.next:

            if currentNode.data == data:
                if currentNode == self.head:
                    self.head = self.head.next
                if currentNode.next:
                    currentNode.next.prev = currentNode.prev
                temp = currentNode.next
                currentNode.next, currentNode.prev = None, None
                currentNode = temp
                self.size -= 1
                continue
            
            currentNode = currentNode.next

        if currentNode.data == data:
            if self.head == self.tail:
                self.head, self.tail = None, None
                return
            self.tail = self.tail.prev
            self.tail.next = None
            currentNode.prev, currentNode.next = None, None    
            self.size -= 1

    def deleteByPosition(self, position):

        if self.head is None or position > self.size:
            return -1
        
        self.size -= 1
        if position == 1:
            temp = self.head.next
            self.head.next.prev = None
            self.head.next, self.head.prev = None, None
            self.head = temp
            return
        
        if position == self.size:
            temp = self.tail.prev
            self.tail.prev = None
            self.tail = temp
            return 
        
        currentNode = self.head

        while position-1:
            currentNode = currentNode.next
            position -= 1 
        
        currentNode.next.prev = currentNode.prev
        currentNode.prev.next = currentNode.next
        currentNode.next, currentNode.prev = None, None

    def display(self):

        if self.head is None:
            return
        
        currentNode = self.head
        
        nodes = []
        while currentNode.next:
            nodes.append(currentNode.data)
            currentNode = currentNode.next

        nodes.append(currentNode.data)
        print("->".join(map(str, nodes)))

    def rotateData(self):

        if self.head is None:
            return 
        
        while self.head.next:
            self.head.next, self.head.prev = self.head.prev, self.head.next
            self.head = self.head.prev

        self.head.next, self.head.prev = self.head.prev, self.head.next


data = doublyLinkedList()

print(data.head)

data.append(1)
data.append(2)
data.append(3)
# print(data.head)

data.prepend(0)
data.display()
# print(data.size)

data.insertByPosition(9, 3)
# print(data.size)

data.deleteByData(3)
data.deleteByData(2)
data.deleteByData(9)
# data.deleteByData(2)

data.display()



        