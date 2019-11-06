"""
Implementation using append, pop, length
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

"""
Implementation wo using append, pop, length
"""

# class Stack:
#     def __init__(self):
#         self.stack = []
#         # will contain the index to the top at all times
#         self.top = -1 
    
#     def push(self, val):
#         if (len(self.stack) == 0):
#             self.top += 1
#             self.stack += [val]
#         else: 
#             self.top += 1
#             self.stack += [val]
#         print(self.top)
#     def pop(self):

#         returnVal = None
#         if (not len(self.stack)):
#             returnVal = self.stack[self.top]
#             del self.stack[self.top]
#             self.top -= 1
#             return returnVal
        
#         return returnVal
    
#     def peek(self):
#         return self.stack[self.top]
    


"""
Parenthesis checker (balanced or not) using stack
"""

# def balancedParen(input):
#     listify = list(input)
#     newStack = Stack()
#     for ind in range(len(listify)):
#         char = listify[ind]
#         if (char == '('):
#             # push into stack
#             newStack.push(char)
#         elif (char == ')' and newStack.size() != 0):
#             newStack.pop()

#     print(newStack.stack)
#     # return not newStack.size()


"""
Infix to Postfix
"""

def inToPost(input):
    precedenceDict = {
        '+': 3,
        '-': 3,
        '*': 2,
        '/': 2,
        '(': 1,
    }
    inputList = list(input)
    postFixResult = ''
    operatorStack = Stack()
    charList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    opList = '+-/*('
    for ind in range(len(inputList)):
        char = inputList[ind]
        if (char in charList):
            postFixResult += char
        
        if (char in precedenceDict):
            if (not operatorStack.size):
                operatorStack.push(char)
            # check for parens
            
            # else check for precendence of top of stack and current char
            elif (precedenceDict[char] > precedenceDict[operatorStack.peek()]):




    