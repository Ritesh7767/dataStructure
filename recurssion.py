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
print(mergeSort(arr))
# mergeSort(arr)
# print(arr)
# print(mergeSort(arr))
# mergeSort(arr)
# print(arr)

