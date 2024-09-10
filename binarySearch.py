def binarySearch(arr, target):

    left = 0
    right = len(arr)-1
    arr.sort()

    while left <= right:
        mid = (left + right)//2
        print(mid)

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [1,2]
arr = [1,2,3,4,5,6,7]
# print(binarySearch(arr, 0))
def findNegative(arr):

    arr.sort()
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == 0:
            break
        elif arr[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    while mid > 0 and arr[mid-1] >= 0:
        mid -= 1

    return mid

arr = [1,2,3,4,-2,-3,-4,-5]
arr = [1,2,3,4,5]
# print(findNegative(arr))
        
def findNegative(arr):

    arr.sort()
    right = 0
    print(arr)
    while arr[right+1] < 0:
        right += 1
    print(right)
    return right + 1

# print(findNegative(arr))

# def binarySearch(arr):

#     left = 0
#     right = len(arr)-1

#     while left <= right:

#         mid = (left + right)//2
#         if arr[mid] == 0:
#             return mid
#         elif arr[mid] > 0:
#             left = mid + 1
#         else:
#             right = mid - 1

#     while mid < len(arr)-1 and arr[mid + 1] >= 0:
#         mid += 1

#     print(mid)
#     return len(arr) - mid - 1 

def pointerSearch(arr):

    arr.sort()
    for right in range(len(arr)):
        if arr[right] >= 0:
            break

    print(arr, right)
    return right

def pointerSearch(arr):

    right = 0

    while right < len(arr):
        if arr[right] < 0:
            break
        right += 1

    # print(arr, right)
    return len(arr)-right

def countNegative(grid):
    
    count = 0 
    for row in grid:
        count += pointerSearch(row)

    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# print(countNegative(grid))

def countNegative(grid):

    row = len(grid)
    col = len(grid[0])

    i = 0
    j = col-1
    count = 0

    while i < row and  j >= 0:

        if grid[i][j] < 0:
            count += col - i
            j -= 1
        
        else:
            i += 1

    return count


# def countNegatives(grid):
#     row = len(grid)  # Number of rows
#     col = len(grid[0])  # Number of columns
#     ans = 0
#     i = row - 1
#     j = 0
#     while i >= 0 and j < col:
#         if grid[i][j] < 0:
#             ans += col - j
#             i -= 1
#         else:
#             j += 1
#     return ans

# def countNegatives(grid):

#     row = len(grid)
#     col = len(grid[0])

#     i = row - 1
#     j = 0
#     count = 0
#     while i >= 0 and j < col:

#         if grid[i][j] < 0:
#             count += col - j
#             i -= 1

#         else:
#             j += 1

#     return count

# grid = [[5,1,0],[-5,-5,-5]]
# result = countNegatives(grid)
# print(result)

# def maximumDifference(arr):

#     negative = 0

#     for i in range(len(arr)):


def binarySearch(arr, target):

    left = 0
    right = len(arr)-1

    while left <= right:

        mid = (left + right)//2

        print(arr[mid])
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(arr[mid])
    return -1

arr = [1,2,3,4,5,6,7]
nums = [-3,-2,2,2,3]
# print(binarySearch(nums,0))
# print(binarySearch(nums, -1))
# print(binarySearch(nums, -1))
# print(binarySearch(nums, -1))
# print(binarySearch(nums, ))

# def reverseArr(arr,left, right):

#     if left > right:
#         return ""
#     if left == right:
#         return arr[left]
#     return arr[right] + reverseArr(arr, left + 1, right - 1) + arr[left]

# string = "ritesh"
# print(reverseArr(string, 0, len(string)-1)) 

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    

class singlyLinkedList:

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
            result.append(currentNode.value)
            currentNode = currentNode.next
        print("->".join(map(str, result)))

    # def reverseList()
    
def reverseList(head, prevNode = None):

    if head.next is None:
        head.next = prevNode
        return head
    
    nextNode = head.next
    head.next = prevNode
    
    return reverseList(nextNode, head)

    

data = singlyLinkedList()

data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
data.append(6)

# data.display()

data.head = reverseList(data.head)
# data.display()


arr = [7,8,9,1,2,3,4]

def searchRotatedArray(arr, target):

    left = 0
    right = len(arr)-1

    while left <= right:

        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[left] <= arr[mid]:
            if arr[left] <= target and arr[mid] > target:
                right = mid -1 
            else:
                left = mid + 1
        else:
            if arr[mid] < target and arr[right] >= target:
                left = mid - 1
            else:
                right = mid + 1
    return -1

def searchSortedArray(arr, target):

    left = 0
    right = len(arr)-1

    while right >= left:

        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] <= arr[mid]:
            if arr[left] <= target and arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        else:
            if arr[right] >= target and arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# arr = [4,5,6,6,7,0,1,2,4,4]
# arr = [0,1,2,4,4,4,5,6,6,7]
arr = [1,0,1,1,1]
target = 0
# print(searchSortedArray(arr, target))
# print(searchRotatedArray(arr, target))

arr = [3,4,5,1,2]

def minArr(arr):

    left = 0
    right = len(arr)-1
    mini = 2**31

    while right >= left:

        mid = (left+right)//2

        if arr[left] > arr[mid]:
            mini = min(mini, arr[left])
            left = mid
        else:
            mini = min(mini, arr[mid+1])
            right = mid

    return mini

import sys

def minArr(arr):

    left = 0
    right = len(arr)-1
    mini = sys.maxsize
    while right >= left:

        mid = (left+right)//2

        if arr[left] <= arr[right]:
            mini = min(mini, arr[left])
            break
        elif arr[left] >= arr[mid]:
            mini = min(mini, arr[mid])
            left = mid + 1
        else:
            mini = min(mini, arr[left])
            left = mid + 1
    return mini

def minArr(arr):

    left = 0
    right = len(arr)-1
    mini = arr[0]
    while right >= left:

        mid = (left+right)//2

        if arr[left] <= arr[right]:
            mini = min(mini, arr[left])
            break

        elif arr[left] <= arr[mid]:
            mini = min(mini, arr[left])
            left = mid + 1
    
        else:
            mini = min(mini, arr[mid])
            right = mid - 1

    return mini

def countRotations(arr):

    left = 0
    right = len(arr)-1
    mini = len(arr)-1

    while left <= right:

        mid = (left+right)//2

        if arr[left] <= arr[right]:
            if arr[left] < arr[mini]:
                mini = left 
            break
        elif arr[left] <= arr[mid]:
            if arr[left] < arr[mini]: mini = left
            left = mid + 1
        else:
            if arr[mid] < arr[mini]: mini = mid
            right = mid - 1

    return mini

# def countRotation(arr):

#     left = 0
#     right = len(arr)-1

#     while right >= left:

#         if arr[left] <= arr[right]:
#             return left
#         elif arr[left] > arr[right]:


arr = [4,5,6,7,0,1,2]
arr = [11,13,15,17]
arr = [3,1,2]
# print(minArr(arr))
# print(countRotations(arr))

nums = [1,1,2,3,3,4,4,8,8]
def singleElement(arr):

    left = 1
    right = len(arr)-2

    while right >= left:
        mid = (left+right)//2
        isEven = mid % 2 == 0

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]

        elif (isEven and arr[mid] == arr[mid+1]) or (not isEven and arr[mid] == arr[mid-1]):
            left = mid + 1
        else:
            right = mid - 1
    return -1            

    # for right in range(1, len(arr)-1):

    #     if arr[right-1] != arr[right] and arr[right+1] != arr[right]:
    #         return arr[right]
        
    # return -1

# print(singleElement(nums))
            
nums = [1,2,1,3,5,6,4]
arr = [1,2,3,4,5,6,7,8,5,1]
def findPeak(arr):

    if len(arr) == 1:
        return arr[0]
    
    left = 1
    right = len(arr)-2

    while right >= left:
        
        mid = (left+right)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid - 1
        print(left, right)

    result = max(arr[0], arr[-1])

    return result

nums = [1,2,3,1]
nums = [8,7,6,5,4,3]
# nums = [1,2,3,4,5,6,7,8]
# print(findPeak(nums))

num = 25

def squareRoot(num):

    # if not num:
    #     return 0

    low = 0
    high = num
    ans = 1
    while high >= low:

        mid = (low+high)//2
        result = mid * mid
        if result == num:
            return mid
        elif result < num:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

# print(squareRoot(49))

def cubeRoot(num):

    left = 0
    right = num-1 

    while right >= left:

        mid = (left+right)//2
        result = mid ** 3
        
        if result == num:
            return mid
        elif result < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def nthRoot(order, number):

    left = 0
    right = number

    while right >= left:

        mid = (left+right)//2
        result = mid ** order
        
        if result == number: return mid
        elif result < number: left = mid + 1
        else: right = mid - 1

    return -1

# print(nthRoot(4, 1))
# print(cubeRoot(2, 8))

import math

def countTotal(piles, mid):

    total = 0

    for i in piles:
        total += math.ceil(i/mid)

    return total

def maxElement(piles):

    maxi = piles[0]

    for i in range(1, len(piles)):
        maxi = max(maxi, piles[i])

    return maxi

def kokoEatsBanana(piles, hour):

    left = 1
    right = maxElement(piles)

    while right >= left:

        mid = (left+right)//2
        totalHour = countTotal(piles, mid)
        print(totalHour, mid)
        if totalHour == hour:
            return mid
        elif totalHour > hour:
            left = mid + 1
        else: 
            right = mid - 1

    return left

def totalHour(piles, mid):

    total = 0
    for i in piles:
        total += math.ceil(i/mid)
    return total

def minEatingSpeed(piles, h):

    left = 1
    right = max(piles)

    while right >= left:
        mid = (right+left)//2

        total = totalHour(piles, mid)
        print(total)
        if total == h:
            return mid
        elif total < h:
            right = mid-1
        else:
            left = mid + 1
    return left

# piles = [30,11,23,4,20]
piles = [3,6,7,11]
h = 8
# print(minEatingSpeed(piles, h))

bloomDay = [1,10,3,10,2]
bloomDay = [7,7,7,7,12,7,7]

def flower(bloomDay, mid, k):

    result = 0
    counter = 0
    # print(bloomDay)
    for i in range(len(bloomDay)):
        if bloomDay[i] > mid:
            result += counter//k
            counter = 0
        else:
            counter += 1

    # print(counter)
    result += counter//k

    return result

# print(flower(bloomDay, 12, 3))

def minDays(bloomDay, m, k):

    left = min(bloomDay)
    right = max(bloomDay)
    ans = right
    possible = False

    while right >= left:

        mid = (left+right)//2

        flowerCount = flower(bloomDay, mid, k)
        print(flowerCount, mid)
        if flowerCount >= m:
            ans = min(ans, mid)
            possible = True
            right = mid - 1
        else:
            left = mid + 1

    if not possible:
        return -1
    return ans

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
# print(minDays(bloomDay, m, k))        


arr = [1,2,5,9]

def arrSum(arr, mid):

    total = 0

    for i in arr:
        total += math.ceil(i/mid)

    return total

def smallestDivisor(arr, limit):

    left = 1
    right = max(arr)
    result = right
    while right >= left:

        mid = (left+right)//2

        total = arrSum(arr,mid)

        if total <= limit:
            result = min(mid, result)
            right = mid - 1    
        else:
            left = mid + 1

    return result

# print(smallestDivisor(arr, 6))

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

def flowerCount(bloomDay, mid, k):

    counter = 0
    result = 0
    for flower in bloomDay:
        if flower > mid:
            result += counter//k
            counter = 0
        else:
            counter += 1

    result += counter//k
    return result

def minDays(bloomDay, m, k):

    left = min(bloomDay)
    right = max(bloomDay)
    result = -1
    # possible = False
    while left <= right:
        mid = (left+right)//2

        totalFlower = flowerCount(bloomDay, mid, k)
        if totalFlower >= m:
            # result = min(result, mid)
            result = mid
            # possible = True
            right = mid - 1
        else:
            left = mid + 1

    # if not possible:
    #     return -1
    return result

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2
# print(minDays(bloomDay, m, k)) 

nums = [44,22,33,11,1]
threshold = 5

def totalCount(nums, mid):

    result = 0
    for i in nums:
        result += math.ceil(i/mid)
    return result

def smallestDivisor(nums, threshold):

    left = 1
    right = max(nums)
    result = right

    while right >= left:
        mid = (left+right)//2
        total = totalCount(nums, mid)

        if total <= threshold:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

nums = [1,2,5,9]
threshold = 6
# print(smallestDivisor(nums, threshold))


# def countTotal(weights, days):


def minCapacity(weights, days):

    left = 1
    right = days
    total = sum(weights)
    minimum = total
    
    while right >= left:
        mid = (right+left)//2
        weight = total//mid

        if weight <= minimum:
            minimum = min(minimum, weight)
            right = mid - 1
        else:
            left = mid + 1

    return minimum

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def daysRequired(arr, weight):

    days = 0
    total = 0
    pointer = 0

    while pointer < len(arr):

        total += arr[pointer]

        if total == weight:
            days += 1
            total = 0
            pointer += 1
        elif total > weight:
            days += 1
            total = 0
        else:
            pointer += 1

    # print(total)
    if total:
        days += 1

    return days

def minCapacity(weights, days):
    
    left = max(weights)
    right = sum(weights)
    minCapacity = right
    while right >= left:
        mid = (left+right)//2

        day = daysRequired(weights, mid)

        if day <= days:
            minCapacity = min(minCapacity, mid)
            right = mid - 1
        else:
            left = mid + 1

    return minCapacity

# print(minCapacity(weights, days))




# print(daysRequired(weights, 15))




# def demo(weights, days):

#     total = sum(weights)
#     print(total)
#     result = total/days
    # result = math.ceil(total/days)

    # return result

# print(demo(weights, days))
# print(minCapacity(weights, days))

arr = [2,3,4,7,11]
k = 5

def missingNumber(arr, k):

    left = 0
    right = len(arr)-1

    while right >= left:

        mid = (left+right)//2
        missing = arr[mid] - mid - 1

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    count = arr[right]-k
    return arr[right]+count

def missingK(vec, k):
    low = 0
    high = len(vec)-1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    print(high)
    return k + high + 1

arr = [2]
k = 1

print(missingK(arr, k))

# vec = [4, 7, 9, 10]
# n = 4
# k = 4
# ans = missingK(vec, n, k)
# print("The missing number is:", ans)

# arr = [2,3]
# k = 4

# result = missingNumber(arr, k)
# print(result)



        
        
