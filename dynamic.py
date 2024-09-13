def fibo(n):
    dp = [0] * (n+1)
    return fib(n, dp)

def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != 0:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

# print(fibo(50))

arr = [1,2,3,4,50,6]

def minCost(arr, pointer, dp):

    if pointer == 0 or pointer == 1:
        return arr[pointer]
    
    if dp[pointer] != -1:
        return dp[pointer]
    dp[pointer] = arr[pointer] + min(minCost(arr, pointer-1, dp), minCost(arr, pointer-2, dp))
    return dp[pointer]

def result(arr):

    dp = [-1] * (len(arr)+1)
    return minCost(arr, len(arr)-1, dp)

# print(result(arr))

def tribonacci(n,dp):

    if n <= 1:
        return n
    if n == 2:
        return 1
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = tribonacci(n-1, dp) + tribonacci(n-2, dp) + tribonacci(n-3, dp)
    return dp[n]

def result(n):
    dp = [-1] * (n+1)
    return tribonacci(n, dp)

# print(result(50))

# print(tribonacci(50))


# def minCost(arr, pointer=None, sum = 0):


# def minCost(arr, pointer=None, sum=0):

#     if pointer is None:
#         pointer = len(arr)-1
#     if pointer == 0:
#         sum += min(arr[pointer], arr[pointer-1])
#         return sum
#     if pointer-2 < 0:
#         sum += min(arr[pointer], arr[pointer-1])
#         return sum
#     sum += min(arr[pointer], arr[pointer-1])
#     return minCost(arr, pointer-2, sum)

# print(minCost(arr))
nums = [2,7,9,3,1]

def robHouse(nums, house):

    if house == len(nums)-1 or house == len(nums)-2:
        return nums[house]
    
    return nums[house] + robHouse(nums, house+2)

def result(nums):

    if len(nums) == 1:
        return nums[0]
    return max(robHouse(nums, 0), robHouse(nums, 1))

nums = [1,2,3,1]
nums = [2, 1]
# print(result(nums))

nums = [2,1]

def robHouse(nums, house, dp):

    if house >= len(nums):
        return 0
    if house == len(nums)-1 or house == len(nums)-2:
        return nums[house]

    if dp[house] != -1:
        return dp[house]
    dp[house] = nums[house] + max(robHouse(nums, house + 2, dp), robHouse(nums, house + 3, dp))
    return dp[house]

def result(nums):

    if len(nums) == 1:
        return nums[0]
    dp = [-1] * len(nums)
    return max(robHouse(nums, 0, dp), robHouse(nums, 1, dp))

# print(result(nums))

def subsequences(string, ans=""):

    if not string: return print(ans)

    for i in range(len(string)):
        char = string[i]
        subsequences(string[:i] + string[i+1:], ans + char)

string = "abc"
# subsequences(string)

def subset(string, pointer=0, ans=""):

    if pointer == len(string):
        return print(ans)
    
    subset(string, pointer + 1, ans + string[pointer])
    subset(string, pointer + 1, ans)

string = 'abcd'

def uniquePath(rows, cols, dp):

    if rows == 0:
        return 1
    if cols == 0:
        return 1
    
    if dp[rows][cols] != -1: return dp[rows][cols]
    dp[rows][cols] = uniquePath(rows-1, cols, dp) + uniquePath(rows, cols-1, dp)
    return dp[rows][cols]

rows = 3
cols = 3
def result(rows, cols):

    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    return uniquePath(rows-1, cols-1, dp)

# print(result(rows, cols))


# obstacleGrid = [[0,1],[0,0]]
# print(obstacleGrid[-1][-1])
# obstacleGrid = [[0,0],[0,1]]

def result2(row, col, obstacle, dp):

    if row == 0 or col == 0: return 1

    if obstacle[row-1][col]:
        return result2(row, col-1, obstacle, dp)
    if obstacle[row][col-1]:
        return result2(row-1, col, obstacle, dp)
    return result2(row-1, col, obstacle, dp) + result2(row, col-1, obstacle, dp)

def uniquePath2(obstacleGrid):

    row = len(obstacleGrid)
    col = len(obstacleGrid[0])

    dp = [[-1 for _ in range(col)] for _ in range(row)]

    return result2(row-1, col-1, obstacleGrid, dp)

# print(uniquePath2(obstacleGrid))

obstacleGrid = [[0,0,0],[0,1,0],[0,0,2]]

def path(rows, cols, obstacle, dp, rowpos=0, colpos=0):

    if rowpos == rows-1 or colpos == cols-1: return 1

    if obstacle[rowpos+1][colpos]:
        if dp[rowpos][colpos+1] != -1: return dp[rowpos][colpos+1]
        dp[rowpos][colpos+1] = path(rows, cols, obstacle, dp, rowpos, colpos+1)
        return dp[rowpos][colpos+1]
    elif obstacle[rowpos][colpos+1]:
        if dp[rowpos+1][colpos] != -1: return dp[rowpos+1][colpos]
        dp[rowpos+1][colpos] = path(rows, cols, obstacle, dp, rowpos+1, colpos)
        return dp[rowpos+1][colpos]
    return path(rows, cols, obstacle, dp, rowpos+1, colpos) + path(rows, cols, obstacle, dp, rowpos, colpos+1)

def uniquePath(obstacleGrid):

    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    if obstacleGrid[-1][-1] or obstacleGrid[0][0] or (obstacleGrid[0][1] and obstacleGrid[1][0]):
        return 0
    
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]

    return path(rows, cols, obstacleGrid, dp)

# print(uniquePath(obstacleGrid))

import math

def perfectSquare(num):
    
    squarert = math.ceil(math.sqrt(num))
    return squarert * squarert == num

def numSquares(num):

    if perfectSquare(num): return 1
    mini = num
    for i in range(1, math.floor(num/2)):
        count = numSquares(i) + numSquares(num-i)
        mini = min(mini, count)

    return mini

num = 12
print(numSquares(num)) 