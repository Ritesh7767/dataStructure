
def minString(string):
    
    mapping = {
        "A": "B",
        "C": "D"
    }
    stack = []
    for char in string:
        
        if stack and (stack[-1] == "A" or stack[-1] == "C"):
            if char == mapping[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    return "".join(stack)


def clearDigits(string):

    stack = []

    for char in string:
        if ord(char) >= 48 and ord(char) <= 57:
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

# string = "ABFCACDB"
string = "cb34"
# print(clearDigits(string))

# print("Hello world")