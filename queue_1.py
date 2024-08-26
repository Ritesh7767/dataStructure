# class Queue:

#     first = -1

#     def __init__(self, size):
#         self.arr = [-1] * size

#     def Enqueue(self, n):
#         if self.first == len(self.arr)-1:
#             print("Queue overflow")
#             return
#         self.first += 1
#         self.arr.append(n)
#         # self.arr.append(self.first += 1)

#     def Dequeue(self, n):
#         if self.first == -1:
#             print("Queue underflow")
#             return 
#         self.arr.pop(self.first)
#         self.first -= 1

#     def isEmpty(self):
#         return len(self.arr) == 0
    
#     def isFull(self):
#         return self.first == len(self.arr) - 1
    
# queue = Queue(5)
# print(queue.arr)

# queue.Enqueue(7)
# queue.Enqueue(3)
# queue.Enqueue(4)
# queue.Enqueue(1)

# print(queue.arr)

# class Queue:

#     def __init__(self):
#         self.arr = []

#     def Enqueue(self, n):
#         self.arr.append(n)

#     def Dequeue(self):
#         if not self.arr:
#             raise IndexError("Dequeue from an empty queue")
#         self.arr.pop(0)

#     def isEmpty(self):
#         return True if not self.arr else False
    
#     def peek(self):
#         return self.arr[0]
    
#     def size(self):
#         return len(self.arr)
    
# queue = Queue()

# queue.Enqueue(7)
# queue.Enqueue(7)
# queue.Enqueue(7)
# queue.Enqueue(7)

# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()

# print(queue.arr)


# def printQueue(arr):

#     for i in range(len(arr)):
#         print(arr.pop(0))

# def printQueue(arr):


#     for i in range(len(arr)):
#         element = arr.pop(0)
#         print(element)
#         arr.append(element)

#     return arr


# print(printQueue(arr))
# printQueue(arr)

# def reversalQueue(arr):

    # result = []
    # for i in range(len(arr)):
    #     result.append(arr.pop())

    # for i in range(len(arr)-1, -1, -1):
    #     arr.append(arr.pop(i))

    # return arr

# def reversalQueueStack(arr):

#     stack = []

#     for _ in range(len(arr)):
#         stack.append(arr.pop(0))

#     while stack:
#         arr.append(stack.pop())

#     return arr

# print(reversalQueueStack(arr))
# print(reversalQueue(arr))

# def reverseKElement(k, arr):

#     stack = []

#     for i in range(k):
#         stack.append(arr.pop(0))
#     while stack:
#         arr.append(stack.pop())

#     for i in range(len(arr) - k):
#         arr.append(arr.pop(0))

#     return arr

# print(reverseKElement(4, arr))

def timeRequired(k, arr):

    time = 0
    index = arr.index(k)
    queue = [x for x in range(len(arr))]

    print(index, queue)

    while queue:
        time += 1
        current = queue.pop(0)
        arr[current] -= 1

        if arr[current] == 0 and current == index:
            break
        elif arr[current] != 0:
            queue.append(current)

    return time

arr = [2, 4, 5, 6]
# print(timeRequired(2,arr))


# def timeRequired(k, arr):
#     if k not in arr:
#         return -1  # Element not found

#     time = 0
#     index = arr.index(k)
#     queue = list(range(len(arr)))

#     while queue:
#         time += 1
#         current = queue.pop(0)
#         arr[current] -= 1

#         if arr[current] == 0 and current == index:
#             return time
#         elif arr[current] != 0:
#             queue.append(current)

#     return time

# arr = [2, 1, 5, 6]
# print(timeRequired(1, arr))  # Output should be corrected based on actual problem statement


# class StackAsQueue:
    
#     stack1 = []
#     stack2 = []
    
#     def push(self, n):
#         self.stack2.append(n)

#     def pop(self):
#         if not self.stack1:
#             if not self.stack2:
#                 print("Queue Underflow")
#                 return
#             else:
#                 while self.stack2:
#                     self.stack1.append(self.stack2.pop())

#         return self.stack1.pop()
    
#     def peek(self):
#         if not self.stack1:
#             if not self.stack2:
#                 return -1
#             else:
#                 return self.stack2[0]
            
#         else:
#             return self.stack1[-1]
        
#     def isEmpty(self):
#         if not self.stack1:
#             if not self.stack2:
#                 return True
#             else:
#                 return False
#         else:
#             return False


# stack = StackAsQueue()

# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.stack1, stack.stack2)
# print(stack.peek())

# stack.pop()
# print(stack.stack1, stack.stack2)


# stack.pop()
# stack.pop()

# print(stack.isEmpty())
# print(stack.peek())

# stack.pop()


# print(stack.stack1, stack.stack2)
# stack.pop()

def windowWithSizeK(k, arr):

    # left = 0
    # right = k - 1
    queue = []
    index = k - 1

    

    # while right < len(arr):

    #     queue.append(arr[left:right + 1])
    #     left += 1
    #     right += 1

    # while queue:
    #     print(queue.pop(0))

    return queue

# arr = [3,6,2,7,8,11, 12]
# windowWithSizeK(3, arr)

def firstNegativeWindow(k, arr):

    queue = arr[0:k-1]
    print(queue)
    result = []
    for i in range(k-1, len(arr)):
        queue.append(arr[i])

        noNegative = True

        for element in queue:
            if element < 0:
                noNegative = False
                result.append(element)
                break

        if noNegative:
            result.append(0)

        queue.pop(0)
    
    return result


arr = [2,-3,-4,-2,7,8,9,-10]
k = 3

