arr = [10,5,2,7,1,9]

def twoSum(arr, k):

    left = 0
    right = 0
    size = len(arr)
    sum = 0

    while right < size and left < size:
        sum += arr[right]

        if sum == k:
            return [left, right]
        elif sum < k:
            right += 1
        else:
            sum -= arr[left]
            left += 1

nums = [2,3,4]
target = 6
# print(twoSum(nums, target))


def longestSubArray(arr, k):

    left = 0
    right = 0
    maximum = 0
    sum = 0

    while right < len(arr) and left < len(arr):

        sum += arr[right]

        if sum == k:
            if right - left + 1 > maximum:
                maximum = right - left + 1
            sum -= arr[left]
            left += 1
            right += 1
        elif sum < k:
             right += 1
        else:
            sum -= arr[left]
            left += 1

    return maximum
k = 15
# print(longestSubArray(arr, 15))

# def selectionSort(arr):

#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# def sortColor(arr):

#     char_index_map = {}

#     for i in arr:
#         if i in char_index_map:
#             char_index_map[i] += 1
#             continue
#         char_index_map[i] = 1

#     print(char_index_map)

#     for i in range(3):

def sortColor(arr):

    count0 = 0
    count1 = 0
    count2 = 0

    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    k = 0
    print(count0, count1, count2)
    while count0:
        arr[k] = 0
        k += 1
        count0 -= 1
    print(k)
    while count1:
        arr[k] = 1
        k += 1
        count1 -= 1
    print(k)
    while count2:
        arr[k] = 2
        k += 1
        count2 -= 1

    return arr

def sortColor(arr):

    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

def twoSum(arr, target):

    mapping = {}
    for i, num in enumerate(arr):
        number = target - num
        if number in mapping:
            return [mapping[number], i]
        mapping[num] = i
    return -1

def twoSum(arr, target):

    arr.sort()
    left = 0
    right = len(arr)-1

    while right > left:

        sum = arr[right] + arr[left]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return arr

arr = [2,0,2,1,1,0]
arr = [2,0,1]
# print(sortColor(arr))
arr = [2,7,11,15]
target = 9
# print(twoSum(arr, target))
            

def majorityElement(arr):

    mapping = {}

    for i in arr:
        if i in mapping:
            mapping[i] += 1
            continue
        mapping[i] = 1

    maximum = None
    for i in mapping:
        if maximum is None:
            maximum = i
        else:
            if mapping[i] > mapping[maximum]:
                maximum = i
    
    return maximum

arr = [3,2,3]
# print(majorityElement(arr))

def maxSubArr(arr, k):

    left = 0
    right = 0
    sum = 0
    maximum = 0
    while right < len(arr):
        sum += arr[right]
        print(sum)

        if sum == k:
            maximum = max(maximum, right-left+1)
            sum -= arr[left]
            left += 1
            right += 1

        elif sum < k:
            right += 1
        else:
            sum -= arr[left]
            left += 1

    return maximum


def maxSubArr(arr):

    left = 0
    right = 0
    maximum = arr[0]
    maxArr = []
    sum = 0

    while right < len(arr):
        if sum < 0:
            sum = 0
            left += 1
        sum += arr[right]
        if sum > maximum:
            maximum = sum
            maxArr = arr[left:right+1]
        right += 1

    print(maxArr)
    return maximum


arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [1]
# print(maxSubArr(arr))
                
def maxSubArr(arr):

    smallest = min(arr[0], arr[1])
    secondSmallest = max(arr[0], arr[1])
    maxSum = smallest + secondSmallest
    for right in range(len(arr)-1):

        sum = smallest + secondSmallest

        if sum > maxSum:
            maxSum = sum

        if arr[right+1] < secondSmallest:
            if arr[right+1] < smallest:
                secondSmallest = smallest
                smallest = arr[right+1]
            else:
                secondSmallest = arr[right+1]

    print(maxSum)
    print(smallest, secondSmallest)

    if arr[0] == smallest: smallest



arr = [5,4,-1,7,8]

# maxSubArr(arr)

# def maxProfit(prices):
    
#     mini = prices[0]
#     maxProfit = 0
#     for right in range(1, len(prices)):
#         profit = prices[right]-mini
#         mini = min(mini, right)
#         maxProfit = max(maxProfit, profit)

#     return maxProfit

# prices = [1]
# print(maxProfit(prices))

def rearrange(arr):

    positive = []
    negative = []

    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    for j in range(len(positive)):
        arr[j*2] = positive[j]

    for k in range(len(negative)):
        arr[2*k + 1] = negative[k]

    return arr

arr = [3,1,-2,-5,2,-4]
# print(rearrange(arr))

# def nextPermutation(arr):

arr = [16,17,4,3,5,2]

def leaderArr(arr):

    stack = []
    result = [None] * len(arr)

    for right in range(len(arr)):

        if not stack:
            stack.append(right)

        while stack and arr[stack[-1]] < arr[right]:
            index = stack.pop(-1)
            result[index] = arr[right]

        stack.append(right)

    print(stack)
    
    # for i in stack:
        

    # output = []
    # for i, num in enumerate(result):
    #     if num is None:
    #         output.append(arr[i])            

    # return output

# arr = [1,2]

def leaderArr(arr):

    stack = []

    for i in arr:

        # if not stack:
        #     stack.append(i)
        while stack and stack[-1] < i:
            stack.pop()

        stack.append(i)

    # print(stack)

    return stack

arr = [6, 5, 4, 3, 2, 1]
# print(leaderArr(arr))

matrix = [[1,1,1],[1,0,1],[1,1,1]]

# def setZeros(matrix):

def longestConsecutive(arr):

    mapping = {}
    longest = 1

    for i, num in enumerate(arr):
        if num in mapping:
            mapping[num] += 1
            continue
        mapping[num] = 1

    for i in arr:
        count = 1
        number = i
        while number+1 in mapping:
            count += 1
            number += 1
        longest = max(count, longest)

    return longest

def longestConsecutive(arr):

    if not arr:
        return 0
    arr.sort()
    # print(arr)
    right = 0
    longest = 1
    count = 1
    while right < len(arr)-1:

        if arr[right] == arr[right+1]:
            right += 1

        elif arr[right]+1 == arr[right+1]:
            count += 1
            right += 1

        else:
            longest = max(count, longest)
            count = 1
            right += 1

    longest = max(longest, count)

    return longest
        
arr = [102,4,100,1,101,3,2,1,1]
arr = [0,3,7,2,5,8,4,6,0,1]
arr = []
result = longestConsecutive(arr)
# print(result)


def matrixZero(matrix):

    row = len(matrix)
    col = len(matrix[0])

    rowArr = [0]*row
    colArr = [0]*col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                rowArr[i] = 1
                colArr[j] = 1

    print(rowArr, colArr)

    for i in range(row):
        for j in range(col):
            if rowArr[i] == 1 or colArr[j] == 1:
                matrix[i][j] = 0

    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]

def matrixZero(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = None
                matrix[i][0] = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[0][j] is None or matrix[i][0] is None:
                matrix[i][j] = 0

    return matrix

# print(matrixZero(matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def rotateMatrix(matrix):

    size = len(matrix)

    for row in range(size):
        for col in range(row, size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
        # left = 0
        # right = size-1

        # while right > left:
        #     row[left], row[right] = row[right], row[left]
        #     left += 1
        #     right -= 1

    print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# result = rotateMatrix(matrix)
# print(result)

def countSubArray(arr, target):

    left = 0
    right = 0
    sum = 0
    count = 0

    while right < len(arr) and left < len(arr):
        sum += arr[right]
        if sum == target:
            count += 1
            sum -= arr[left]
            left += 1
            right += 1
        elif sum < target:
            right += 1
        else:
            sum -= arr[left]
            left += 1

    return count

arr = [1,2,3]
k = 3
# print(countSubArray(arr, k))


def spiralMatrix(matrix):  

    result = []
    while matrix:
        
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix = [[7],[9],[6]]
# print(spiralMatrix(matrix))
                
def pascalTriangle(count):

    row1 = [1]
    row2 = [1,1]
    
    result = []
    result.append(row1)
    result.append(row2)

    # print(result)

    for i in range(count-2):
        temp = result[-1]
        ans = [1]
        left = 0
        right = 1

        while right < len(temp):
            sum = temp[left]+temp[right]
            ans.append(sum)
            left += 1
            right += 1

        ans.append(1)

        result.append(ans)

    return result

# print(pascalTriangle(3))
# pascalTriangle(1)

def printNumber(row, col):

    result = 1

    diff = row - col

    for i in range(diff):
        result *= (row - i)/(i+1)

    return int(result)

# print(printNumber(2,1))


# def removeOutermost(string):

    # stack = []
    # result = ""

    # for i in string:

    #     if i == "(":
    #         stack.append(i)
    #     elif i == ")":
    #         if stack:


string = "(())(())"
def validParenthesis(string):

    stack = []

    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# print(validParenthesis(string))

def lowerBound(arr, target):

    ans = len(arr)
    left = 0
    right = len(arr)-1

    while right >= left:

        mid = (right+left)//2

        if arr[mid] == target:
            ans = min(ans, mid)
            if arr[mid-1] == target:
                ans = min(ans, mid-1)
            return ans
        elif arr[mid] > target:
            ans = min(ans, mid)
            right = mid-1
        else:
            left = mid+1
    
    return ans

arr = [1,2,3,4,4,5,6,9]
target = 7
# print(lowerBound(arr, target))


def floor(arr, target):

    ans = -1
    left = 0
    right = len(arr)-1

    while right >= left:

        mid = (left+right)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            ans = max(ans, mid)
            left = mid+1
        else:
            right = mid-1

    return ans

arr = [1,2,8,10,11,12,19]
# print(floor(arr, 5))


def upperBound(arr, target):

    arr.sort()
    lowerBound = -1
    higherBound = len(arr)
    left = 0
    right = len(arr)-1
    
    while right >= left:

        mid = (left+right)//2

        if arr[mid] == target:
            return mid, mid
        elif arr[mid] < target:
            lowerBound = max(lowerBound, mid)
            left = mid + 1
        else:
            higherBound = min(higherBound, mid)
            right = mid - 1

    lower = 0
    higher = 0
    if lowerBound != -1:
        lower = arr[lowerBound]
    else:
        lower = lowerBound
    if higherBound == len(arr):
        higher = -1
    else: 
        higher = arr[higherBound]

    return lower, higher

arr = [5, 6, 8, 9, 6, 5, 5, 6]
arr = [5, 6, 8, 8, 6, 5, 5, 6]
arr = [36, 82, 88, 56, 21, 17, 73, 86]
target = 17
# print(upperBound(arr, target))


def insertIndex(arr, target):

    lowerBound = -1
    left = 0
    right = len(arr)-1

    while right >= left:

        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lowerBound = max(lowerBound, mid)
            left = mid+1
        else:
            right = mid-1 

    return lowerBound+1

arr = [1,3,5,6]
target = 8
# print(insertIndex(arr, target))
        
nums = [5,7,7,8,8,10]
target = 6

def searchRange(nums, target):
    
    left = 0
    right = len(nums)-1

    while left <= right:

        mid = (left+right)//2

        if nums[mid] == target:
            if mid > 0 and mid < len(nums)-1:
                if nums[mid-1] == target and nums[mid+1] == target:
                    return mid-1, mid+1
                elif nums[mid-1] == target:
                    return mid-1, mid
                elif nums[mid+1] == target:
                    return mid, mid+1
            return mid, mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1, -1

# def firstRange(nums, target):

#     lowerBound = -1
#     upperBound = len(nums)

#     left = 0
#     right = len(nums)-1

    # while right >= left:

    #     mid = (left+right)//2

    #     if nums[mid] == target:
    #         lowerBound
# nums = [1]
# target = 1
# nums = [3,3,3]
# target = 3
# print(searchRange(nums, target))

def lowerBound(arr, target):

    lower = -1
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lower = max(lower, mid)
            left = mid+1
        else:
            right = mid-1

    return lower

def upperBound(arr, target):

    upper = len(arr)
    left = 0
    right = len(arr)-1

    while right >= left:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            upper = min(upper, mid)
            right = mid-1
        else:
            left = mid+1

    if upper == len(arr): return -1
    return upper


# print(lowerBound(nums, target))
# print(upperBound(nums, target))

def firstOccurence(arr, target):

    first = -1
    left = 0
    right = len(arr)-1

    while right >= left:
        mid = (left+right)//2

        if arr[mid] == target:
            first = mid
            right = mid-1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid-1

    return first

def lastOccurence(arr, target):

    last = -1
    
    left, right = 0, len(arr)-1

    while right >= left:

        mid = (left+right)//2

        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1

    return last

nums = [5,7,7,8,8,10]
target = 8
# print(firstOccurence(nums, target))
# print(lastOccurence(nums, target))

def StartEnd(arr, target):

    first = firstOccurence(arr, target)
    last = lastOccurence(arr, target)

    return first, last
# print(StartEnd(nums,target))

nums = [1, 1, 2, 2, 2, 2, 3]
target = 2

def count(nums, target):

    left = 0
    right = len(nums)-1

    while left <= right:

        if nums[left] == target and nums[right] == target:
            return right - left + 1
        if nums[left] != target:
            left += 1
        if nums[right] != target:
            right -= 1

    return 0

print(count(nums, target))


        
    









