arr = [10,16,8,12,15,6,3,9,5]
name = "rit"

def stringSubsequences(string, index = 0, subString = ""):

    if index == len(string):
        if len(string) != 0:
            return print(subString)

    stringSubsequences(string, index + 1, subString + string[index])
    stringSubsequences(string, index + 1, subString)

# stringSubsequences("rit")
# print(stringSubsequences("ritesh"))

def subsequences(arr, index=0, subArr = []):

    if index == len(arr):
        if len(arr) != 0:
            print(subArr)
        return
    
    subsequences(arr, index + 1, subArr + [arr[index]])
    subsequences(arr, index + 1, subArr)
# arr = [1,2,3]
# subsequences(arr)

# arr = [[1,2,3],[1,2],[1]]

# arr = []
# print(arr + [1,2,3])


# print(arr)

# def subString(string):

#     for i in range(len(string)):
#         for j in range(i, len(string)+1):
#             print(string[i:j])

# subString(name)

# def quickSort(arr, left, right):

#     pivot = arr[left]
#     left += 1

#     while left <= right:

#         while arr[left] <= pivot:
#             left += 1
#         while arr[right] > pivot:
#             right -= 1

#         arr[left], arr[right] = arr[right], arr[left]
    
#     arr[0], arr[right] = arr[right], pivot
#     return arr


# def quickSort(arr):

#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr)//2]
#         left = [x for x in arr if x <= pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quickSort(left) + middle + quickSort(right)

# print(quickSort(arr))

# def SubsetSum(arr, index = 0, subarr = []):

#     if index == len(arr):
#         if len(arr) != 0:
#             print(subarr)
#             sum = 0
#             for i in subarr:
#                 sum += i
#             return print(sum)

#     SubsetSum(arr, index + 1, subarr + [arr[index]])
#     SubsetSum(arr, index + 1, subarr)

def SubsetSum(arr, index = 0, subarr = [], sum = 0, sumArr = []):

    if index == len(arr):
        if len(arr) != 0:
            print(subarr)
            sumArr.append(sum)
            return sumArr

    SubsetSum(arr, index + 1, subarr + [arr[index]], sum + arr[index], sumArr)
    SubsetSum(arr, index + 1, subarr, sum, sumArr)

arr = [1,2,3]
sumArr = []
SubsetSum(arr, sumArr=sumArr)
print(sumArr)

