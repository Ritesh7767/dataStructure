class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newnode = Node(data)

        if not self.head:
            self.head = self.tail = newnode
            return 
        
        self.tail.next = newnode
        self.tail = newnode

    def display(self):

        if not self.head:
            return 
        result = []
        
        temp = self.head

        while temp:
            result.append(temp.data)
            result = result.next

        print("->".join(map(str, result)))