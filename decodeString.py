"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

when you bump into a closing bracket, store result and pop
seems recursive

3 [ a 2 [ c ] ]
3 [ a c c ]

temp = 'cc'

num stack = 3 2 
              top
alph sta  = [ a [ c ]
alph sta  = [ a c c ]


When you bump into ], pop the alpha stack until you reach [, then pop numeric stack, and multiple that by the temp and push to stack

"""



def decodeStr(str1):
    strList = list(str1)
    pt = 0

    numStack = []
    alphStack = []
    builtStr = ''

    while (pt < len(strList)):
        # single digit only
        if strList[pt].isdigit():
            numStack.append(strList[pt])
            # increment to next char
            pt += 1
        elif strList[pt] == ']':
            popped = alphStack.pop()
            tempStr = ''
            # while the popped val is not an open brack means there are more characters
            while popped != '[':
                tempStr += popped
                popped = alphStack.pop()
            
            numPop = numStack.pop()
            builtStr += int(numPop) * tempStr[::-1]

            if len(alphStack) > 0:
                print(builtStr, len(alphStack))
                alphStack += list(builtStr)
                builtStr = ''
                tempStr = ''
                popped = ''
            if len(alphStack) == 0:
                tempStr = ''
                popped = ''
            
            
            pt += 1
        else:
            alphStack.append(strList[pt])
            pt += 1
    print('I am builtStr',builtStr)

decodeStr("3[a2[c]]")


                
