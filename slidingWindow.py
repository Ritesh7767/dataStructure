name = "abcabcdefghabcd"

def minString(string):

    char_index_map = {}

    for s in string:
        if s in char_index_map:
            char_index_map[s] += 1
        else:
            char_index_map[s] = 1

    print(len(char_index_map.items()))
    numberCharacter = len(char_index_map.items())

    start = 0
    end =  numberCharacter - 1
    char_index_map = {}
    minString = ""

    # for c in range(len(string)):

    #     if c in char_index_map:
            

        # if c not in char_index_map:
        #     numberCharacter -= 1

        # if numberCharacter == 0:
            # minString = string[start:c+1]
            # print(minString)

        # while(numberCharacter != 0)

        # if end - start + 1 > 8: 
        #     start += 1

    # return minString

# response = minString('ritehsdsflk')
# print(response)


        
        
        



# minString(name)

# frequency = {}
# for s in name:
#     if s in frequency:
#         frequency[s] += 1
#     else:
#         frequency[s] = 1

# print(frequency)


# def frequency(string):

#     char_index_map = {}

#     print(string)

#     for s in string:
#         print(s)
#         if s in char_index_map:
#             char_index_map[s] += 1
#         else:
#             char_index_map[s] = 1

#     return char_index_map


# response = frequency("ritesh")
# print(response)

# def minString(arr):

#     char_index_map = {}

#     for i in arr:
#         if i in arr:
#             char_index_map[i] += 1
#         else:
#             char_index_map[i] = 1

#     return char_index_map

# response = minString(name)
# print(response)

# def maxSubstring(arr):

#     start = 0
#     maxLength = 0
#     char_index_map = {}
#     maxString = ""

#     for end in range(len(arr)):


#         if arr[end] in char_index_map:
#             start = max(start, char_index_map[arr[end]] + 1)
#         char_index_map[arr[end]] = end

#         sum = end - start + 1
#         if maxLength < sum:
#             maxString = arr[start:end+1]
#             maxLength = sum

#     return maxLength, maxString

# response = maxSubstring(name)

# print(response)
        


# def maxSubstring(string):

#     start = 0
#     maxlength = 0
#     char_index_map = {}
#     substring = ""

#     for end in range(len(string)):

#         if string[end] in char_index_map:
#             start = max(start, char_index_map[string[end]] + 1)
#         char_index_map[string[end]] = end

#         print(start, end)

#         if end + 1 - start + 1 > maxlength:
#             maxlength = end + 1 - start + 1
#             print(maxlength)
        
#     return maxlength

# response = maxSubstring("ritesh")

# print(response)

    # start = 0
    # maxlength = 0
    # char_index_map = {}

    # for end in range(len(string)):

    #     if string[end] in string:
    #         start = max(start, char_index_map[string[end]] + 1)
    #     char_index_map[string[end]] = end

    #     if (end + 1) - (start + 1) > max_length:
    #         max_length = (end + 1) - (start + 1)
        
    # return maxlength

# response = maxSubstring(name)

# def frequency(string){
#     response = {}
#     for s in string:
#         if s in string:

# }

# result = {}
# for s in name:
#     if s in result:
#         result[s] += 1
#     else:
#         result[s] = 1

# print(result)

# user = {
#     "name": "ritesh",
#     "salary": 50000
# }

# for s in user:
#     print(s)

# if "name" in user:
#     print(user["name"])

# if "ritesh" in user:
#     print(user)
# def longestString(arr):
#     start = 0
#     end = 0
#     longestString = ""


def substring(string):

    left = 0
    
    for right in range(2, len(string)):

        print(string[left:right+1])
        left += 1

string = "ritesh"
# substring(string)

# def uniqueSubString(string):

#     left = 0
#     char_map_index = {}

#     for right in range(len(string)):

#         if string[right] in char_map_index:
#             left = max(left, char_map_index[string[right]]+1)
#         print(string[left:right])
#         char_map_index[string[right]] = right 

#     print(string[left])

# uniqueSubString("aababcabc")

# def uniqueSubString(string):

#     left = 0
#     char_map_index = {}

#     for right in range(len(string)):

#         if string[right] in char_map_index:
#             left = max(left, char_map_index[string[right]]+1)
#             if len(string[left:right+1]) == 3:
#                 print(string[left:right+1])
#         char_map_index[string[right]] = right

#     print(string[left:])

# string = "aababcabc"
# uniqueSubString(string)

# def uniqueSubString(string):

#     left = 0
#     char_index_map = {}

#     for right in range(len(string)):

#         if string[right] in char_index_map:
#             print(string[left:right])
#             left = max(left, char_index_map[string[right]]+1)
#         char_index_map[string[right]] = right

# uniqueSubString(string)

def subString3(string):

    if len(string) < 3:
        return

    left = 0
    count = 0
    for right in range(2, len(string)):

        print(string[left:right+1])
        print(set(string[left:right+1]))
        if len(set(string[left:right+1])) == 3:
            count += 1

        left += 1

    return count

string = "xyzzaz"
# result = subString3(string)
# print(result)

colors = [0,1,0,0,1]
# color = [0,1,0,0,1,0,1]

def differentCombination(colors):

    if len(colors) < 3:
        return 
    
    colors.append(colors[0])
    colors.append(colors[1])

    left = 0
    
    for right in range(2,len(colors)):

        if colors[left] == colors[right] and colors[left+1] != colors[left]:
            print(colors[left:right+1])
        left += 1
    
# colors = [0,0,1]
# differentCombination(colors)


def rightSum(number):

    result = sum(number)
    rightSum = []

    for i in range(len(number)):
        result -= number[i]
        rightSum.append(result)

    return rightSum

def leftSum(number):

    result = sum(number)
    leftSum = []
    for i in range(len(number)-1, -1, -1):

        result -= number[i]
        leftSum.append(result)

    return leftSum[::-1]

def leftSumPointer(number):

    leftSum = [0]
    sum = 0
    for i in range(1, len(number)):
        sum += number[i-1]
        leftSum.append(sum)

    return leftSum

# def rightSumPointer(number):

#     rightSum = [0]
#     sum = 0

#     number = number[::-1]
#     for i in range(1, len(number)):
#         sum += number[i]
#         rightSum.append(sum)

#     return rightSum[::-1]

def rightSumPointer(number):

    rightSum = []
    sum = 0

    for i in range(len(number)-1, -1, -1):
        
        if i == len(number)-1:
            rightSum.append(0)
            continue

        sum += number[i+1]
        rightSum.append(sum)

    return rightSum[::-1]

# def leftRightDifference(number):

#     leftSum = [0]
#     rightSum = [0]

#     lsum = 0
#     rsum = 0

#     for i in range(1, len(number)):
#         lsum += number[i-1]
#         leftSum.append(lsum)

#     for j in range(len(number)-2, -1, -1):
#         rsum += number[j+1]
#         rightSum.append(rsum)

#     rightSum = rightSum[::-1]
#     print(leftSum, rightSum)
#     result = []
#     for i in range(len(leftSum)):
#         result.append(abs(leftSum[i]-rightSum[i]))

#     return result

def leftSumDifference(number):

    summation = sum(number)
    lsum = 0
    result = []

    for i in range(len(number)):

        summation -= number[i]
        if i == 0:
            result.append(abs(0-summation))
            continue
        lsum += number[i-1]
        result.append(abs(lsum - summation))

    return result

number = [10,4,8,3]
number = [1]
# print(leftSumDifference(number))
# print(leftRightDifference(number))


# print(leftSumPointer(number))
# print(rightSumPointer(number))
# print(rightSum(number))
# print(leftSum(number))

def runningSum(number):

    sum = 0

    for i in range(len(number)):
        sum += number[i]
        number[i] = sum

    return number

number = [1,2,3,4]
# print(runningSum(number))

# def pivotInteger(number):
    
#     arr = []
#     for i in range(1, number+1):
#         arr.append(i)

#     leftSum = 0
#     rightSum = sum(arr)

#     for i in range(len(arr)):
#         if leftSum == rightSum:
#             return i
#         rightSum -= arr[i]
#         if i == 0:

#     return -1

# print(pivotInteger(8))

string = "YazaAay"

def longestNiceString(string):

    if len(string) <= 1:
        return ""
    
    mapping = {}
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()

    for i in range(len(upper)):
        mapping[upper[i]] = lower[i]
        mapping[lower[i]] = upper[i]

    left = 0
    char_map_index = {}
    char_map_index[string[left]] = True
    for right in range(1, len(string)):
        if mapping[string[right]] in char_map_index:
            if mapping[string[right]]:
                return string[left:right+1]
            else: mapping[string[right]] = True
        else: mapping[string[right]] = True
        char_map_index[string[left]] = False
        left += 1

# longestNiceString(string) 

def nextGreaterElement(nums):

    stack = []
    result = [-1] * len(nums)
    for right in range(len(nums)):
        while stack and nums[right] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[right]
        stack.append(right)

    return result

# nums = [1,3,4,2]
nums1 = [4,1,2]
nums2 = [1,3,4,2]
# print(nextGreaterElement(nums))


def nextGreater(nums1, nums2):

    mapping = {}
    for i in range(len(nums2)):
        mapping[nums2[i]] = i

    result = [-1]*len(nums2)
    stack = []

    for right in range(len(nums2)):
        while stack and nums2[right] > nums2[stack[-1]]:
            index = stack[-1]
            result[index] = nums2[right]
        stack.append(right)

    result2 = []
    for j in range(len(nums2)):
        index = mapping[nums1[j]]
        result2.append(result[index])

    return result2

def nextGreater(nums1, nums2):

    result = [-1] * len(nums2)
    stack = []
    mapping = {}
    for right in range(len(nums2)):
        while stack and nums2[right] > nums2[stack[-1]]:
            index = stack.pop()
            result[index] = nums2[right]
        mapping[nums2[right]] = right
        stack.append(right)

    result1 = []
    for i in range(len(nums1)):
        index = mapping[nums1[i]]
        result1.append(result[index])

    return result1

nums1 = [2,4]
nums2 = [1,2,3,4]
# print(nextGreater(nums1, nums2))

ops = ["5","-2","4","C","D","9","+","+"]

def footBall(ops):

    stack = []

    for i in ops:
        if i == "+":
            topElement = stack[-1]
            secondElement = stack[-2]
            stack.append(topElement + secondElement)
        elif i == "C":
            stack.pop()
        elif i == "D":
            topElement = stack[-1]
            stack.append(topElement * 2)
        else:
            stack.append(int(i))
    print(stack)
    return sum(stack)
ops = ["5","2","C","D","+"]
# print(footBall(ops))

# print("+")
# print(int("9"))
# print(int("-"))

string1 = [1,2,3]
string2 = [1,2,3]

# print(string1 == string2)

string = "ritesh"

# print(string[:-1])

string += ' laxman gupta'
# print(string)

s = "(()())(())"

def removeOutermost(string):

    result = []
    opened = 0

    for char in string:
        if char == "(":
            if opened > 0:
                result.append(char)
            opened += 1
        elif char == ")":
            if opened > 1:
                result.append(char)
            opened -= 1

    return "".join(result)

s = "(()())(())(()(()))"
# s = "((()))"
# print(removeOutermost(s))

string = "leEeetcode"

def greatString(string):

    stack = []
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    mapping = {}

    for i in range(len(lower)):
        mapping[lower[i]] = upper[i]
        mapping[upper[i]] = lower[i]

    for char in string:

        if stack and char == mapping[stack[-1]]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)
string = "s"
result = greatString(string)
# print(result)

folder = ["d1/","d2/","../","d21/","./"]

def folderOperations(folder):

    stack = []

    for ope in folder:
        if ope == "../":
            stack.pop()
        elif ope == "./":
            continue
        else:
            stack.append(ope)

    return len(stack)

# print(folderOperations(folder))

def maxNesting(string):

    level = 0
    maxi = 0

    for char in string:

        if char == ")":
            level -= 1
        elif char == "(":
            level += 1
            maxi = max(maxi, level)
        else:
            continue

    return maxi

string = "(1+(2*3)+((8)/4))+1"
# print(maxNesting(string))


students = [1,1,0,0]
sandwiches = [0,1,0,1]

def countStudents(students, sandwiches):

    count = [students.count(0), students.count(1)]

    for sandwich in sandwiches:

        if count[sandwich]:
            count[sandwich] -= 1
        else: 
            break

    return sum(count)         

result = countStudents(students, sandwiches) 
# print(result)

