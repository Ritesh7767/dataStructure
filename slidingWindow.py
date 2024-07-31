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

    for c in range(len(string)):

        if c in char_index_map:
            

        # if c not in char_index_map:
        #     numberCharacter -= 1

        if numberCharacter == 0:
            minString = string[start:c+1]
            print(minString)

        while(numberCharacter != 0)

        # if end - start + 1 > 8: 
        #     start += 1

    return minString

response = minString('ritehsdsflk')
print(response)


        
        
        



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

