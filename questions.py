name = "acbddacdabcdefghijk"

# uniqueChar = set(name)
def minString (string):

    uniqueChar = len(set(name))
    print(uniqueChar)

    left = 0
    minString = ""
    minLength = 0
    diff = uniqueChar
    char_index_map = {}

    for char in range(len(string)):

        if string[char] in char_index_map:
            char_index_map[string[char]] += 1
        else:
            char_index_map[string[char]] = 1
            diff -= 1

        if diff == 0:

            print(char_index_map)
            minString = string[left:char + 1]
            minLength = char - left + 1

            while (diff == 0):

                char_index_map[string[left]] -= 1
                if char_index_map[string[left]] == 0:
                    minString = string[left:char+1]
                    minLength = char - left + 1
                    diff += 1

                left += 1

    return minString, minLength

print(minString(name))




