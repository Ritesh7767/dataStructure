class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return 
        
        lastnode = self.head

        while lastnode.next:
            lastnode = lastnode.next

        lastnode.next = newnode


def displayLinkedList(head):

    if head.next is None:
        return print(head.data)

    print(head.data)
    return displayLinkedList(head.next)

def reverseLinkedList(head):

    if head is None or head.next is None:
        return 

    prevnode = None
    nextnode = head.next

    while head.next:

        head.next = prevnode
        prevnode = head
        head = nextnode

        if nextnode.next:
            nextnode = nextnode.next

    head.next = prevnode
    return head

def insertElement(head, position, newnode):

    for i in range(position-2):
        head = head.next

    newnode.next = head.next
    head.next = newnode

data = linkedList()

def deleteByPosition(head, position = 0):
    
    temp = None

    for _ in range(position-1):
        temp = head
        head = head.next

    temp.next = head.next
    head.next = None

data = linkedList()

data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)

deleteByPosition(data.head, 1)
displayLinkedList(data.head)
