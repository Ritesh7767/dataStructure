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

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return 
        
        self.tail.next = newnode
        self.tail = newnode

    def prepend(self, data):

        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode

        newnode.next = self.head
        self.head = newnode

    def deleteByValue(self, value):

        if self.head is None:
            return
        
        currentNode = self.head.next
        prevNode = self.head
        
        while currentNode.next:

            if currentNode.data == value:
                prevNode.next = currentNode.next
                currentNode.next = None
                currentNode = prevNode.next
                continue

            prevNode = currentNode
            currentNode = currentNode.next

        if self.head.data == value: self.head = self.head.next
        if self.tail.data == value:
            prevNode.next = None
            self.tail = prevNode


    def displayData(self):

        if self.head is None:
            return 
        
        result = []
        currentNode = self.head

        while currentNode:
            result.append(currentNode.data)
            currentNode = currentNode.next

        print("->".join(map(str, result)))

    def reverse(self):

        prev = None

        while self.head.next:
            nextnode = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nextnode
        self.head.next = prev

    # def reverserecur(self, temp=None, )        

def reverseRecur(head, prev, next):

    if next is None:
        head.next = prev
        prev = head
        head = next
        head.next = prev
        return 
    
    head.next = prev
    return reverseRecur(head.next)

data = LinkedList()
data.append(1)
data.append(2)
# data.displayData()
data.reverse()
# data.displayData()
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return 
        
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def displayData(self):

        if self.head is None:
            return 
        
        currentNode = self.head
        result = []
        while currentNode:

            result.append(currentNode.data)
            currentNode = currentNode.next

        print("->".join(map(str, result)))

    def deleteValue(self, value):

        if self.head is None:
            return 
        
        currentNode = self.head.next

        while currentNode.next:

            if currentNode.data == value:
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                currentNode = currentNode.next
                continue
            currentNode = currentNode.next

        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
        
        if self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None

    def reverse(self):

        temp = self.head

        while temp.next:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev

        temp.prev, temp.next = temp.next, temp.prev
        self.head = temp

    def middle(self):

        left = self.head
        right = self.head

        while right.next:
            left = left.next
            
            if right.next.next:
                right = right.next.next
            else:
                right = right.next

        return left.data
    
    def palindrome(self):

        if self.head is None:
            return 
        string = ""

        currentNode = self.head
        while currentNode:
            string += currentNode.data
            currentNode = currentNode.next

        return string == string[::-1]


data = DoublyLL()
data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
data.append(6)
data.append(7)
# data.displayData()
# data.reverse()
# data.displayData()

data.deleteValue(1)
data.deleteValue(2)
data.deleteValue(3)
# data.displayData()


def addTowLL(head1, head2):

    carry = 0
    result = DoublyLL()

    while head1 is not None or head2 is not None:

        num1 = 0
        num2 = 0
        
        if head1 is not None:
            num1 = head1.data
            head1 = head1.next

        if head2 is not None:
            num2 = head2.data
            head2 = head2.next

        sum = num1 + num2 + carry
        data = sum % 10
        carry = sum // 10 
        result.append(data)

    result.displayData()

    return result

# data.displayData()

data2 = DoublyLL()
data2.append(9)
data2.append(8)
data2.append(7)
data2.append(6)
data2.append(5)
data2.append(4)
# data2.displayData()
result = addTowLL(data.head, data2.head)

# print(data)

# print(result)