arr = [6,11,7,4,8,9,11]

def reverseArr(arr):

    left = 0
    right = len(arr) - 1

    while (left < right):

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# print(reverseArr(arr))

def createFibonacci(k):

    arr = [0, 1]

    for i in range(1, k-1):
        arr.append(arr[i-1]+arr[i])

    return arr

print(createFibonacci(7))

print(arr)
def rotateBy1(arr):

    firstElement = arr[0]

    for i in range(1, len(arr)):
        arr[i-1] = arr[i]

    arr[len(arr) - 1] = firstElement

    return arr

print(rotateBy1(arr))
        

            