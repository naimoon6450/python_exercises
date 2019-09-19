def same(init_arr, sq_arr):
    if (not len(init_arr) == len(sq_arr)):
        return 'Freq not same'
    
    freqInit = {}
    prodDict = {}
    for ind in range(len(init_arr)):
        if (init_arr[ind] not in freqInit):
            freqInit[init_arr[ind]] = 1
        else:
            freqInit[init_arr[ind]] += 1
        
        if (sq_arr[ind] not in prodDict):
            prodDict[sq_arr[ind]] = 1
        else:
            prodDict[sq_arr[ind]] += 1
    
    lenSuccess = 0
    for ind in range(len(init_arr)):
        square = init_arr[ind] ** 2
        if (freqInit[init_arr[ind]] == prodDict[square]):
            lenSuccess += 1
    
    if (lenSuccess == len(init_arr)):
        return True
    
    return False



print(same([1,2,3], [4,1,9]))


""" returns true if there's a squared result of each elem in init arr .. must contain the frequency as well so if there's [1, 2, 1] and prod array is [4, 4, 1] although it has the squared products the freq is off so [4, 1, 1] would work

freqInit = {
    1: 2,
    2: 1
}

freqProd = {
    1: 2,
    4: 1
}


Naive approach is to loop through initial array and index second array for the square

On every successful index, you remove the indexed square and continue the loop/search until nothing remains in second array or the square isn't in the array
"""