# def greeting(day):
    
#     if not day:
#         print("happy birthday")
#         return
#     print(f"{day} days for your birthday") 
#     greeting(day-1)


# greeting(5)

def reverseNumber(n):
    if n == 1:
        print(n)
        return 
    
    reverseNumber(n-2)
    print(n)

# reverseNumber(7)

# def nEvenNumber(n):

#     if n % 2 != 0:
#         n -= 1

#     print(n)
#     if n == 0:
#         return
#     nEvenNumber(n-2)

# nEvenNumber(8)

# def nEvenNumber(n):

#     while n:
#         print(n)
#         n-=2

# nEvenNumber(6)

# def factorial(n):

#     if n == 1:
#         return 1
#     return n* factorial(n-1)

# result = factorial(4)
# print(result)

# def factorialWhile(n):

#     result = n
#     while n != 1:
#         n -= 1
#         result *= n

#     return result

# print(factorialWhile(7))

# def sumOfN(n):

#     if n == 1:
#         return 1

#     return n + sumOfN(n-1)

# print(sumOfN(4))

# def powerOf2(n, power = 2):

#     if power == 1:
#         return n
#     return n*powerOf2(n,1)

# print(powerOf2(9))

# def powerOf2(n):

#     if n == 0:
#         return 1    
#     return 2 * powerOf2(n-1)

# print(powerOf2(5))

# def sumOfSquare(n):

#     if n == 1:
#         return 1
    
#     return n**2 + sumOfSquare(n-1)

# print(sumOfSquare(2))


def sumOfSquare(n):

    result = 0

    while n:
        result += n**2
        n-=1

    return result

# print(sumOfSquare(2))

# def fibonacci(n):

#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
    
#     return fibonacci(n-2) + fibonacci(n-1)

# response = fibonacci(10)
# print(type(response))
# print(fibonacci(10))


# def fibonacci(n):

#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(2))

# for i in range(1, 10):
#     print(fibonacci(i))

# def fibonacci(n):

#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1, 10):
#     print(fibonacci(i))


# def gcd(n1, n2):

#     if n2 == 0:
#         return n1

#     return gcd(n2, n1%n2)

# print(gcd(18, 48))

# def printArray(arr, index = 0):

#     if index == len(arr):
#         return

#     printArray(arr, index+1)
#     print(arr[index])

def printArray(arr, index = 0):

    if index == len(arr):
        return

    printArray(arr, index + 1)
    print(arr[index])

# printArray(arr)

def printArray1(arr, index):

    if index == -1:
        return 
    
    printArray1(arr, index - 1)
    print(arr[index])

# printArray1(arr, len(arr)-1)
# print(printArray1(arr, len(arr)-1))

# def sumOfElement(arr, index = 0):

#     if index == len(arr):
#         return 0
    
#     return arr[index] + sumOfElement(arr, index+1)

# print(sumOfElement(arr))

# def minimumElement(arr, index = 0):

#     if index == len(arr)-1:
#         return arr[index]
    
#     return min(arr[index], minimumElement(arr, index + 1))

# def maximumElement(arr, index = 0):

#     if index == len(arr) - 1:
#         return arr[index]
    
#     return max(arr[index], maximumElement(arr, index + 1))

# arr = [3,4,5,1]
# print(maximumElement(arr))
# print(minimumElement(arr))

# def isPalindrome(string):

#     left = 0
#     right = len(string) -1

#     while left < right:

#         if string[left] != string[right]:
#             return False
        
#         left += 1
#         right -= 1


#     return True

# print(isPalindrome('dad'))

def isPalindrome(string, right, left = 0):

    if string[left] != string[right - 1]:
        return False
    if left >= right-1:
        return True
        
    return isPalindrome(string, right - 1, left + 1)

# print(isPalindrome("racecar", 7 ))

# def countVowels(string):

#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for i in range(len(string)):

#         if string[i] in vowels:
#             count += 1

#     return count

# print(countVowels("ritesh"))

def countVowels(string, pointer = 0):

    if pointer == len(string):
        return 0
    
    if string[pointer] in ["a", "e", "i", "o", "u"]:
        return 1 + countVowels(string, pointer + 1)

    return countVowels(string, pointer + 1)

# print(countVowels("aeiou"))

# def reverseString(string, end, start = 0):

#     if start >= end - 1:
#         return
    
# def reverseString(string, end):

#     if end == 0:
#         return ""
    
#     return string[end-1] + reverseString(string, end - 1)

# print(reverseString("ritesh", 6))

def reverseString(string, left, right):

    if left >= right:
        return ""
    
    return string[right] + reverseString(string, left+1, right-1) + string[left]

# print(reverseString("ritesh", 0, len("ritesh")-1))

alphabets = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for i in range(len(alphabets)):
#     print(ord(alphabets[i]), ord(Alpha[i]))


# def toUpperCase(string):

#     left = 0
#     right = len(string) - 1
#     result = ""
    
#     while left <= right:

#         ascii = ord(string[left]) - 97
#         char = chr(ascii + 65)

#         result += char
#         left += 1

#     return result

# print(toUpperCase("ritesh"))

# def toUpperCase(string, start, end):

#     if start >= end:
#         return ""
    
#     ascii = ord(string)

#     return chr(ord(string[start]))

# def toUpperCase(string, left, right):

    # if left >= right:
    #     return ""
    
    # diffLeft = ord(string[left]) - 97
    # charLeft = chr(65 + diffLeft)

    # diffRight = ord(string[right]) - 97
    # charRight = chr(65 + diffRight)

    # return charLeft + toUpperCase(string, left + 1, right - 1) + charRight

# string = "jkflsjkfdsds"
# print(toUpperCase(string, 0, len(string)-1))

def toUpperCase(string, left, right):

    if left > right:
        return ""
    
    if left == right:
        return string[left].upper()

    return string[left].upper() + toUpperCase(string, left + 1, right - 1) + string[right].upper()

# print(toUpperCase("riteshj", 0, 6))

# def binarySearch(k, arr):

#     arr.sort()
#     left = 0
#     right = len(arr) - 1

#     while left > right:

#         result = (left + right)/2

#         if arr[result] == k:
#             return 1
#         elif arr[result] < k:
#             left = result
#         else:
#             right = result

#     return -1

# def binarySearch(k, arr):

#     arr.sort()

#     left = 0
#     right = len(arr) - 1

#     while left < right:

#         mid = (left + right)//2

#         if arr[mid] == k:
#             return k
        
#         elif arr[mid] < k:
#             left = mid + 1
        
#         else:
#             right = mid - 1

#     return -1

# arr = [4,5,3,6,7]
# print(binarySearch(3, arr))
        

# def binarySearch(k, arr, left, right):


#     if left > right:
#         return -1

#     mid = (left + right)//2

#     if arr[mid] == k:
#         return mid
#     elif arr[mid] < k:
#         return binarySearch(k, arr, mid + 1, right)
#     else:
#         return binarySearch(k, arr, left, mid - 1)

# arr = [1,2,3,4,5,6,7,8,9]
# print(binarySearch(2, arr, 0, len(arr)-1))

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1

            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

    return arr

# def mergeSort(arr):

#     while len(arr) > 1:
#         mid = len(arr)//2

#         leftHalf = arr[mid]
#         rightHalf = arr[mid:]

#         mergeSort(leftHalf)
#         mergeSort(rightHalf)

#         i = j = k = 0

#         while i < len(leftHalf) and j < len(rightHalf):
#             if leftHalf[i] < rightHalf[j]:
#                 arr[k] = leftHalf[i]
#                 i += 1
#             else:
#                 arr[k] = rightHalf[j]
#                 j += 1
#             k += 1
        
#         while i < len(leftHalf):
#             arr[k] = leftHalf[i]
#             i += 1
#             k += 1

#         while j < len(rightHalf):
#             arr[k] = rightHalf[j]
#             j += 1
#             k += 1

#     return arr


# def mergeSort(arr):

#     while len(arr) < 1:
        
#         mid = len(arr) // 2
#         leftHalf = arr[mid]
#         rightHalf = arr[mid:]

#         mergeSort(leftHalf)
#         mergeSort(rightHalf)

#         i = j = k = 0

#         while i < len(leftHalf) and j < len(rightHalf):

#             if leftHalf[i] < rightHalf[j]:
#                 arr[k] = leftHalf[i]
#                 i += 1
#             else:
#                 arr[k] = rightHalf[j]
#                 j += 1
#             k += 1

#         while i < len(leftHalf):
#             arr[k] = leftHalf[i]
#             i += 1
#             k += 1
        
#         while j < len(rightHalf):
#             arr[k] = rightHalf[j]
#             j += 1
#             k += 1

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf): 
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

    return arr
    


arr = [9,8,7,6,5,4,3,2,1]
# print(mergeSort(arr))
# mergeSort(arr)
# print(arr)
# print(mergeSort(arr))
# mergeSort(arr)
# print(arr)

def printNto1(number):

    if number == 1:
        print(number)
        return 

    print(number)
    printNto1(number-1)

# printNto1(10) 

def factorial(number):

    if number == 0:
        return 0
    if number == 1:
        return 1
    
    return number * factorial(number-1)

# print(factorial(3))

def reverseArray(arr, left=0, right=None):

    if right is None:
        right  = len(arr)-1
    
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]

    return reverseArray(arr, left + 1, right - 1)

arr = [1,2,3,4,5,6,7,8,9]
result = reverseArray(arr)
# print(result)

def isPalindrom(string, left=0, right=None):

    if right is None:
        right  = len(string)-1

    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return isPalindrom(string, left + 1, right - 1)

string = "racecar"
# print(isPalindrom(string))

def fibonacci(count):

    if count == 1:
        return 0
    if count == 2:
        return 1
    
    return fibonacci(count - 2) + fibonacci(count - 1)

# print(fibonacci(6))

arr = [2,3,2,3,5]

def frequency(arr,n):

    char_index_map = {}

    for i in range(1, n+1):
        char_index_map[i] = 0

    for i in arr:
        char_index_map[i] += 1
    return list(char_index_map.values())

# print(frequency(arr, 5))

# username = {
#     "firstname": "ritesh",
#     "lastname": "gupta", 
#     "middlename": "laxman"
# }

# print(username.keys())
# print(username.values())

def frequency(arr):

    char_index_map = {}

    for i in range(1, len(arr)+1):
        char_index_map[i] = 0

    for i in arr:
        char_index_map[i] += 1

    return char_index_map.values()

arr = [2,3,2,3,5]
arr = [3,3,3,3]
# print(frequency(arr))

def selectionSort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr    

def select(arr, i):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
    
def selectionSort(arr):

    for i in range(len(arr)):
        select(arr, i)

    return arr
    
arr = [9,8,7,6,5,4,3,2,1,0]
# print(selectionSort(arr))

# def bubbleSort(arr):

#     for i in range(len(arr)):
#         maximum = i
#         for j in range(i+1,len(arr)-i):
#             if arr[maximum] < arr[j]:
#                 maximum = j
                 

# def bubbleSort(arr):

#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)-1-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]

#     return arr

# print(bubbleSort(arr))

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def mergeSort(arr):
    
    if len(arr) > 1:

        mid = len(arr)//2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1
        
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

    return arr

# print(insertionSort(arr))
# print(mergeSort(arr))


def recurssiveBubble(arr, i, j):

    if j == len(arr)-1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        return 
    
    # if arr[]

def quickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)
    

# print(quickSort(arr))


# def powerOf2(n, ans=1):

#     if n == 1:
#         return True
#     if ans == n:
#         return True
#     if ans > n:
#         return False
#     ans *= 2
#     return powerOf2(n, ans)

# print(powerOf2(34))  

class Solution:

    def powerOf2(self, n, ans=1):

        if n == 1:
            return True
        elif ans == n:
            return True
        elif ans > n:
            return False
        ans *= 2
        return self.powerOf2(n, ans)
    
test = Solution()
result = test.powerOf2(16)
# print(result)

def fibo(n):

    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibo(n-1)+fibo(n-2)

# print(fibo(50))

def fib(n):
        
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)


# print(fib(3))

def power(base, index):

    if not index:
        return 1
    if index == 1:
        return base
    if index == -1:
        return 1/base
    
    if index > 0:
        return base * power(base, index-1)
    else:
        return 1/base * power(base, index+1)

# print(power(2, -2))

def binarySearch(arr, target, left = 0, right = None):
    
    if right is None:
        right = len(arr)

    if left > right:
        return -1
    
    mid = (left+right)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, left, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, right)
    
arr = [1,2,3,4,5,6,7,8,9]
# print(binarySearch(arr, 4))

def printN(n):

    if n == 1:
        return print(n)
    printN(n-1)
    print(n)

# printN(5)

def factorial(n):

    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(4))

def sumOfN(n):

    if n == 1:
        return 1
    return n + sumOfN(n-1)

# print(sumOfN(3))

# def productOfN(n):

#     if n % 100 == n:
#         return n
#     return n//100 * productOfN(n%100)

# print(productOfN(222))

def productOfN(n):

    if n % 10 == n:
        return n
    return n % 10 * productOfN(n//10)

# print(productOfN(222))

def reverseString(string, left = 0, right = None):

    if right is None:
        right = len(string)-1
    if left > right:
        return ""
    if left == right:
        return string[left]
    return string[right] + reverseString(string, left + 1, right - 1) + string[left]


string = "Ritesh"
# print(reverseString(string))
# def reverseNumber(number, left, right=None)

def isPalindrome(string, left=0, right=None):

    if right is None:
        right = len(string)-1
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return isPalindrome(string)

# print(isPalindrom(string))

string = "amanaplanacanalpanama"
number = 302

def countZero(number, count=0):

    num = number % 10
    if num == number:
        if num == 0:
            return count + 1
        else: 
            return count
    if num == 0:
        return countZero(number//10, count + 1)
    else:
        return countZero(number//10, count)
    
number = 203400
# print(countZero(number))

def isSorted(arr, left=0, right=None):

    if len(arr) <= 1:
        return True
    if right is None:
        right = len(arr)-1
    if left > right:
        return True
    if left == right:
        return arr[left] > arr[left-1]
    if arr[left] < arr[right]:
        return isSorted(arr, left+1, right-1)
    else:
        return False
    
arr = [1,2,3,4,5,6,7]
# print(isSorted(arr))
    
def linearSearch(arr, target, pointer=0, result=[]):

    if not arr:
        return -1
    if pointer == len(arr):
        return result
    if arr[pointer] == target:
        result.append(pointer)
        return linearSearch(arr, target, pointer + 1, result)
    else:
        return linearSearch(arr, target, pointer + 1)
    
arr = [4,3,2,5,73,3,2]
target = 3
# print(linearSearch(arr, target))

# arr = []

def power(base, index):

    if not index:
        return 1
    return base * power(base, index-1)

# print(power(2,3))

def nStair(steps):

    if steps == 1:
        return 1
    if steps == 2:
        return 2
    return nStair(steps-1) + nStair(steps-2)

# print(nStair(4))

def mazePath(rowpos, colpos, row, col):

    if rowpos == row or colpos == col:
        return 1
    return mazePath(rowpos+1, colpos, row, col) + mazePath(rowpos, colpos+1, row, col)

# print(mazePath(1,1,1,1))

def mazePath(row, col):

    if row == 1 or col == 1:
        return 1
    return mazePath(row-1, col) + mazePath(row, col-1)

# print(mazePath(4,4))


def preInPost(n):

    if not n: return 
    print(n)
    preInPost(n-1)
    print(n)
    preInPost(n-1)
    print(n)

# preInPost(3)

def printArr(arr, pointer=0):

    if pointer == len(arr):
        return 
    printArr(arr, pointer+1)
    print(arr[pointer])

arr = [1,2,3,4,5,6,7]
# printArr(arr)

string = "ritesh laxman gupta"

def printString(string, char, pointer=0):
    
    if pointer == len(string):
        return
    if string[pointer] == char:
        printString(string, char, pointer +1)
    else:
        print(string[pointer])
        printString(string, char, pointer+1)

# printString(string, "r")

def printString(string, char, pointer=0, result=""):

    if pointer == len(string):
        return result
    if string[pointer] == char:
        return printString(string, char, pointer+1, result)
    else: 
        result += string[pointer]
        return printString(string, char, pointer+1, result)

string = "ritesh laxman gupta"
char = "a"
# print(printString(string, char))

string = "ab"

# def subset(string, left=0):

#     if len(string) == 1:
#         print(string)
#         return
#     subset(string[left:], left+1)
#     subset(string[left+1:], left+1)

# subset(string)

# def subset(string, index=0, ans=""):

#     if index == len(string):
#         print(ans)
#         return 
#     char = string[index]
#     subset(string, index + 1, ans + char)
#     subset(string, index + 1, ans)

# subset(string)

result = []
def subset(string, index=0, ans=""):

    if index == len(string):
        result.append(ans)
        return
    char = string[index]
    subset(string, index+1, ans+char)
    subset(string, index+1, ans)

string = "abcd"
subset(string)
# print(result)


def permutation(string, ans=""):

    if not string:
        print(ans)
        return
    for i in range(len(string)):
        permutation(string[:i] + string[i+1:], ans + string[i])

# string = "abcd"
# permutation(string)
# print(permutation(string))

# string = "ritesh"
# index = 2
# print(string[:index]+string[index+1:])

def hcf(x, y):

    while y:
        x, y = y, x%y
    return x

def hcf(x, y):

    if not y:
        return x
    return hcf(y, x % y)


# print(hcf(9,3))

def generateBinary(number, string=""):

    if not number:
        print(string)
        return 

    for i in range(2):
        if i == 1:
            if string[-1] == 1:
                continue
            else:
                generateBinary(number-1, string + str(i))
        else:
            generateBinary(number-1, string + str(i))

# def generateBinary(count, ans = ""):

#     if not count:
#         print(ans)
#         return 
    
#     for i in range(2):
#         generateBinary(count-1, ans + str(i))

def generateBinary(count, ans=""):
    if not count:
        print(ans)
        return 
    for i in range(2):
        if i == 1 and ans and ans[-1] == "1":
            continue
        else:
            generateBinary(count-1, ans + str(i))

# generateBinary(3)

# string = ""
# print(string[-1])


# if string: print(True)
# else: print(False)

# string = ""

# def generateBracket(n, open=0, close=0, string=""):

#     if len(string) == 2*n:
#         print(string)
#         return 
#     if open < n: generateBracket(n, open+1, close, string + "(")
#     if close < open: generateBracket(n, open, close+1, string + ")")

# generateBracket(3)

def generateBracket(n, open=0, close=0, string="", result=[]):

    if len(string) == 2*n:
        result.append(string)
        return 
    if open < n: return generateBracket(n, open+1, close, string + "(", result)
    if close < open: return generateBracket(n, open, close+1, string + ")", result)

# print(generateBracket(3))

string = "111222334"
def countAndSay(string):

    left = 0
    result = ""

    for right in range(len(string)):

        if right == len(string)-1:
            if string[left] == string[right]:
                result += string[left] + str(right-left)
            else: 
                result += string[left] + str(right-left)
                result += string[right] + str(1)
        elif string[right] != string[left]:
            result += string[left] + str(right-left)
            left = right

    return result

# print(countAndSay(string))


