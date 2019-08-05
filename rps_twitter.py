#!/bin/python

import math
import os
import random
import re
import sys


# Apologies in advance for the horror that is below...
def handFormationChange(n, a, formations):
    # Write your code here
    dictOfWin = {
        'RP': 'P',
        'PR': 'P',
        'SR': 'R',
        'RS': 'R',
        'PS': 'S',
        'SP': 'S',
        'POIP': 'S',
        'PPOI': 'S',
        'SPOI': 'R',
        'POIS': 'R',
        'RPOI': 'P',
        'POIR': 'P',
        'PP': '',
        'SS': '',
        'RR': ''
    }
    formArr = list(formations)
    arrayInit = [0] * n
    # place POI in array
    arrayInit[a] = 'POI'
    for ind in range(len(arrayInit)-1, -1, -1):
        if (arrayInit[ind] != 'POI'):
            arrayInit[ind] = formArr.pop()

    changes = []
    resultArr = []
    initEval = []
    while(len(arrayInit) >= 1):
        # if there's one more remaining add to result arr
        if (len(arrayInit) == 1):
            lastVal = arrayInit.pop()
            resultArr.append(lastVal)
        else:
            # popping the values
            initEval.append(arrayInit.pop(0))

        if (len(initEval) == 2):
            stringify = ''.join(initEval)
            # if poi is playing then return poi add the change to changes
            if ('POI' in stringify):
                resultArr.append('POI')
                if (dictOfWin[stringify] != ''):
                    changes.append(dictOfWin[stringify])
            else:
                if (dictOfWin[stringify] != ''):
                    resultArr.append(dictOfWin[stringify])
            # reset after 2 vals
            initEval = []

        if (len(arrayInit) == 0):
            arrayInit = resultArr

        if (len(initEval) == 1 and len(arrayInit) == 1 and len(resultArr) == 1):
            lastEval = initEval[0] + arrayInit[0]
            if ('POI' in lastEval):
                if (dictOfWin[stringify] != ''):
                    changes.append(dictOfWin[lastEval])

        if (len(resultArr) == 1 and len(arrayInit) == 1):
            break

        print(arrayInit)
    remDupe = helper(changes)
    if (len(remDupe) > 1):
        return len(remDupe) - 1
    else:
        return 0


def helper(arr):
    return list(dict.fromkeys(arr))


print(handFormationChange(5, 3, 'RSPR'))

# 18
# 15
# RSPRSPRSPRSPRSPRS

# 5
# 3
# RSPR
