# arr = [4,5,6,7,8,9]
# key = 2

# def insertBottom(key, arr):

#     top = -1
#     stack = []

#     for i in range(len(arr)):
#         top += 1
#         stack.append(arr.pop())

#     arr.append(key)

#     while top != -1:
#         arr.append(stack[top])
#         top -= 1

#     return arr

# print(insertBottom(key, arr))

arr = [2,3,5,-4,6,-2,-8,9]

def beautifulMaker(arr):

    stack = []
    top = -1

    for i in range(len(arr)):

        if top == -1:
            stack.append(arr[i])
            top += 1

        elif arr[i] >= 0:
            if stack[top] >= 0:
                stack.append(arr[i])
                top += 1
            else:
                stack.pop()
                top -= 1

        else:
            if stack[top] < 0:
                stack.append(arr[i])
                top += 1
            else:
                stack.pop()
                top -= 1

    return stack

print(beautifulMaker(arr))

arr = ["ab", "ac", "da", "da", "ac", "db", "ea"]

def beautifulStringMaker(arr):

    stack = []
    top = -1

    for i in range(len(arr)):
        if top == -1:
            stack.append(arr[i])
            top += 1
        
        elif stack[top] == arr[i]:
            stack.pop()
            top -= 1
        
        else:
            stack.append(arr[i])
            top += 1

    return stack

print(beautifulStringMaker(arr))


string = "((())())()"

def validParenthesis(string):

    stack = []

    for char in string:

        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0



def func1(n):

    if n == 0:
        return -1
    
    else:
        func1(n - 1)

    return -1


# def validParenthesis(string):

#     stack = []
#     top = -1

#     for i in range(len(string)):

#         if top == -1:
#             stack.append(string[i])
#             top += 1

#         elif string[i] == "(":
#             if stack[top] == "(":
#                 stack.append(string[i])
#                 top += 1
#             else:
#                 stack.pop()
#                 top -= 1

#         else:
#             if stack[top] == ")":
#                 stack.append(string[i])
#                 top += 1
#             else:
#                 stack.pop()
#                 top -= 1

#     print(stack)
#     return True if top == -1 else False

print(validParenthesis(string))
            