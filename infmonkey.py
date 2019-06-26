# encoding=utf8
# The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

import random as rand
# generate 26 letters + string
def generateString():
    strOfLetters = 'qwertyuiopasdfghjklzxcvbnm '
    split = list(strOfLetters) #will spit the str of letters to array
    formSentence = []
    # start generating a string
    for num in range(27):
        formSentence.append(split[rand.randint(0, 26)])
    
    return "".join(formSentence)



print(generateString())
