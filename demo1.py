arr = [4,2,0,5,2,6,2,3]

def tappingRain(arr):

    leftMax = arr[0]
    rightMax = arr[len(arr) - 1]
    water = 0
    maxIndex = 0

    for i in range(len(arr) - 1):
        if arr[maxIndex] < arr[i]:
            maxIndex = i

    for j in range(maxIndex):
        if leftMax < arr[j]:
            leftMax = arr[j]
            continue
        water += leftMax - arr[j]

    for k in range(len(arr) - 2, maxIndex, -1):
        if rightMax < arr[k]:
            rightMax = arr[k]
            continue
        water += rightMax - arr[k]

    return water

# print(tappingRain(arr))

arr = [1,4,45,6,10,8]

def insertionSort(arr):
    
    for i in range(len(arr) - 1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
            
    return arr

print(insertionSort(arr))








    # for i in range(len(arr)):
    #     result.append(arr[i])


# for i in range(len(arr) - 2):
#     firstBreak = False
#     for j in range(i+1, len(arr) - 1):
#         secondBrak = False
#         for k in range(j+1, len(arr)):
#             if arr[i] + arr[j] + arr[k] == 13:
#                 print(arr[i], arr[j], arr[k])
#                 firstBreak, secondBrak = True, True
#                 break
#         if secondBrak:
#             break
#     if firstBreak:
#         break


# print(range(5, 1))

# for i in range(5,1, -1):
#     print(i)

    

# def tappingRain(arr):

#     leftMax = arr[0]
#     rightMax = arr[len(arr) - 1]
#     water = 0
#     maximum = 0

#     for i in range(len(arr)):
        
    

#     for pointer in range(1, len(arr)):

#         if leftMax < arr[pointer]:
#             leftMax = arr[pointer]
#             continue
#         water += leftMax - arr[pointer]
#         print(water)

#     return water

# print(tappingRain(arr))





# def tappingRain(arr):

#     leftMax = [0]
#     rightMax = []
#     water = 0 

#     for i in range(1,len(arr)):
#         leftMax.append(max(arr[:i]))

#     for j in range(len(arr) - 1):
#         rightMax.append(max(arr[j+1:len(arr)]))

#     rightMax.append(0)

#     for building in range(len(arr)):
#         height = min(leftMax[building], rightMax[building])
        
#         if height < arr[building]:
#             continue
#         water = water + (height - arr[building])

#     return water

# print(tappingRain(arr))

