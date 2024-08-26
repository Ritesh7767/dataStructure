def selectionSort(arr):

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                print(arr)

    return arr

arr = [1,4,45,6,10,8]

def insertionSort(arr):

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

# def bubbleSort(arr)

print(insertionSort(arr))



# bubble sort
# arr = [5,4,3,2,1]

# for i in range(len(arr) - 1):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]

# print(arr)


# def bubbleSort():

# arr = [1,8,6,12,5,4,8,9,13]
# arr = [1,8,6,2,5,4,8,3,7]

# def minArr(arr):

#     left = 0
#     right = len(arr) - 1
#     maxArr = 0

#     while right > left:

#         height = min(arr[left], arr[right])
#         width = abs(right - left)

#         area = height * width
        
#         maxArr = max(area, maxArr)

#         if arr[left] < arr[right]:
#             left += 1
#         else:
#             right -= 1

#     return maxArr

# print(minArr(arr))

# arr1 = [1,2,2,3,4,5]
# arr2 = [4,4,3,2,1,1]

# def commonElement(arr1, arr2):

#     left = 0
#     right = len(arr1) - 1
#     count = 0

#     while left < right:

#         if arr1[left] == arr2[right]:
#             count += 1
#             left += 1
#             right -= 1

#         elif arr1[left] < arr2[right]:
#             right -= 1
#         else:
#             left += 1

#     return count

# print(commonElement(arr1, arr2))














