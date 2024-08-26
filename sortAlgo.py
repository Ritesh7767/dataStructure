def selectionSort(arr):

    for i in range(len(arr)):
        max = i
        for j in range(i+1, len(arr)):
            if arr[max] > arr[j]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]
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

def quickSort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# def quickSort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr)//2
#     pivot = arr[mid]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quickSort(left) + middle + quickSort(right)

arr = [9,8,7,6,5,4,3,2,1]
print("Bubble sort", bubbleSort(arr))
print("selection sort", selectionSort(arr))
print("mergeSort", mergeSort(arr))
print("insertion sort", insertionSort(arr))
print("Quick sort", quickSort(arr))



