
# from python.numOfElemsRight import numOfElems
from python.numOfElemsRight import binSearch

# def testNumOfElems():
#     assert numOfElems([3,  4,  9,  6,  1]) == [1, 1, 2, 1, 0]
#     assert numOfElems([5,2,6,1]) == [2,1,1,0]

def testBinSearch():
    assert binSearch([4,9,6,1], 3) == 1
    assert binSearch([9,6,1], 4) == 1
    assert binSearch([6,1], 9) == 2
    assert binSearch([1], 6) == 1
    assert binSearch([], 1) == 0
