string = ')())'

def requiredParenthesis(arr):

    stack = []
    counter = 0 
    for i in range(len(arr)):

        if arr[i] == "(":
            stack.append(arr[i])
        elif arr[i] == ")":
            if not stack:
                counter += 1
            else:
                stack.pop()

    return counter + len(stack)

# print(requiredParenthesis(string))

string = "{[()]}"

# print(string)

def validBrackets(string):

    bracketSet = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for char in string:

        if char in bracketSet:
            if not stack or stack[-1] != bracketSet[char]:
                return False
            stack.pop()

        elif char in bracketSet.values():
            stack.append(char)

        else:
            continue

    return len(stack) == 0


# print(validBrackets(string))

username = ["ritesh", "vivek"]
username1 = ["ritesh", "vivek"]

user = {
    "name": "ritesh laxman gupta"
}

user1 = {
    "name": 'ritesh laxman gupta'
}

# print(user == user1)
# print(username == username1)

string1 = "ab#c"
string2 = "ad#c"

def processString(string):

    stack = []

    for char in string:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return stack

def validString(string1, string2):
    return processString(string1) == processString(string2)

print(validString(string1, string2))

string = "(aa(bdc))p(de)((j))"

def bracketNumber(string):

    stack = []
    counter = 0
    result = ""
    

    for char in range(len(string)):

        if string[char] == ")":
            if not stack:
                return False
            result += str(stack.pop())

        elif string[char] == "(":
            counter += 1
            stack.append(counter)
            result += str(counter)

        else:
            continue

    return result

print(bracketNumber(string))