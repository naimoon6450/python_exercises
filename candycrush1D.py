# Given a string, reduce the string by removing 3 or more consecutive identical characters. You should greedily remove characters from left to right.

# this finds shortes string 
def removeThree(string):
    dictStr = {}
    for char in string:
        if dictStr.get(char):
            dictStr[char] += 1
        else:
            dictStr[char] = 1
    result = []

    for char in string:
        if dictStr.get(char) < 3:
            result.append(char)
    
    return ''.join(result)

# CONSECUTIVE DUPES of >=3 will need a stack 


print(removeThree("aaabbbc"))
print(removeThree("aabbbacd"))
print(removeThree("aaabbbacd"))
print(removeThree("baaabbbabbccccd"))
print(removeThree("aabbccddeeedcba"))