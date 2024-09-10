seats = [3,1,5] 
students = [2,7,4]

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
  
def minimumMovies(seats, students):

    sortedSeats = mergeSort(seats)
    sortedStudents = mergeSort(students)

    moves = 0

    for i in range(len(sortedSeats)):
        moves += abs(sortedSeats[i]-sortedStudents[i])

    return moves

# response = minimumMovies(seats, students)
# print(response)

# def numberSmallerThanCurrent(arr):

#     for i in range(len(arr)):
#         count = 0
#         for j in range(len(arr)):
#             if arr[j] < arr[i]:
#                 count += 1
#         arr[i] = count 

#     return arr

def numberSmallerThanCurrent(arr):

    sortedArr = sorted(arr)

    smallerCount = {}

    for i, num in enumerate(sortedArr):
        if num not in smallerCount:
            smallerCount[num] = i
        
    result = [smallerCount[num] for num in arr]

    return result

arr = [8,1,2,2,3]
# print(numberSmallerThanCurrent(arr))

num = 2932
# def minimumSum(num):
    
#     number = list(str(num))
#     mid = len(number)//2

#     num1 = number[:mid]
#     num2 = number[mid:]

#     num1.sort() 
#     num2.sort()

#     num1 = int("".join(num1))
#     num2 = int("".join(num2))

#     return num1 + num2 

# num = 2687
# print(minimumSum(num))

# print(list(str(2687)))

def miniSum(num):

    number = list(str(num))
    number.sort()

    num1 = []
    num2 = []

    num1_boolean = True

    for i in number:
        if num1_boolean:
            num1.append(i)
            num1_boolean = False
        else:
            num2.append(i)
            num1_boolean = True

    num1 = "".join(num1)
    num2 = "".join(num2)

    return int(num1) + int(num2)

num = 2687
result = miniSum(num)
# print(result)

def miniGame(number):

    number.sort()
    arr = []

    while number:
        alice = number.pop(0)
        bob = number.pop(0)
        arr.append(bob)
        arr.append(alice)

    return arr


num = [5,4,3,2]
# print(miniGame(num))

nums = [7,8,3,4,15,13,4,1]

def miniAverage(nums):
    
    nums.sort()
    
    mini = (nums.pop(0) + nums.pop())/2

    while nums:
        smallest = nums.pop(0)
        largest = nums.pop()
        avg = (smallest + largest)/2
        mini = min(mini, avg)

    return mini

result = miniAverage(nums)
# print(result)

names = ["Mary","John","Emma"]
heights = [180,165,170]

def sortPeople(names, heights):

    peopleHeight = {}
    for i in range(len(names)):
        peopleHeight[heights[i]] = names[i]

    sortedPeople = []
    heights.sort()

    for i in heights[::-1]:
        sortedPeople.append(peopleHeight[i])

    return sortedPeople


# print(sortPeople(names, heights))
# def sortPeople(names, heights):

#     sortedHeight = sorted(heights)

# def quickSort(arr):

#     if len(arr) > 1:

#         pivot = arr[len(arr)//2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]

#         return quickSort(left) + middle + quickSort(right)
    
#     return arr

# print(quickSort([9,8,7,6,5,4,3,2,1]))

s = "is2 sentence4 This1 a3"

def sortingSentence(s):

    arr = s.split()

    char_index_map = {}
    numArr = []

    for i in arr:
        char_index_map[i[-1]] = i[:len(i)-1]
        numArr.append(i[-1])

    numArr.sort()
    result = ""
    for i in numArr:
        result += char_index_map[i] + " "

    return result.strip()

result = sortingSentence(s)
# print(result)

nums = [3,4,5,2]

def maximumProduct(nums):

    nums.sort()

    num1 = nums[-1]
    num2 = nums[-2]

    return (num1-1)*(num2-1)

nums = [3,7]
# print(maximumProduct(nums))

nums = [4,2,5,9,7,4,8]

def productDifference(nums):

    nums.sort()

    num1 = nums[-1] * nums[-2]
    num2 = nums[0] * nums[1]

    return num1 - num2


# print(productDifference(nums))

heights = [1,1,4,2,1,3]

def insertionSort(heights):

    for i in range(1, len(heights)):    
        key = heights[i]
        j = i-1

        while j <= 0 and key < heights[j]:
            heights[j+1] = heights[j]
            j -= 1
        heights[j+1] = key

    return heights

# print(insertionSort(heights))

nums = [1,1,2,2,2,3]

def sortByFrequency(nums):

    char_index_map = {}
    frequency_map = {}

    for i in nums:
        if i in char_index_map:
            char_index_map[i] += 1
        else:
            char_index_map[i] = 1

    frequency = list[char_index_map.values()]
    value = list[char_index_map.keys()]
    result = []

    

    for i in nums:
        count = char_index_map[i]
        result += [i] * count

    # frequency = list(char_index_map.values())
    # value = list(char_index_map.keys())

    # frequency_map = {}
    # for i in range(len(frequency)):
    #     frequency_map[frequency[i]] = value[i]

    # frequency.sort()
    # result = []
    # for i in frequency:
    #     result += [frequency_map[i]] * i

    return result

result = sortByFrequency(nums)
# print(result)


    
arr = [6,2,6,5,1,2]

def minimumSum(arr):

    arr.sort()

    num1 = arr[0]
    num2 = arr[-2]
    print(arr, num1, num2)
    return num1 + num2

print(minimumSum(arr))