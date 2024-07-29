demo = [1,0,0,1,1,0,0,1,1]

count0 = 0
count1 = 0
for i in range(len(demo)):
    
    if demo[i] == 0:
        count0 += 1
    else:
        count1 += 1

for j in range(count0):
    demo[j] = 0

for k in range(count1, len(demo)):
    demo[k] = 1

print(demo)             # O(n)


arr = [1,0,0,1,1,0,1]

left = 0
right = len(arr) - 1

while (left < right):

    if arr[left] == 0:
        left += 1
    else:
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            right -= 1

print(arr)                  # O(n)



# while(left < right):
#     if(arr[left] == 0):
#         left += 1
#     if arr[right] == 1:
#         right -= 1
#     if arr[left] == 1 and arr[right] == 0:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1

# arr = [2,7,11,15,27]

# for i in range(len(arr)):
#     shouldBreak = False
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == 22:
#             print(arr[i], arr[j])
#             shouldBreak = True
#             break

#     if shouldBreak:
#         break                  # )(n*n)

# left = 0
# right = len(arr) - 1
# sum = 0  

# while(left < right):
    
#     sum = arr[left] + arr[right]

#     if sum == 22:
#         print(arr[left], arr[right])
#         break
#     elif sum > 22:
#         right -= 1
#     else:
#         left += 1           # O(n)


# for i in range(len(arr)):
#     for j in range(i+1, len(arr)+1):
#         if len(arr[i:j]) == 2:
#             sum = 0
#             print(arr[i:j])
#             for s in range(len(arr[i:j])):
#                 sum += arr[i:j][s]
#             if sum == 22:
#                 print(arr[i:j])
#                 break
            
# arr = [1,2,4,3,87,76]

# print(arr.sort())
# arr.sort()
# print(arr)

# def findNumber(num, arr):

#     left = 0
#     right = len(arr) - 1

#     while (left < right):

#         sum = arr[left] + arr[right]

#         if sum == num:
#             return arr[left], arr[right]
#         elif sum > num:
#             right -= 1
#         else: 
#             left += 1

#     return "No such combination"

# response = findNumber(10, arr)
# print(response)

# arr = [5,10,3,2,50,80]

# def pairs (diff, arr):

#     arr.sort()

#     left = 0
#     right = 1

#     while (left < right):

#         result = arr[right] - arr[left]

#         if result == diff:
#             return arr[right], arr[left]
#         elif result < diff:
#             right += 1
#         else:
#             left += 1
    
#     return -1

# pairs(45, arr)

# def pairs(diff, arr):

#     arr.sort()
#     print(arr)

#     left = 0
#     right = len(arr) - 1

#     while(left < right):

#         result = arr[right] - arr[left]

#         if result == diff:
#             return arr[right], arr[left]
#             break

#         elif result > diff:
#             left += 1
#         else:
#             right -= 1

#     return 0



# response = pairs(45, arr)
# print(response)

arr = [3,7,8,11,23]

def productPair(k, arr):

    arr.sort()
    left = 0
    right = len(arr) - 1

    while(left < right):

        product = arr[left] *arr[right]
    
        if product == k:
            return arr[left] , arr[right]
        elif product > k:
            right -= 1
        else: 
            left += 1
     
    return 0


response = productPair(21, arr)
print(response)