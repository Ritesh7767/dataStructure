class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        
        newnode.prev = self.tail
        self.tail.next = newnode
        self.tail = newnode

    def prepend(self, data):

        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def pop(self):

        if self.head == None:
            return
        
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None

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

data = DoublyLinkedList()

class node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):

        newnode = node(data)
        self.size += 1
        if self.head is None:
            self.head = newnode
            return

        lastnode = self.head

        while lastnode.next:
            lastnode = lastnode.next
        
        lastnode.next = newnode

    def prepend(self, data):

        newnode = node(data)
        self.size += 1

        if self.head is None:
            self.head = newnode

        newnode.next = self.head
        self.head = newnode

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

    # def displayRecurssive(self, currentNode):
    #     if currentNode.next is None:
    #         return print(currentNode.data)
    #     print(currentNode.data)
    #     return displayRecurssive()

    def reverse(self):

        if self.head is None:
            return

        if self.head.next is None:
            return

        prevNode = None
        nextNode = self.head.next

        while self.head.next:

            self.head.next = prevNode
            prevNode = self.head
            self.head = nextNode

            if nextNode.next:
                nextNode = nextNode.next

        self.head.next = prevNode

    def length(self):
        return self.size
    
    def size(self):

        if self.head is None:
            return 0
        
        if self.head.next is None:
            return 1
        
        currentNode = self.head
        size = 0

        while currentNode.next:
            size += 1
            currentNode = currentNode.next
        return size + 1

data = linkedList()

data.append(1)
data.append(2)
data.append(3)
data.append(5)
data.append(6)
data.append(7)
data.append(8)
data.append(9)
data.append(10)
data.append(11)

# data.display()

data.reverse()
# data.display()

data.prepend(0)
# data.display()
data.reverse()
# data.display()

# print(data.size)
# print(data.length())
# print(data.head)

# def displayRecurssive(head):

#     if head.next is None:
#         print(head.data)
#         return
    
#     print(head.data)
#     return displayRecurssive(head.next)

# displayRecurssive(data.head)