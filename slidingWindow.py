name = "abcabcdefghabcd"

def minString(string):

    char_index_map = {}

    for s in string:
        if s in char_index_map:
            char_index_map[s] += 1
        else:
            char_index_map[s] = 1

    print(len(char_index_map.items()))
    numberCharacter = len(char_index_map.items())

    start = 0
    end =  numberCharacter - 1
    char_index_map = {}
    minString = ""

    # for c in range(len(string)):

    #     if c in char_index_map:
            

        # if c not in char_index_map:
        #     numberCharacter -= 1

        # if numberCharacter == 0:
            # minString = string[start:c+1]
            # print(minString)

        # while(numberCharacter != 0)

        # if end - start + 1 > 8: 
        #     start += 1

    # return minString

# response = minString('ritehsdsflk')
# print(response)


        
        
        



# minString(name)

# frequency = {}
# for s in name:
#     if s in frequency:
#         frequency[s] += 1
#     else:
#         frequency[s] = 1

# print(frequency)


# def frequency(string):

#     char_index_map = {}

#     print(string)

#     for s in string:
#         print(s)
#         if s in char_index_map:
#             char_index_map[s] += 1
#         else:
#             char_index_map[s] = 1

#     return char_index_map


# response = frequency("ritesh")
# print(response)

# def minString(arr):

#     char_index_map = {}

#     for i in arr:
#         if i in arr:
#             char_index_map[i] += 1
#         else:
#             char_index_map[i] = 1

#     return char_index_map

# response = minString(name)
# print(response)

# def maxSubstring(arr):

#     start = 0
#     maxLength = 0
#     char_index_map = {}
#     maxString = ""

#     for end in range(len(arr)):


#         if arr[end] in char_index_map:
#             start = max(start, char_index_map[arr[end]] + 1)
#         char_index_map[arr[end]] = end

#         sum = end - start + 1
#         if maxLength < sum:
#             maxString = arr[start:end+1]
#             maxLength = sum

#     return maxLength, maxString

# response = maxSubstring(name)

# print(response)
        


# def maxSubstring(string):

#     start = 0
#     maxlength = 0
#     char_index_map = {}
#     substring = ""

#     for end in range(len(string)):

#         if string[end] in char_index_map:
#             start = max(start, char_index_map[string[end]] + 1)
#         char_index_map[string[end]] = end

#         print(start, end)

#         if end + 1 - start + 1 > maxlength:
#             maxlength = end + 1 - start + 1
#             print(maxlength)
        
#     return maxlength

# response = maxSubstring("ritesh")

# print(response)

    # start = 0
    # maxlength = 0
    # char_index_map = {}

    # for end in range(len(string)):

    #     if string[end] in string:
    #         start = max(start, char_index_map[string[end]] + 1)
    #     char_index_map[string[end]] = end

    #     if (end + 1) - (start + 1) > max_length:
    #         max_length = (end + 1) - (start + 1)
        
    # return maxlength

# response = maxSubstring(name)

# def frequency(string){
#     response = {}
#     for s in string:
#         if s in string:

# }

# result = {}
# for s in name:
#     if s in result:
#         result[s] += 1
#     else:
#         result[s] = 1

# print(result)

# user = {
#     "name": "ritesh",
#     "salary": 50000
# }

# for s in user:
#     print(s)

# if "name" in user:
#     print(user["name"])

# if "ritesh" in user:
#     print(user)
# def longestString(arr):
#     start = 0
#     end = 0
#     longestString = ""


def substring(string):

    left = 0
    
    for right in range(2, len(string)):

        print(string[left:right+1])
        left += 1

string = "ritesh"
# substring(string)

# def uniqueSubString(string):

#     left = 0
#     char_map_index = {}

#     for right in range(len(string)):

#         if string[right] in char_map_index:
#             left = max(left, char_map_index[string[right]]+1)
#         print(string[left:right])
#         char_map_index[string[right]] = right 

#     print(string[left])

# uniqueSubString("aababcabc")

# def uniqueSubString(string):

#     left = 0
#     char_map_index = {}

#     for right in range(len(string)):

#         if string[right] in char_map_index:
#             left = max(left, char_map_index[string[right]]+1)
#             if len(string[left:right+1]) == 3:
#                 print(string[left:right+1])
#         char_map_index[string[right]] = right

#     print(string[left:])

# string = "aababcabc"
# uniqueSubString(string)

# def uniqueSubString(string):

#     left = 0
#     char_index_map = {}

#     for right in range(len(string)):

#         if string[right] in char_index_map:
#             print(string[left:right])
#             left = max(left, char_index_map[string[right]]+1)
#         char_index_map[string[right]] = right

# uniqueSubString(string)

def subString3(string):

    if len(string) < 3:
        return

    left = 0
    count = 0
    for right in range(2, len(string)):

        print(string[left:right+1])
        print(set(string[left:right+1]))
        if len(set(string[left:right+1])) == 3:
            count += 1

        left += 1

    return count

string = "xyzzaz"
# result = subString3(string)
# print(result)

colors = [0,1,0,0,1]
# color = [0,1,0,0,1,0,1]

def differentCombination(colors):

    if len(colors) < 3:
        return 
    
    colors.append(colors[0])
    colors.append(colors[1])

    left = 0
    
    for right in range(2,len(colors)):

        if colors[left] == colors[right] and colors[left+1] != colors[left]:
            print(colors[left:right+1])
        left += 1
    
# colors = [0,0,1]
# differentCombination(colors)


def rightSum(number):

    result = sum(number)
    rightSum = []

    for i in range(len(number)):
        result -= number[i]
        rightSum.append(result)

    return rightSum

def leftSum(number):

    result = sum(number)
    leftSum = []
    for i in range(len(number)-1, -1, -1):

        result -= number[i]
        leftSum.append(result)

    return leftSum[::-1]

def leftSumPointer(number):

    leftSum = [0]
    sum = 0
    for i in range(1, len(number)):
        sum += number[i-1]
        leftSum.append(sum)

    return leftSum

# def rightSumPointer(number):

#     rightSum = [0]
#     sum = 0

#     number = number[::-1]
#     for i in range(1, len(number)):
#         sum += number[i]
#         rightSum.append(sum)

#     return rightSum[::-1]

def rightSumPointer(number):

    rightSum = []
    sum = 0

    for i in range(len(number)-1, -1, -1):
        
        if i == len(number)-1:
            rightSum.append(0)
            continue

        sum += number[i+1]
        rightSum.append(sum)

    return rightSum[::-1]

# def leftRightDifference(number):

#     leftSum = [0]
#     rightSum = [0]

#     lsum = 0
#     rsum = 0

#     for i in range(1, len(number)):
#         lsum += number[i-1]
#         leftSum.append(lsum)

#     for j in range(len(number)-2, -1, -1):
#         rsum += number[j+1]
#         rightSum.append(rsum)

#     rightSum = rightSum[::-1]
#     print(leftSum, rightSum)
#     result = []
#     for i in range(len(leftSum)):
#         result.append(abs(leftSum[i]-rightSum[i]))

#     return result

def leftSumDifference(number):

    summation = sum(number)
    lsum = 0
    result = []

    for i in range(len(number)):

        summation -= number[i]
        if i == 0:
            result.append(abs(0-summation))
            continue
        lsum += number[i-1]
        result.append(abs(lsum - summation))

    return result

number = [10,4,8,3]
number = [1]
# print(leftSumDifference(number))
# print(leftRightDifference(number))


# print(leftSumPointer(number))
# print(rightSumPointer(number))
# print(rightSum(number))
# print(leftSum(number))

def runningSum(number):

    sum = 0

    for i in range(len(number)):
        sum += number[i]
        number[i] = sum

    return number

number = [1,2,3,4]
# print(runningSum(number))

def pivotInteger(number):
    
    arr = []
    for i in range(1, number+1):
        arr.append(i)

    leftSum = 0
    rightSum = sum(arr)

    for i in range(len(arr)):
        if leftSum == rightSum:
            return i
        rightSum -= arr[i]
        if i == 0:
            


    return -1

print(pivotInteger(8))