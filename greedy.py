def assignCookies(children, cookies):

    children.sort()
    cookies.sort()
    satisfied = 0

    i = 0
    j = 0

    while i < len(children) and j < len(cookies):

        if cookies[j] >= children[i]:
            i += 1
            j += 1
            satisfied += 1
        
        else:
            j += 1

    return satisfied


children = [1,5,3,3,4]
cookies = [4,2,1,2,1,3]
# print(assignCookies(children, cookies))

def lemonadeChange(customers):

    five = 0
    ten = 0
    twenty = 0

    for i in customers:
        if i == 5:
            five += 1
        elif i == 10:
            if five:
                ten += 1
                five -= 1
            else:
                return False
        else:
            if ten and five:
                twenty += 1
                ten -= 1
                five -= 1
            elif five >= 3:
                twenty += 1
                five -= 3
                
            else:
                return False
    return True

customers = [5,5,10,10,20]
# print(lemonadeChange(customers))

schedule = [4,3,7,1,2]
def averageWaitingTime(schedule):

    schedule.sort()
    time = 0
    waitingTime = 0
    time = 0

    for i in range(1, len(schedule)):
        time += schedule[i-1]
        waitingTime += time

    return waitingTime//len(schedule)

result = averageWaitingTime(schedule)
# print(result)

def jumpingGame(number):

    maxIndex = 0

    for i in range(len(number)):
        maxIndex = max(maxIndex, number[i] + i)
        print(maxIndex, i)
        if i == maxIndex:
            return False
    return True

number = [1,2,4,1,1,0,2,5]
# print(jumpingGame(number))

start = [0,3,1,5,5,8]
end = [5,4,2,9,7,9]

def insertionSort(arr, arr1, arr2):

    for i in range(1, len(arr)):
        key = arr[i]
        key1 = arr1[i]
        key2 = arr2[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr1[j+1] = arr1[j]
            arr2[j+1] = arr2[j]
            j -= 1
        arr[j+1] = key
        arr1[j+1] = key1
        arr2[j+1] = key2

    return arr, arr1, arr2

def jobSequencing(start, end):

    char_index_map = {}
    for i in range(len(start)):
        char_index_map[start[i]] = end[i]

    print(char_index_map)

    start.sort()
    end = []

    for i in start:
        end.append(char_index_map[i])
    print(start)
    print(end)

    hours = []

    for key, value in char_index_map.items():
        time = value-key
        hours.append(time)

# print(hours)

#     hours = []

#     for i in range(len(start)):
#         hours.append(end[i]-start[i])

#     hours, start, end = insertionSort(hours, start, end)
#     print(hours, start, end)

# jobSequencing(start,end)

arr = [1,2,3,4,5,6,7]
print("".join(map(str, arr)))