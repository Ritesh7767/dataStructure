# arr = [8,6,4,7,4,9,10,8,12]

# def nearestGreaterElement(arr):

#     stack = []
#     nextGreaterElement = [-1] * len(arr)

#     for i in range(len(arr)):

#         while stack and arr[i] < arr[stack[-1]]:
#             nextGreaterElement[stack[-1]] = arr[i]
#             stack.pop()

#         stack.append(i)

#     return nextGreaterElement

# print(nearestGreaterElement(arr))

# arr = [7,9,12,10,14,8,3,6,9]

# def nextSmallerElement(arr):

#     stack = []
#     nextSmallerElement = [-1]*len(arr)

#     for i in range(len(arr)):

#         while stack and arr[i] < arr[stack[-1]]:
#             index = stack.pop()
#             nextSmallerElement[index] = arr[i]

#         stack.append(i)

#     return nextSmallerElement
# print(nextSmallerElement(arr))

# def leftSmallerElement(arr):

#     stack = []
#     resultArr = [-1] * len(arr)
#     for i in range(len(arr)-1, -1, -1):

#         while stack and arr[i] < arr[stack[-1]]:
#             resultArr[stack.pop()] = arr[i]

#         stack.append(i)

#     return resultArr
# arr = [4,13,11,5,9,7,8,6]
# print(leftSmallerElement(arr))

# def leftGreaterElement(arr):

#     stack = []
#     resultArr = [-1]*len(arr)

#     for i in range(len(arr)-1, -1, -1):

#         while stack and arr[i] > arr[stack[-1]]:
#             resultArr[stack.pop()] = arr[i]

#         stack.append(i)

#     return resultArr

# print(leftGreaterElement(arr))

# def nextGreaterElement2(arr):

#     stack = []
#     resultArr = [-1]*len(arr)

#     for i in range(len(arr)):

#         while stack and arr[i] > arr[stack[-1]]:
#             resultArr[stack.pop()] = arr[i]

#         stack.append(i)

#     # print(stack)

#     for i in range(len(stack)-1, 0, -1):
        
#         if arr[stack[i]] < arr[stack[0]]:
#             resultArr[stack.pop()] = arr[stack[0]]

#     return resultArr

# arr = [11,10,7,4,8,9,4]

# def stockSpanProblem(arr):

#     stack = []
#     result = [1]*len(arr)

#     for i in range(len(arr)):

#         while stack and arr[i] >= arr[stack[-1]]:
#             stack.pop()

#         if not stack:
#             result[i] = i+1
#         else:
#             result[i] = i - stack[-1]

#         stack.append(i)

#     return result


# arr = [100,80,55,70,60,75,85]
# print(stockSpanProblem(arr))

    # stack = []
    # result = [1]*len(arr)

    # for i in range(len(arr)-1, -1, -1):

    #     while stack and arr[i] > arr[stack[-1]]:
    #         result[stack[-1]] = stack[-1] - i
    #         stack.pop()

    #     stack.append(i)

    # return result

# def stockSpanProblem(arr):

#     stack = []
#     result = [1]*len(arr)

#     for i in range(len(arr)):



# print(stockSpanProblem(arr))

# def stockSpanProblem(arr):

#     stack = []
#     result = [-1]*len(arr)
#     for i in range(len(arr)-1, -1 -1):

#         while stack and arr[i] > stack[-1]:
#             result[stack[-1]] = stack.pop()            


# def largestRectangle(arr):

#     stack = []
#     result = 0
#     for i in range(len(arr)):

#         while stack and arr[i] < arr[stack[-1]]:
#             index = stack.pop()
#             height = arr[index]
#             width = i+1 if not stack else i - stack[-1]
#             result = max(result, height * width)

#         stack.append(i)

    # while stack
    # print(stack)
    # return result


# def largestRectangle(arr):
#     stack = []
#     result = 0
#     n = len(arr)

#     for i in range(n):
#         while stack and arr[i] < arr[stack[-1]]:
#             index = stack.pop()
#             height = arr[index]
#             width = i if not stack else i - stack[-1] - 1
#             result = max(result, height * width)

#         stack.append(i)

#     # Process remaining bars in stack
#     while stack:
#         index = stack.pop()
#         height = arr[index]
#         width = n if not stack else n - stack[-1] - 1
#         result = max(result, height * width)

#     return result

# # Example usage:
# histogram = [2, 1, 5, 6, 2, 3]
# max_area = largestRectangle(arr)
# print(max_area)  # Output: 10

# def largestRectangle(arr):

#     stack = []
#     result = 0
#     n = len(arr)
#     for i in range(len(arr)):
        
#         while stack and arr[i] < arr[stack[-1]]:
#             index = stack.pop()
#             height = arr[index]
#             width = i if not stack else i - stack[-1] -1 
#             result = max(result, width*height)

#         stack.append(i)
    
#     while stack:
#         index = stack.pop()
#         height = arr[index]
#         width = n if not stack else n - stack[-1] -1
#         result = max(result, width*height)

#     return result
            

# arr = [2,3,4,2,6,5,4,5,1]
# print(largestRectangle(arr))

# arr = [[1,2,3], [4,5,6]]

# def waveForm(arr):

#     for col in range(len(arr[0])):

#         if col % 2 == 0:
#             for row in range(len(arr)):
#                 print(arr[row][col])
#         else:
#             for row in range(len(arr)-1, -1, -1):
#                 print(arr[row][col])

# waveForm(arr)

# result = []
# arr = [[1,2,3],[4,5,6]]

# result += arr[0]
# result.append(arr[1][2])
# print(arr[1][2])
# result += arr[1]
# print(result)

# def spiralArr(matrix):

#     result = []

#     while matrix:

#         result += matrix.pop(0)

#         if matrix:
#             for row in matrix:
#                 if row:
#                     result.append(row.pop())

#         if matrix:
#             result += matrix.pop()[::-1]

#         if matrix:
#             for row in matrix[::-1]:
#                 if row:
#                     result.append(row.pop(0))

#     return result

# matrix = [[1,2,3,4,5],[20,21,22,23,6],[19,32,33,24,7],[18,31,34,25,8],[17,30,35,26,9],[16,29,28,27,10],[15,14,13,12,11]]
# print(spiralArr(matrix))


# matrix = [[1,2,3],[4,5],6,7]
# result = []

# result += matrix[0]
# print(result)

# result += matrix[1]
# result.append(matrix[1])
# print(result)

# result.append(matrix[2])
# print(result)



# def transposeMatrix(matrix):

#     result = []
#     for col in range(len(matrix[0])):
#         sampleMatrix = []
#         for row in range(len(matrix)):
#             sampleMatrix.append(matrix[row][col])
#         result.append(sampleMatrix)

#     return result

# response = transposeMatrix(matrix)
# print(response)


# def matrixRotation90(matrix):

#     resultMatrix = []

#     for col in range(len(matrix[0])):
#         sampleMatrix = []
#         for row in range(len(matrix)):
#             sampleMatrix.append(matrix[row][col])
#         resultMatrix.append(sampleMatrix)

#     for row in resultMatrix:
#         left = 0
#         right = len(resultMatrix[0])-1

#         while left < right:
#             row[left], row[right] = row[right], row[left]
#             left += 1
#             right -= 1

#     return resultMatrix

# matrix = [[1],[2]]
# print(matrixRotation90(matrix))

def rotateMatrix180(matrix):

    left = 0
    right = len(matrix[0])-1

    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1

    for row in matrix:
        print(row)
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    return matrix

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# print(rotateMatrix180(matrix))

def rotateAntiClockWise(matrix):

    result = []
    
    for col in range(len(matrix[0])):
        sampleMatrix = []
        for row in range(len(matrix)):
            sampleMatrix.append(matrix[row][col])
        result.append(sampleMatrix)

    left = 0
    right = len(matrix) -1

    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1

    return result

# print(rotateAntiClockWise(matrix))

def rotateClockWise(matrix):

    result = []

    for col in range(len(matrix[0])):
        sampleMatrix = []
        for row in range(len(matrix)):
            sampleMatrix.append(matrix[row][col])
        result.append(sampleMatrix)

    for row in result:
        left = 0
        right = len(result[0])-1

        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    return result

def rotateMatrix(k, matrix):

    result = matrix
    while k:
        result = rotateClockWise(result)
        k -= 1
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(rotateMatrix(5, matrix))
# print(rotateClockWise(matrix))

# def binarySearch(arr):

#     arr.sort()
#     left = 0
#     right = len(arr) -1

#     while left < right:
        
#         mid = left+right//2

# def celebrityProblem(matrix):j

#     candidate = 0
#     for i in range(1, len(matrix)):
#         if matrix[candidate][i] == 1:
#             candidate = i

#     for row in range(len(matrix)):
#         if row != candidate:
#             if matrix[candidate][row] == 1 or matrix[row][candidate] == 0:
#                 return -1
            
#     return candidate

# matrix = [[0,1,0,1,1],[0,0,0,1,1],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]
# print(celebrityProblem(matrix))

# class Stack:

#     stack = []

#     def push(self, n):
#         self.stack.append(n)

#     def pop(self):

#         if not self.stack:
#             print("Stack underflow")
#             return
#         self.stack.pop()

#     def getMinimum(self):
#         minimum = self.stack[0]

#         if not self.stack:
#             print("Stack is empty")
#             return

#         for i in range(1, len(self.stack)):
#             minimum = min(minimum, self.stack[i])

#         return minimum

# stack = Stack()
# stack.push(5)
# stack.pop()
# stack.push(10)
# stack.push(3)
# stack.push(2)
# print(stack.stack)
# print(stack.getMinimum())

# class Stack:

#     stack = []
#     minElement = []

#     def push(self, n):
#         self.stack.append(n)
#         if not self.minElement:
#             self.minElement.append(n)
#         else:
#             self.minElement.append(min(self.minElement[-1], n))

#     def pop(self):
#         if not self.stack:
#             print("Stack overflow")
#             return -1 
#         self.minElement.pop()
#         return self.stack.pop()
    
#     def getMinElement(self):

#         if not self.minElement:
#             print("Stack is empty")
#             return
#         return self.minElement[-1]
    
# stack = Stack()
# stack.push(5)
# stack.push(4)
# stack.push(7)
# stack.push(-1)

# print(stack.stack)
# print(stack.getMinElement())

# def makeTwoStack(arr):

#     left = 0
#     right = len(arr) -1

class TwoStack:

    left = -1
    
    def __init__(self, size):
        self.arr = [-1] * size
        self.right = size

    def push1(self, n):
        if self.left + 1 == self.right:
            print("Stack overflow")
            return 
        self.left += 1
        self.arr[self.left] = n

    def push2(self, n):
        if self.right - 1 == self.left:
            print("Stack overflow")
            return
        self.right -= 1
        self.arr[self.right] = n

stack = TwoStack(6)
stack.push1(1)
stack.push1(2)
stack.push1(3)
stack.push1(4)

# print(stack.arr, stack.left, stack.right)

stack.push2(9)
stack.push2(8)

print(stack.arr, stack.left, stack.right)

stack.push1(0)
print(stack.arr, stack.left, stack.right)

stack.push2(-4)
print(stack.arr, stack.left, stack.right)

# stack.push2(9)
