
def removeDuplicate(arr):

    left = 0
    right = 1

    while right < len(arr):

        if arr[left] == arr[right]:
            arr.pop(left)
            continue
        left += 1
        right += 1

    return arr

# arr = [1,1,2,2,2,2,3,3,4,5,5,5]

# def removeValues(arr, value):

#     pointer = 0

#     while pointer < len(arr):

#         if arr[pointer] == value:
#             arr.pop(pointer)
#             continue
#         pointer += 1

#     return arr

# print(removeValues(arr, 3))

# print(removeDuplicate([1])) 

# """this is comment"""

# def sampleFunction():
#     return 1, 2

# print(sampleFunction())

# def twoSum(arr, value):

#     left = 0
#     right = len(arr)-1

#     while left < right:

#         sum = arr[left] + arr[right]

#         if sum == value:
#             return [left, right]
#         elif sum < value:
#             left += 1
#         else:
#             right -= 1

#     return -1

# arr = [1,2,3,4]
# print(twoSum(arr, 3))

# def twoSum(arr, value):

#     left = 0
#     right = 0
#     sum = arr[left]

#     for right in range(len(arr)):

        # if sum == value:
        #     return [left, right]
        # elif sum < value:
        #     sum -= arr[left]
        #     left += 1
        

    # return -1

# arr = [3,2,4]
# print(twoSum(arr, 7))

# string1 = "butchsad"
# string2 = "sad"

# def firstOccurence(string1, string2):

#     pointer1 = 0
#     pointer2 = 0
#     resultString = ""

#     for right in range(len(string1)):

#         if string1[right] == string2[pointer2]:
#             pointer1 = right
#             resultString += string1[right]
#             pointer2 += 1

#         if resultString == string1:
#             return True
        
# print(firstOccurence(string1, string2))


# def permute(arr):

#     if not arr:
#         return []
    
#     if len(arr) == 1:
#         return arr
    
#     permutations = []

#     for i in range(len(arr)):
#         currentElement = arr[i]

        

# arr = [1,2,3,4,5]
# print(arr[:0], arr[1:])

# def permute(nums):
    # Base case: if the list is empty, return an empty list
    # if len(nums) == 0:
    #     return []
    
    # Base case: if the list has one element, return a list with one permutation (itself)
    # if len(nums) == 1:
    #     return [nums]
    
    # List to store all permutations
    # permutations = []
    
    # Iterate through each element in the list
    # for i in range(len(nums)):
        # Get the current element
        # current = nums[i]
        
        # Remaining list after removing the current element
        # remaining_list = nums[:i] + nums[i+1:]
        
        # Recursive call to permute the remaining list
    #     for p in permute(remaining_list):
    #         permutations.append([current] + p)
    
    # return permutations

# Example usage
# items = [1, 2, 3]
# result = permute(items)

# def permute(arr):

#     if len(arr) == 0:
#         return []

#     if len(arr) == 1:
#         return [arr]
    
#     permutation = []

#     for i in range(len(arr)):
#         currentElement = arr[i]

#         remaningElement = arr[:i] + arr[i+1:]

#         for p in permute(remaningElement):
#             permutation.append([currentElement] + p)

#     return permutation

# arr = [1,2,3]
# print(permute(arr))
    


# def permute(arr):

#     if len(arr) == 0:
#         return []
    
#     if len(arr) == 1:
#         return [arr]
    
#     permutation = []

#     for i in range(len(arr)):
#         current = arr[i]
#         remaningArr = arr[:i] + arr[i+1:]

#         for p in permute(remaningArr):
#             permutation.append([current] + p)

    

#     return permutation

# arr = [1,1,2]
# print(permute(arr))



# def firstOccurence(string1, string2):

#     if len(string2) > len(string1):
#         return -1
    
#     left = 0
#     right = len(string2) - 1

#     while right < len(string1):
#         if string1[left:right+1] == string2:
#             return left
#         left += 1
#         right += 1

#     return -1

# string1 = "sadabadsad"
# string2 = "sada"
# print(firstOccurence(string1, string2))


def longestSubString(string):

    maxLength = 0
    left = 0
    char_index_map = {}
    
    for right in range(len(string)):

        if string[right] in char_index_map:
            left = max(left, char_index_map[string[right]] + 1)
        char_index_map[string[right]] = right

        if right - left + 1 > maxLength:
            maxLength = right - left + 1
    
    return maxLength

string = "abcdefgh"
# print(longestSubString(string))

# def reverseNumber(num):

number = 123
strNumber = str(number)
# print(strNumber[1])
# print(str(number))
# print(number[1])

# print(abs(-123))
# print(str(-123))

# print(len(457))
# def reverseNumber(number):

# print(765*-1)
# def reverseNumber(number):

#     left = 0
#     isNegative = False
#     if number < 0:
#         left = 1
#         isNegative = True
    
#     strNumber = str(number)
#     right = len(strNumber)-1

#     while left < right:
#         strNumber[left], strNumber[right] = strNumber[right], strNumber[left]
#         left += 1
#         right -= 1

#     number = int(strNumber)
#     return number

# print(reverseNumber(123))

# def reverseString(string):

#     result = ""

#     for right in range(len(string)-1,-1,-1):
#         result += string[right]

#     return result

# print(reverseString("ritesh"))

# print(123[::-1])

# print(list(map(int, 123)))

# def reverseNumber(number):

#     result = ""
#     strNumber = str(number)

#     if number < 0:
#         for i in range(len(strNumber)-1,0,-1):
#             result += strNumber[i]
#         return int(result) * -1

#     for i in range(len(strNumber)-1, -1, -1):
#         result += strNumber[i]
#     return int(result)

# print(reverseNumber(-12))

def reverseNumber(number):

    result = ""
    strNumber = str(number)
    end = 0 if number < 0 else -1

    for i in range(len(strNumber)-1, end, -1):
        result += strNumber[i]

    result = int(result)
    if not end:
        return result * -1
    return result 

# print(reverseNumber(-321))

# def isPalindrome(number):

#     number = str(number)
#     reverseNumber = number[::-1]

#     if reverseNumber == number:
#         return True
#     return False

# def isPalindrome(x):
    
#     x = str(x)
#     reverseString = x[::-1]

#     if reverseString == x:
#         return "true"
#     return "false"

# print(isPalindrome(121))
    

# def isValid(string):

#     stack = []

#     for i in string:

#         if i == ")" or i == "]" or i == "}":
#             stack.pop()


# def rotateMatrix(matrix):

#     resultMatrix = []
#     for col in range(len(matrix[0])):
#         sample_matrix = []
#         for row in range(len(matrix)):
#             sample_matrix.append(matrix[row][col])
#         resultMatrix.append(sample_matrix[::-1])

    # for row in resultMatrix:
    #     left = 0
    #     right = len(row) - 1

    #     while left < right:
    #         row[left], row[right] = row[right], row[left]
    #         left += 1
    #         right -= 1

    # return resultMatrix

# def rotateMatrix(matrix):

#     for i in range(len(matrix)):
#         for j in range(i+1, len(matrix)):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     for i in range(len(matrix)):
#         matrix[i].reverse()

#     return matrix

# print(rotateMatrix())

# def spiralOrder(matrix):

#     result = []

#     while matrix:

#         result += matrix.pop(0)

#         if matrix and len(matrix[0]):
#             for row in matrix:
#                 result.append(row.pop())

#         if matrix and len(matrix[0]):
#             result += matrix.pop()[::-1]

#         if matrix and len(matrix[0]):
#             for row in matrix[::-1]:
#                 result.append(row.pop(0))

#     return result

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[7],[9],[6]]
# print(spiralOrder(matrix))
# print(rotateMatrix(matrix))

# def isValid(string):

#     char_index_map = {
#         ")": "(",
#         "]": "[",
#         "}": "{"
#     }

#     stack = []

#     for char in string:

#         if char in char_index_map:
#             top_element = stack.pop() if stack else "#"

#             if char_index_map[char] != top_element:
#                 return False
#         else:
#             stack.append(char)

#     return not stack

# print(isValid("()"))

# def func(x,y):

#     if x == 0:
#         return y
    
#     return func(x-1, x+y)

# print(func(4,3))


# a,b = [1,2]

# print(a, b)

# def binaryConverter(num):

#     if num == 1:
#         return "1"
#     if num == 0:
#         return "0"
    
#     return binaryConverter(num // 2) + str(num % 2)

# print(binaryConverter(13))

# print(3/2)

# class node:

#     def __init__(self, data):
#         self.data = data
#         self.head = None

# class linkedList:

#     def __init__(self):
#         self.data

# class Node:

#     def __init__(self, data = None):
#         self.data = data
#         self.next = None


# class linkedList:

#     def __init__(self):
#         self.head = None
    
#     def append(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             return 
        
#         lastNode = self.head
        
#         while lastNode.next:
#             lastNode = lastNode.next
#         lastNode.next = newNode

#     def prepend(self, data):
#         newNode = Node(data)

#         newNode.next = self.head
#         self.head = newNode

#     def deleteWithValue(self, data):

#         if self.head is None:
#             return 
#         if self.head.data == data:
#             self.head = self.head.next
#             return 
        
#         currentNode = self.head

#         while currentNode.next:

#             if currentNode.next.data == data:
#                 currentNode.next = currentNode.next.next
#                 return
#             currentNode = currentNode.next

#     def displayNode(self, data):

#         if self.head is None:
#             return
        
#         currentNode = self.head

#         node = []        
#         while currentNode.next:
#             node.append(currentNode.data)
#             currentNode = currentNode.next
#         print("->".join(map(str, node)))



# arr = [-1,1,1,2,3]
# arr = [2,3,4,5,6,7,8,9]

# def countPairs(arr, target):

#     arr.sort()
#     print(arr)
#     left = 0
#     right = len(arr)-1
#     count = 0
#     while left < right:

#         sum = arr[left] + arr[right]

#         if sum >= target:
#             right -= 1
#         else:
#             print(right)
#             for i in range(left, right + 1):
#                 for j in range(i+1, right + 2):
#                     print(arr[i], arr[j])
#                     count += 1
#             break

#     return count

# arr = [-1,1,1,2,3]
# print(countPairs(arr, target))
        

# def countPairs(arr, k):

#     arr.sort()
#     print(arr)
#     right = len(arr)-1
#     count = 0

#     while right:

#         sum = arr[0] + arr[right]

#         if sum >= k:
#             right -= 1
#         else:
#             print(sum)
#             count += 1
#             right -= 1

#     return count

# def countPairs(arr,k):

#     left = 0
#     right  = len(arr)-1
#     count = 0

#     while left < right:

#         sum = arr[left] + arr[right]

#         if sum >= k:
#             right -= 1
#         else:
#             count += (right - left)
#             left += 1

#     return count

# arr = [-6,2,5,-2,-7,-1,3]
# target = -2
# print(countPairs(arr, target))

# def reversePrefix(string, ch):

#     left = 0

#     for right in range(len(string)):

#         if string[right] == ch:
#             while left < right:
#                 string[left], string[right] = string[right], string[left]
#                 right -= 1
#             break

# def reverseString(string, left, right):

#     if left > right:
#         return ""
    
#     return string[right] + reverseString(string, left + 1, right - 1) + string[left]

# string = "ritesh"
# print(reverseString(string, 0, len(string)-1))


def reverseString(string, left, right):

    if left > right:
        return ""
    return string[right] + reverseString(string, left+1, right-1) + string[left]

string = "ritesh"
# print(reverseString(string, 0, len(string)-1))

# def reversePrefix(string, ch):

#     result = ""
#     add = False
#     findPrefix = True

#     for i in range(len(string)):
#         if string[i] == ch and findPrefix:
#             result += reverseString(string, 0, i+1)
#             print(result)
#             add = True
#             findPrefix = False
#         if add:
#             result += string[i]

#     return result

# string = "ritesh",
# ch = "t"
# print(reversePrefix(string, ch))

# def reversePrefix(string, ch):

#     arr = list(string)

#     for i in range(len(arr)):

#         if arr[i] == ch:
#             left = 0
#             right = i

#             while left < right:
#                 arr[left], arr[right] = arr[right], arr[left]
#                 left += 1
#                 right -= 1
#             break

#     result = ""
#     for i in arr:
#         result += i

#     return result

# string = "ritesh"
# ch = "z"
# print(reversePrefix(string, ch))

# name = list("ritesh")
# print(name)
# print(type(str(name)))

# print(list("ritesh"))
    
def minAverageSum(arr):

    average = []
    arr.sort()
    left= 0
    right = len(arr)-1

    while left < right:

        avg = (arr[left] + arr[right])/2
        average.append(avg)
        left += 1
        right -= 1

    return min(average)

arr = [1,9,8,3,10,5]
arr = [7,8,3,4,1,15,13,4]
# print(minAverageSum(arr))

def minimumAverage(nums):
        
        average = []
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            avg = (nums[left] + nums[right])/2
            average.append(avg)
            left += 1
            right -= 1

        print(average)
        return min(average)

# print(minimumAverage(arr))



# def arithmeticTriplet(nums, diff):
    
    # if len(nums) == 1 or not len(nums):
    #     return 
    
    # left = 0
    # right = 1

    # i = j = k = 0
    # arr = []
    # while right < len(nums):
    #     result = nums[right] - nums[left]

    #     if result == diff:
    #         print(nums[left], nums[right], result)
    #         arr += [left, right]
    #         left += 1
    #         right += 1
    #     elif result < diff:
    #         right += 1
    #     else:
    #         left += 1

    # return arr

# nums = [0,1,4,6,7,10]
# diff = 3
# arr = arithmeticTriplet(nums, diff)
# print(len(arr)//3)
# print(print(len(arr)//3))
        
def arithmeticTriplet(arr, diff):

    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[j] - arr[i] == diff and arr[k] - arr[j] == diff:
                    count += 1

    return count

nums = [4,5,6,7,8,9]
diff = 2
# print(arithmeticTriplet(nums, diff))

def isPalindrome(string):

    left = 0
    right = len(string)-1

    while left < right:

        if string[left] is not string[right]:
            return False
        left += 1
        right -= 1

    return True

def firstPalindrome(words):

    for i in words:
        response = isPalindrome(i)
        if response:
            return i
    return ""

words = ["abc","car","ada","racecar","cool"]
# print(firstPalindrome(words))
# print(isPalindrome("ada"))

# s = "LeetcodeHelpsMeLearn" 
# spaces = [8,13,15]

# def addSpaces(string, spaces):

#     result = []
#     pointer = 0

#     for i in range(len(string)):

#         if pointer != len(spaces):
#             if spaces[pointer] == i:
#                 result.append(" ")
#                 pointer += 1

#         result.append(string[i])

#     string = ""
#     for ch in result:
#         string += ch

#     return string

# s = "HIUFyGKNyYQjrfcjOCRVxOqYnKyrnyKuWZpWBkYZTZLblxGUGHfSqYXtwztwTDhcgMMWLCljBoSLyGCtwzEUyNyZwDQTMAHkuyLufkwulkKmXtRnxOfylFhEBtBMUCsRyCCvqwoBErTELPHuDlqdvAjgmUZhwvKDCEvWpkGRBPXJcZPuwgRhPnyCderZUuBJYSzIoFPSzZAHnLEmDOfsTnfHoPyoFeZipoOTGZMNihbgvnZSNawjRavrWUkDOKJSqUrxBykZKsOObSGwbhBFILbsopCQvFapsEVdYhrGpwOtRdwwsQQlOfqUQkgkDiLVdruwsDYHmrIZJYsGDcFdIykxVdVgbNhLFNouvepCJOxvToaEXLklAHsPAYQpupODdsvpavVPtNqLDiTrZqQbhwrztdjHNehVStrOxeVeJbRxlAsClGarqcbDzdSjRHyKWQzYPGzbGxtFUptsZWQhmKbWhAXYtDzHypQYZCsBshHbpiYZnFEqtnoBvGbXEofCsJHCpOtGonTcIZplxoTCGMPHSsGsYVzfveaGaqGWeLyakTwBOHqCnFMywNZBXTYCzeCDqyDWoPzqBiIXMzwZBKBkxdSHuywwzTTcuaOEgTrtLyIXiXtXgZqePHDCXdJKPyUeRUaqKuoiSdOAEFRGOMieQgPJIdgYhgbsoeh"
# spaces = [0,1,2,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,123,125,126,127,128,129,130,132,133,134,135,136,138,139,140,141,142,144,146,147,148,149,150,151,152,153,154,155,157,159,161,162,163,164,166,168,169,170,171,174,175,176,177,178,179,180,181,184,185,187,188,189,190,191,193,194,195,196,197,198,199,200,201,202,203,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,227,228,229,231,232,233,234,235,236,238,239,240,241,242,243,244,245,248,249,250,252,253,254,255,256,257,258,259,260,262,263,267,268,269,270,271,272,273,274,275,276,278,279,280,281,282,284,285,286,287,288,289,291,292,294,296,297,298,300,301,303,304,305,306,307,309,310,311,312,313,315,316,317,318,320,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,351,352,353,354,355,357,358,359,360,361,362,363,364,365,366,367,368,369,371,372,373,375,376,377,378,379,380,381,382,383,385,387,388,389,390,391,393,394,395,396,397,398,399,400,401,402,405,407,408,409,410,412,413,415,416,417,418,420,421,422,424,425,426,427,428,429,430,432,433,434,435,436,437,439,440,441,443,444,445,446,448,449,450,451,452,453,454,457,458,459,460,461,462,463,464,466,467,469,470,471,472,474,475,476,477,478,479,480,481,482,483,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,501,503,504,505,506,508,509,511,512,513,514,515,517,518,519,520,521,522,523,524,525,527,528,530,531,532,533,534,536,537,538,539,540,541,542,543,544,546,547,548,550,553,554,555,556,557,558,559,560,561,562,563,566,567,568,570,571,572,573,574,575,576,579,580,581,582,583,588,589,590,592,593,594,596,597,598,599,601,602,603,604,605,606,607,608,610,611,612,614,615,616,617,618,619,620,621,622,623,624,626,627,628,629,630,631,632,633,634,636,637,638,639,640,641,642,643,644,645,646,647,648,649,651,652,653,654,655,656,657,658,660,661,662,663,664,665,666,667,669,670,671,672,673,675,676,677,678]

# print(addSpaces(s, spaces))


# def reverseSentences(string):

#     arr = string.split(" ")

#     for i in arr

def reverseString(string, left, right):

    if left > right:
        return ""
    
    if left == right:
        return string[left]
    
    return string[right] + reverseString(string, left + 1, right - 1) + string[left]

string = "ritesh"
# print(reverseString(string, 0, len(string)-1))

def reverse2(string):

    arr = string.split(" ")

    for i in range(len(arr)):

        reversedString = reverseString(arr[i], 0, len(arr[i])-1)
        arr[i] = reversedString
    
    return " ".join(arr)

# print(reverse2("ritesh laxman gupta"))

class ReverseString:

    def __init__(self, string):
        self.string = string

    def reverse(self, string = None, left = 0, right = None):

        if string is None:
            string = self.string

        if right is None:
            right = len(self.string)-1

        if left > right:
            return ""
        
        if left == right:
            return string[left]
        
        return string[right] + self.reverse(string, left+1, right-1) + string[left]
    
ritesh = ReverseString('ritesh')
# print(ritesh.reverse())


def reverseMatrix(matrix):

    for row in matrix:

        left = 0
        right = len(row) - 1

        while left < right:

            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

        for i in range(len(row)):
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0

    return matrix

image = [[1,1,0],[1,0,1],[0,0,0]]
# print(reverseMatrix(image))

def makePalindrome(string):

    arr = list(string)
    left = 0
    right = len(arr)-1

    while left < right:

        if arr[left] != arr[right]:
            minimum = min(arr[left], arr[right])
            arr[right] = arr[left] = minimum

        right -= 1
        left += 1

    return "".join(arr)

string = "abcd"
# print(makePalindrome(string))

def mergeWordAlternate(string1, string2):

    length = min(len(string1), len(string2))
    
    result = ""
    pointer = 0

    while pointer < length:

        result += string1[pointer] + string2[pointer]
        pointer += 1

    if len(string1) > len(string2):
        result += string1[pointer:]
    elif len(string1) < len(string2):
        result += string2[pointer:]

    return result

string1 = "riteshabc"
string2 = "gupta"
# print(mergeWordAlternate(string1, string2))
    

def diMatchString(string):

    n = len(string)

    low = 0
    high = n

    result = []
    for ch in string:

        if ch == "I":
            result.append(low)
            low += 1

        else:
            result.append(high)
            high -= 1

    print(low, high)
    result.append(low)

    return result

string = "IDID"
# print(diMatchString(string))

# def removePalindrome(word):

#     left = 0
#     string = list(word)
#     right = len(string)-1
#     count = 0

#     while left < right:

#         if string[left] == string[right]:
#             left += 1
#             right -= 1

#         elif string[left] < string[right]:
#             string.pop(left)
#             count += 1
        
#         else:
#             string.pop(right)
#             count += 1

#     return count

# string = "abb"
# print(removePalindrome(string))

# def removePalindrome(word):

#     if word == word[::-1]:
#         return 1
#     else:
#         return 2
    

# string = "aabbaaab"
# print(removePalindrome(string))

# def sortArrayByParity(arr):

#     size = len(arr)
#     left = 0
#     right = size -1 

#     while left < right:

#         while arr[left] % 2 == 0 and left < size:
#             left += 1

#         while arr[right] % 2 != 0 and right >= 0:
#             right -= 1

#         if arr[left] % 2 != 0 and arr[right] % 2 == 0:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1

#     return arr

# arr = [3,1,2,4]
# arr = [2,4,6,8]
# print(sortArrayByParity(arr))


arr = [0,1,1,0,0,1,1]
def seperate(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        if arr[left] != 1:
            left += 1
        if arr[right] != 0:
            right -= 1

        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# print(seperate(arr))


def sortByParity(arr):

    left = 0
    right = len(arr)-1

    while left < right:

        if arr[left] % 2 != 0 and arr[right] % 2 == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        if arr[left] % 2 == 0:
            left += 1
        if arr[right] % 2 != 0:
            right -= 1

    return arr

# arr = [3,1,2,4]
# arr = [0,1]
# print(sortByParity(arr))

nums1 = [1,2,2,1]
nums2 = [2,2]

# print(set(nums1))
def intersectionArray(arr1, arr2):

    arr1 = set(arr1)
    arr2 = set(arr2)

    return list(arr1.intersection(arr2))

# print(intersectionArray(nums1, nums2))

nums = [-1,2,-3,3]
# nums = [-4,-3,-1,2,3]
def longestPositive(nums):

    nums.sort()
    left = 0
    right = len(nums)-1

    while left < right and nums[left] < 0 and nums[right] > 0:

        lvalue = abs(nums[left])
        rvalue = nums[right]
        
        if lvalue == rvalue:
            return rvalue
        
        elif lvalue > rvalue:
            left += 1

        else:
            right -= 1

    return -1

# nums = [-1,10,6,7,-7,1]
# nums = [-1,-2,-3,-4]
# print(longestPositive(nums))

def powerOf(number, power):

    if power == 0:
        return 1
    if power == 1:
        return number
    
    return number * powerOf(number, power - 1)

# print(powerOf(2, 5))

def binaryToDecimal(number):

    string = str(number)
    result = 0
    count = 0
    for i in string[::-1]:
        result += int(i) * powerOf(2, count)
        count += 1

    return result

# print(binaryToDecimal(1101))

class Node:

    def __init__(self, data=None):
        self.val = data
        self.next = None

class SinglyLinkedList:

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

    def display(self):

        if self.head is None:
            return 
        
        currentNode = self.head
        result = []
        while currentNode:
            result.append(currentNode.val)
            currentNode = currentNode.next

        print("->".join(map(str, result)))
    
    def middle(self):

        slow = self.head
        fast = self.head
        size = 1

        while fast and fast.next:
            size += 2
            slow = slow.next
            fast = fast.next.next

        return slow.val

data = SinglyLinkedList()

data.append(3)
data.append(2)
data.append(1)
data.append(0)
data.append(-1)
data.append(-2)
data.append(-3)
data.append(-4)
# data.display()

# print(data.middle())


arr1 = [1,2,2,3,4,5]
arr2 = [4,4,3,2,1,1]

def matchingElement(arr1, arr2):

    left = 0
    right = len(arr2)-1

    while right > -1 and left < len(arr1):

        if arr1[left] == arr2[right]:
            print(arr1[left], arr2[right])
            left += 1
            right -= 1

        elif arr1[left] < arr2[right]:
            left += 1
        else:
            right -= 1


arr1 = [1, 3, 5, 7]
arr2 = [7, 5, 3, 1]
# matchingElement(arr1, arr2)
# def bubbleSort(arr):

#     limit = 0

#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
            
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

arr = [23,25,41,18,14,54]
# print(bubbleSort(arr))


# def bubbleSort(arr):

#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# def bubbleSort(arr):

#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr 

# print(bubbleSort(arr))

arr = [3,4,5,1,6,2]

# def selectionSort(arr):

#     for i in range(len(arr)):
#         min = i
#         for j in range(i+1, len(arr)):
#             if arr[min] > arr[j]:
#                 min = j

#         arr[i], arr[min] = arr[min], arr[i]

#     return arr

# def selectionSort(arr):

#     for i in range(len(arr)):
#         min = i

#         for j in range(i+1, len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]

#     return arr

# def selectionSort(arr):

#     for i in range(len(arr)):
#         min = i
#         for j in range(i+1, len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]

#     return arr

# def bubbleSort(arr):

#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# def bubbleSort(arr):

#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# def selectionSort(arr):

#     for i in range(len(arr)):
#         min = i
#         for j in range(i+1, len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]

#     return arr            

# print(bubbleSort(arr))
# print(selectionSort(arr))

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def insertionSort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
    
    return arr

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    # print("Hello ritesh")
    return arr

def insertionSort(arr):
    
    for i in range(0, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    print("Hello world")
    return arr

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    return arr

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key

    return arr

def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key

    return arr
        
def selectionSort(arr):

    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr

def mergeSort(arr):

    while len(arr) > 1:
        
        mid = len(arr)//2
        leftPart = arr[:mid]
        rightPart = arr[mid:]

        mergeSort(leftPart)
        mergeSort(rightPart)


        

arr = [64, 34, 25, 12, 22, 11, 90]
# print("insertion sort", insertionSort(arr))
# print("bubble sort", bubbleSort(arr))
# print("selection sort", selectionSort(arr))

arr1 = [1,2,3,4]
arr2 = [3,4,5,6]

def mergeTwo(arr1, arr2):

    if not arr1:
        return arr2
    elif not arr2:
        return arr1
    
    result = []
    left = 0
    right = 0

    while left < len(arr1) and right < len(arr2):

        if arr1[left] == arr2[right]:
            result.append(arr1[left])
            result.append(arr2[right])
            left += 1
            right += 1
        elif arr1[left] < arr2[right]:
            result.append(arr1[left])
            left += 1
        else:
            result.append(arr2[right])
            right += 1

    if left < len(arr1):
        while left < len(arr1):
            result.append(arr1[left])
            left += 1

    else:
        while right < len(arr2):
            result.append(arr2[right])
            right += 1

    return result

result = mergeTwo(arr1, arr2)
# print(result)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def mergeList(nums1, nums2):

    i = len(nums1)-1
    j = len(nums2)-1
    k = len(nums1)+len(nums2)-1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

# print(mergeList(nums1, nums2))


def isPalindrome(string):
    
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    mapping = {}

    for i in alpha:
        mapping[i] = True

    left = 0
    right = len(string)-1

    print(string[left], string[right])

    while left <= right:

        lchar = string[left].lower()
        rchar = string[right].lower()

        if lchar not in mapping or rchar not in mapping:
            if lchar not in mapping:
                left += 1
            if rchar not in mapping:
                right -= 1
        else:
            if lchar != rchar:
                return False
            else:
                left += 1
                right -= 1

    return True

string = "A man, a plan, a canal: Panama"
string = "0P"
# print(len(string))
# print(isPalindrome(string))

# def isPalindrome2(string):

    # deleteCount = 0

    # left = 0
    # right = len(string)-1

    # while left <= right:

    #     if string[left] == string[right]:
    #         left += 1
    #         right -= 1
    #     else:
    #         if not deleteCount:
    #             right -= 1
    #             deleteCount += 1
    #         else:
    #             return False
            
    # return True

def isPalindrome2(string):

    reverseString = string[::-1]
    first = 0
    second = 0
    count1 = False
    count2 = False

    while second < len(string):

        if string[first] != reverseString[second]:
            if not count2:
                second += 1
                count2 = True
            elif not count1:
                first += 1
                count1 = True
            else:
                return False
        else:
            first += 1
            second += 1
    else:
        return True

# string = "abc"
# string = "deeeee"
# string = "cbbcc"
# string = "cdbeeeabddddbaeedebdc"
# print(isPalindrome2(string))

def reverseVowel(string):

    arr = list(string)
    left = 0
    right = len(string)-1
    vowels = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }

    while right >= left:

        if arr[left].lower() not in vowels or arr[right].lower() not in vowels:
            if arr[left].lower() not in vowels:
                left += 1
            if arr[right].lower() not in vowels:
                right -= 1
        else: 
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return "".join(arr)

string = "hello"
string = ""
string = "Euston saw I was not Sue."
output = "euston saw I was not SuE."
# print(reverseVowel(string))

# print("ritesh".split(""))
# print(list("ritesh"))


def dupilcates(arr, k):

    mapping = {}
    left = 0
    right = 0

    while right < k:
        if arr[right] in mapping:
            return True
        mapping[arr[right]] = True
        right += 1

    while right < len(arr):

        if arr[right] in mapping:
            if mapping[arr[right]]:
                return True
            else:
                mapping[arr[right]] = True
        else:
            mapping[arr[right]] = True
        right += 1
        mapping[arr[left]] = False
        left += 1

    return False

arr = [1,2,3,1,2,3]
arr = [1,0,1,1]
k = 1
# print(dupilcates(arr, k))
# def maxSubArr(arr):

#     maxi = float('-inf')
#     avg = 0
#     left = 0
#     sum = 0
#     maxArr = []
#     for right in nums:
#         sum += right
        
#         if maxi < sum:
#             maxi = sum
#             maxArr = arr[left:right+1]

#         if sum < 0:
#             sum = 0

#     return maxi

def maxSubArr(nums):

    left = 0
    maxi = float('-inf')
    avg = 0
    maxArr = []
    sum = 0

    for right in range(len(nums)):
        sum += nums[right]

        if maxi < sum:
            maxi = sum
            maxArr = nums[left:right+1]
            average = maxi/(right+1)
            avg = max(avg, average)
        if sum < 0:
            sum = 0
            left = right + 1

    return maxi, maxArr, avg 

# print(maxSubArr(nums))

def maxSubArr(nums,k):

    window_sum = sum(nums[:k])
    left = 0 
    maxi = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[left]

        if maxi < window_sum:
            maxi = window_sum
        
        left += 1
    return maxi/k


nums = [1,12,-5,-6,50,3]
k = 4
# print(maxSubArr(nums, k))

def kBeauty(num, k):

    string = str(num)
    left = 0
    right = k
    count = 0
    while right < len(arr):
        divisor = int(string[left:right])
        print(string[left:right])

        if num % divisor == 0:
            count += 1
        left += 1
        right += 1

    return count

# print(kBeauty(num, k))

def subArr(arr, k):

    left = 0
    right = k-1

    while right < len(arr):

        print(arr[left:right+1])
        left += 1
        right += 1

arr = [1,2,3,4,5,6,7,8,9]
k = 3
# subArr(arr, k)

def kBeauty(number, k):

    string = str(number)
    left = 0
    right = k-1
    count = 0

    while right < len(string):
        divisor = int(string[left:right+1])

        # print(divisor)
        if divisor == 00:
            left += 1
            right += 1
            continue
        elif number % divisor == 0:
            count += 1
        left += 1
        right += 1
    return count

num = 430043
k = 2
result = kBeauty(num, k)
# print(result)


def defuseTheBomb(codes, k):

    limit = len(codes)
    result = [0] * limit

    if k == 0:
        return result
    elif k > 0:
        for i in range(k):
            codes.append(codes[i])
    else:
        index = limit-1
        for _ in range(abs(k)):
            codes.insert[0, codes[index]]
    print(codes)

code = [5,7,1,4]
k = -2
print(defuseTheBomb(code, k))

arr = [1,2,3,4,5]
arr.insert(0, 10)
print(arr)