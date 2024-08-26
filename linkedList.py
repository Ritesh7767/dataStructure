class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def deleteWithValue(self, data):

        if self.head is None:
            return 
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        currentNode = self.head

        while currentNode.next:

            if currentNode.next.data == data:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next

    def displayNodes(self):

        if self.head is None:
            return
        
        currentNode = self.head

        node = []
        while currentNode.next:
            node.append(currentNode.data)
            currentNode = currentNode.next

        node.append(currentNode.data)
        print("->".join(map(str, node)))


data = linkedList()

class doubleNode:

    def __init__(self, data=None):
        self.data = data
        self.previous = None
        self.next = None

class doublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        newNode = doubleNode(data)

        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode
        newNode.previous = lastNode

    def prepend(self,data):

        newNode = doubleNode(data)

        if self.head is None:
            self.head = newNode
            return
        
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode


class node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class singlyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):

        newNode = node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        self.tail.next = newNode
        self.tail = newNode

    def prepend(self, data):

        newNode = node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head = newNode



        
