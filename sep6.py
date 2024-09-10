class Node:

    def __init__(self, data=None):
        self.value = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return 
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newnode

    def deleteNthNode(self, n):

        if self.head is None:
            return 
        
        size = 1
        temp = self.head

        while temp.next:
            temp = temp.next
            size += 1
        print(size)
        count = size - n

        if not count:
            self.head = self.head.next
            return 

        temp = self.head
        prevnode = None
        while count:
            prevnode = temp
            temp = temp.next
            count -= 1

        prevnode.next = temp.next
        temp.next = None

    def deleteByValue(self, value):

        if self.head is None:
            return 
        
        currentNode = self.head.next
        prevNode = self.head

        while currentNode and currentNode.next:

            if currentNode.value == value:
                prevNode.next = currentNode.next
                currentNode.next = None
                currentNode = prevNode.next
                continue
            prevNode = currentNode
            currentNode = currentNode.next

        if self.head == value:
            nextnode = self.head.next
            self.head.next = None
            self.head = nextnode

    def displayData(self):

        if self.head is None:
            return 
        
        temp = self.head
        result = []

        while temp:
            result.append(temp.value)
            temp = temp.next

        print("->".join(map(str, result)))
    
    def reverse(self):

        if self.head is None:
            return 
        
        prevNode = None
        temp = self.head

        while temp:

            nextnode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextnode

        self.head = prevNode

    def oddAndEven(self):

        if self.head is None:
            return 

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

    def palindrome(self):
        pass

    def middle(self):

        left = self.head
        right = self.head

        while right.next:
            left = left.next
            if right.next.next:
                right = right.next.next
            else:
                right = right.next

        return left.value
    
    def sort(self):

        zeros = None
        zerohead = None
        ones = None
        onehead = None
        twos = None
        twohead = None

        temp = self.head

        while temp:
            nextnode = temp.next
            temp.next = None

            if temp.value == 0:
                if zeros is None: 
                    zeros = temp
                    zerohead = temp
                else:
                    zeros.next = temp
                    zeros = temp
            elif temp.value == 1:
                if ones is None:
                    ones = temp
                    onehead = temp
                else: 
                    ones.next = temp
                    ones = temp
            else:
                if twos is None:
                    twos = temp
                    twohead = temp
                else: 
                    twos.next = temp
                    twos = temp
            temp = nextnode

        if zerohead is not None:
            self.head = zerohead
            if onehead is not None:
                zeros.next = onehead
                if twohead is not None:
                    ones.next = twohead
            elif twohead is not None:
                zeros.next = twohead
        elif onehead is not None:
            self.head = onehead
            if twohead is not None:
                ones.next = twohead
        else:
            self.head = twohead

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list2 = LinkedList()
list2.append(3)
list2.append(4)
list2.append(5)
list2.append(6)
list2.append(7)
list2.append(8)
list2.append(9)

# list1.displayData()
# list2.displayData()


# print(list1.value, list2.value)
# print(list1, list2)
# print(list1.head, list2.head)
def mergeList(list1, list2):

    result = LinkedList()

    while list1 or list2:

        if list1 is not None:
            if list2 is not None:
                if list1.value < list2.value:
                    result.append(list1.value)
                    list1 = list1.next
                else:
                    result.append(list2.value)
                    list2 = list2.next
            else:
                result.append(list1.value)
                list1 = list1.next
        else:
            result.append(list2.value)
            list2 = list2.next

    return result

def mergeList(list1, list2):

    prevlist1 = None

    while list1 and list2:

        if list1.value == list2.value:
            nextlist2 = list2.next
            list2.next = list1.next
            list1.next = list2
            list2 = nextlist2
            prevlist1 = list1
            list1 = list1.next

        elif list1.value > list2.value:
            nextlist2 = list2.next
            list2.next = list1
            if prevlist1:
                prevlist1.next = list2
                prevlist1 = list2
            else:
                prevlist1 = list2

            list2 = nextlist2

        else:
            nextlist2 = list2.next
            list2.next = list1.next
            list1.next = list2
            prevlist1 = list1
            list1 = list1.next

def removeDuplicate(head):

    if head is None or head.next is None:
        return head
    
    prev = head
    temp = head.next

    # while temp:

    #     if prev.

# merge = mergeList(list1.head, list2.head)
# merge.displayData()

def removeNthNode(head, n):

    fast = head
    slow = head

    while n:
        fast = fast.next
        n -= 1

    if fast is None:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    if slow.next.next:
        slow.next = slow.next.next
    else:
        slow.next = None

    return head

# result = removeNthNode()
data = LinkedList()
data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
data.append(6)

# data.displayData()
# data.head = removeNthNode(data.head, 2)
# data.displayData()
# result.displayData()

def swapNodes(head):

    if head is None or head.next is None:
        return head
    
    left = head
    right = head.next

    while left and left.next:
        
        left.value, right.value = right.value, left.value
        left = right.next
        if left and left.next:
            right = left.next

def rotateList(head, n):

    if head is None or head.next is None:
        return head
    
    size = 1
    current = head

    while current.next:
        current = current.next
        size += 1

    n = n % size

    if not n:
        return head
    slow = fast = head
    while n:
        fast = fast.next
        n -= 1

    while fast.next:
        fast = fast.next
        slow = slow.next

    temp = slow.next
    slow.next = None

    fast.next = head
    head = temp

    return head

# data.head = removeNthNode(data.head, 2)
# data.displayData()
# swapNodes(data.head)
# data.displayData()
data = LinkedList()
# data.append(1)
# data.append(2)
# data.head = rotateList(data.head, 9)
# data.displayData()

# def removeDuplicates(head):
        
#         if head is None or head.next is None:
#             return head
        
#         left = head
#         right = head.next

#         while right:

#             if left.value == right.value:
#                 left.next = right.next
#                 right.next = None
#                 right = left.next
#             else:
#                 left = right
#                 right = right.next

#         return head
def removeDuplicates(head):

    if head is None or head.next is None:
        return head
    
    headDuplicate = False
    if head.value == head.next.value:
        headDuplicate = True

    temp = head.next
    prev = head

    while temp and temp.next:

        if temp.value == temp.next.value:
            prev.next = temp.next.next
            temp = prev.next
        else:
            temp = temp.next

    if headDuplicate:
        # head = head.next
        if head.next:
            if head.value == head.next.value:
                head = head.next.next
                return head
        else:
            return head.next

    return head

# data.append(1)
# data.append(2)
# data.append(2)
# data.append(2)

data.head = removeDuplicates(data.head)
data.displayData()

def partition(head, x):

    if head is None or head.next is None:
        return head
    
    smallerNodes = None
    smallerHead = None

    temp = head.next
    prev = head

    while temp:

        if temp.value < x:
            prev.next = temp.next
            temp.next = None
            if smallerNodes is None:
                smallerNodes = temp
                smallerHead = temp
            else:
                smallerNodes.next = temp
                smallerNodes = temp
            temp = prev.next
        else:
            prev = temp
            temp = temp.next

    if head.value < x:
        newhead = head.next
        head.next = smallerHead
        smallerHead = head
        head = newhead

    if smallerNodes:
        smallerNodes.next = head
        return smallerHead
        
    return head

# data.append(1)
# data.append(2)
# data.append(3)
# data.append(8)
# data.append(7)
# data.append(4)
# data.append(5)
# data.append(6)

# data.append(1)
# data.append(4)
# data.append(3)
# data.append(2)
# data.append(5)
# data.append(2)

# data.append(1)
# data.append(1)

# data.head = partition(data.head, 1)
# data.displayData()

# print(result.displayData)
# data.displayData()
# print(result.value)

# def reverse(head):

#     if head is None or head.next is None:
#         return head
    
#     prev = None
#     temp = head

#     while temp:
#         nextnode = temp.next
#         temp.next = prev
#         prev = temp
#         temp = nextnode

#     print('ritesh')

#     return [prev, head]

# def reverse2(head, left, right):

#     if head is None or head.next is None:
#         return head
    
#     rightpointer = leftpointer = head

#     while left - 2 or right - 1:

#         if left-2:
#             leftpointer = leftpointer.next
#             left -= 1
#         if right-1:
#             rightpointer = rightpointer.next
#             right -= 1

#     reverseHead = leftpointer.next
#     leftpointer.next = None
#     nextRight = rightpointer.next
#     rightpointer.next = None
#     right = nextRight

#     headpointer, tailpointer = reverse(reverseHead)
#     leftpointer.next = headpointer
#     tailpointer.next = rightpointer

#     return head

class linkedList:

    def __init__(self, value=0):
        self.value = value
        self.next = None

def reverseList(head, left, right):

    if head is None or left == right:
        return head

    dummy = linkedList(-1)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    start = prev.next
    then = start.next

    for _ in range(right-left):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return dummy.next

def removeDuplicates(head):

    dummy = linkedList(-1)
    dummy.next = head
    prev = dummy

    while head:

        if head.next and head.value == head.next.value:
            while head.next and head.value == head.next.value:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next

    return dummy.next

class ListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next

def deleteDuplicates(head):
    
    if not head or not head.next:
        return head

    dummy = ListNode(-1, head)
    prev = dummy

    while head:
        if head.next and head.value == head.next.value:
            while head.next and head.value == head.next.value:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next

    return dummy.next

data.append(1)
data.append(2)
data.append(3)
data.append(3)
data.append(4)
data.append(4)
data.append(5)
# data.head = removeDuplicates(data.head)
data.head = deleteDuplicates(data.head)
# data.displayData()

list1 = LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

list2.append(3)
list2.append(4)
list2.append(5)

# list1.displayData()
# def mergeList(list1, list2):

#     if not list1:
#         return list2
#     if not list2:
#         return list1

#     temp1 = list1
#     temp2 = list2

#     while temp1.next:

#         if temp2.next:
#             temp2 = temp2.next
#         temp1 = temp1.next

# class Node:

#     def __init__(self, value, random=None, next=None):
#         self.value = value
#         self.random = random
#         self.next = next

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def append(self, value, random=None):
#         newnode = Node(value, random)

#         if not self.head:
#             self.head = newnode
#             return 
        
#         currentnode = self.head
#         while currentnode.next:
#             currentnode = currentnode.next

#         currentnode.next = newnode
#         currentnode = newnode


list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
# list.append(6)

list.displayData()

def reorder(head):

    if not head or not head.next:
        return head

    stack = []
    temp = head.next

    while temp.next:
        stack.append(temp)
        temp = temp.next

    if not stack:
        return head

    start = head
    second = stack.pop()
    last = temp

    while start:
        second.next = None
        last.next = start.next
        start.next = last
        start = last.next
        if start == last or start == second:
            break
        last = second
        second = stack.pop()

    return head

list.head = reorder(list.head)
list.displayData()

def insertionLL(head):

    temp = head

    while temp:
        key = temp.value
        


arr = [9,8,7,6,5,4,3,2,1]
def insertionSort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

print(insertionSort(arr))


    
