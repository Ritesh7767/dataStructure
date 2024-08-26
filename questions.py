# name = "abbccd"

# def minString(string):

#     if not string:
#         return "", 0

#     uniqueChar = len(set(string))
#     left = 0
#     minString = ""
#     minLength = float("inf")
#     diff = uniqueChar
#     char_index_map = {}

#     for right in range(len(string)):
#         if string[right] in char_index_map:
#             char_index_map[string[right]] += 1
#         else:
#             char_index_map[string[right]] = 1
#             diff -= 1

#         while diff == 0:
#             if minLength > right - left + 1:
#                 minString = string[left:right + 1]
#                 minLength = right - left + 1

#             char_index_map[string[left]] -= 1
#             if char_index_map[string[left]] == 0:
#                 diff += 1

#             left += 1

#     return minString, minLength

# print(minString(name))


# Example usage:
# name = "abbcdefabcdef"
# result = minString(name)
# print("The minimum distinct substring is:", result[0], "with length:", result[1])

# def minString (string):

#     uniqueChar = len(set(string))

#     left = 0
#     minString = ""
#     minLength = float("inf")
#     diff = uniqueChar
#     char_index_map = {}

#     for right in range(len(string)):

#         if string[right] in char_index_map:
#             char_index_map[string[right]] += 1

#         else:
#             char_index_map[string[right]] = 1
#             diff -= 1

#         while (diff == 0):

#             if minLength > right - left + 1:
#                 minString = string[left:right + 1] 
#                 minLength = right - left + 1

#             char_index_map[string[left]] -= 1
#             if char_index_map[string[left]] == 0:
#                 diff += 1

#             left += 1

#     return minString, minLength


arr = [2,3,1,2,4,3]

def minArr (k, arr):

    left = 0
    # right = 0
    minLength = float('inf')
    minArr = []
    sum = 0


    for right in range(len(arr)):

        sum += arr[right]

        while sum >= k:

            if sum == k:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minArr = arr[left:right + 1]
                
            sum -= arr[left]
            left += 1

    return minLength, minArr



    # while right < len(arr):

        # sum += arr[right]

        # if sum == k:
        #     if right - left + 1 < minLength:
        #         minLength = right - left + 1
        #         minArr = arr[left:right+1]
        
        # if sum > k:
            # sum -= arr[left] - arr[right]
            # left += 1

        # else:
        #     right += 1

    return minLength, minArr

    # for right in range(len(arr)):

    #     sum += arr[right]

    #     if sum == k:
    #         if right - left + 1 < minLength:
    #             minLength = right - left + 1
    #             minArr = arr[left:right+1]
        
    #     if sum > k:
            


    # while (right < len(arr)):

    #     sum += arr[right]

    #     if sum == k:
    #         if right - left + 1 < minLength:
    #             minLength = right - left + 1
    #             minArr = arr[left:right + 1]
    #     if sum > k and left < right:
    #         sum -= arr[left]
    #         left += 1

    return minLength, minArr

# response = minArr(7, arr)    
# print(response)




# def minArr (k, arr):

#     left = 0
#     right = 1
#     minLength = float('inf')    
#     minSubArr = []

#     while right < len(arr):

#         sum = arr[left] + arr[right]

#         if sum == k:

#             print("sum block")
#             if minLength > right - left + 1:
#                 minLength = right - left + 1
#                 minSubArr = arr[left:right+1]
        
#         if sum < k:
#             right += 1

#         else:
#             left += 1

#     return minLength, minSubArr

# print(minArr(7, arr))

string = 'ADOBECODEBANC'

def minString(sub, string):

    left = 0
    minLength = float('inf')
    minArr = []
    char_index_map = {}

    for s in sub:
        char_index_map[s] = 1

    totalChar = len(char_index_map.values())

    for right in range(len(string)):

        if string[right] in char_index_map:
            char_index_map[string[right]] = 0
            totalChar -= 1

        while totalChar == 0:
            
            if right - left + 1 < minLength:
                minLength = right - left + 1
                minArr = string[left:right+1]

            if string[left] in char_index_map:
                char_index_map[string[left]] = 0
                totalChar += 1

            left += 1

    return minArr, minLength

response = minString("ABC", string)
# print(response)


# def minString(sub, string):

#     left = 0
#     minLength = float('inf')
#     minArr = []
#     char_index_map = {}
#     result_index_map = {}

#     for s in sub:
#         if s in char_index_map:
#             char_index_map[s] += 1
#         else:
#             char_index_map[s] = 1
#         result_index_map[s] = 0

#     print(char_index_map, result_index_map)
    
#     for right in range(len(string)):

#         if string[right] in result_index_map:
#             result_index_map[string[right]] += 1
#         else:
#             result_index_map[string[right]] = 1

        # print(result_index_map)
         
        # if result_index_map == char_index_map:
            # print(result_index_map, char_index_map)
#             while result_index_map != char_index_map:
                
#                 if right - left + 1 < minLength:
#                     minLength = right - left + 1
#                     minArr = string[left:right+1]

#                 result_index_map[string[left]] -= 1
#                 left += 1

#     return minArr, minLength

# print(minString('ABC', string))

arr = [1,2,3,1,2,3,3,4,1,2,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
k = 2

def longestArr(k, arr):

    left = 0
    maxLength = 0
    maxArr = []
    char_index_map = {}
    
    for right in range(len(arr)):

        if arr[right] in char_index_map:
            char_index_map[arr[right]] += 1
        else:
            char_index_map[arr[right]] = 1

        while char_index_map[arr[right]] > k:

            if right - left > maxLength:
                maxLength = right - left 
                maxArr = arr[left:right]

            char_index_map[arr[left]] -= 1
            left += 1

    if len(arr) - left > maxLength:
        maxLength = len(arr) - left
        maxArr = arr[left:]

    return maxArr, maxLength

# print(longestArr(k, arr))

# def longestArr(k, arr):

#     left = 0
#     maxLength = 0
#     maxArr = []
#     char_index_map = {}
#     formed = False

#     for right in range(len(arr)):

#         if arr[right] in char_index_map:
#             char_index_map[arr[right]] += 1
#             if char_index_map[arr[right]] > k:
#                 formed = True
#         else:
#             char_index_map[arr[right]] = 1

#         while formed: 

#             if right - left + 1 > maxLength:
#                 maxLength = right - left
#                 maxArr = arr[left:right]

#             char_index_map[arr[left]] -= 1

#             if char_index_map[arr[left]] == 2:
#                 formed = False

#             left += 1
    
#     return maxArr, maxLength

# arr = [1,2,3,2,3,1,2,3,3,2]
# k=2

def countSubArray(k, arr):
    left = 0
    count = 0
    arrCount = 0
    maxArr = []
    maximum = max(arr)  # Find the maximum element in the array

    for right in range(len(arr)):
        if arr[right] == maximum:
            count += 1

        while count > k:
            if arr[left] == maximum:
                count -= 1
            left += 1

        # All subarrays ending at 'right' and starting from 'left' to 'right'
        arrCount += right - left + 1
        maxArr.extend([arr[i:right + 1] for i in range(left, right + 1)])

    return maxArr, arrCount

k = 2

# print(countSubArray(k, arr))


# def countSubArray(k, arr):

#     left = 0
#     count = 0
#     arrCount = 0
#     maxArr = []
#     maximum = 0

#     for i in arr:
#         maximum = max(i, maximum)

#     for right in range(len(arr)):

#         if arr[right] == maximum:
#             count += 1

#         while count > k:

#             arrCount += 1
#             maxArr.append(arr[left:right])

#             if arr[left] == maximum:
#                 count -= 1

#             left += 1

#     arrCount += 1
#     maxArr.append(arr[left:])

#     return maxArr, arrCount

# print(countSubArray(k, arr))



# def subArr(k, arr):

#     left = 0
#     maxLength = 0
#     maxArr = []
#     maximum = max(set(arr))
#     count = 0

#     for right in range(len(arr)):

#         if arr[right] == maximum:
#             count += 1

#         while count > k:

#             if arr[left] == maximum:
#                 count -= 1

#             left += 1

#         if right - left + 1 > maxLength and count == k:
#             maxLength = right - left + 1
#             maxArr = arr[left:right + 1]

#     return maxLength, maxArr

# response = subArr(k, arr)
# print(response)

# def subArr(k, arr):

#     left = 0
#     maxArr = []
#     maxLength = 0
#     maximum = max(set(arr))
#     count = 0

#     for right in range(len(arr)):

#         if arr[right] == maximum:
#             count += 1

#         print(count)
#         # while count >= k:

#             # print(left, count, arr[left])
#             # print(count)
#             if right - left + 1 > maxLength:
#                 maxLength = right - left + 1
#                 maxArr = arr[left:right+1]

#             if arr[left] == maximum:
#                 count -= 1

#             left += 1

#     if len(arr) - left > maxLength:
#         maxLength = right - left + 1
#         maxArr = arr[left:right+1]

#     return maxLength, maxArr
# arr = [1, 2, 3, 2, 3, 1, 2, 3, 3, 2, 1]

arr = [3,5,6,3,9,4,6,9]
k = 7

def arrCount (k,arr):

    left = 0
    count = 0
    sum = 0
    Arr = []
    for right in range(len(arr)):

        sum += arr[right]

        while sum >= k and left < right:

            print(arr[left:right+1])
            if sum % k == 0:
                print(arr[left:right+1])
                count += 1
                Arr.append(arr[left:right+1])

            sum -= arr[left]
            left += 1

    return count, Arr
    
print(arrCount(k, arr))

        


