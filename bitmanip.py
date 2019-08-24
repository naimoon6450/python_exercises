def countBits(x):
    # num_bits = 0
    # while x:
    #     num_bits += x & 1
    #     print('in binary', str(bin(x))[2:])
    #     x >>= 1
    # return num_bits
    bins = str(bin(x))[2:];
    print(bins)
    newbin = str(bin(x >> 1))[2:];
    print(newbin)

# print(countBits(10))

"""
11010 = num = 26

Find the i-th bit so if i = 3 the mask goes from 0001 to 1000

then you & it with the original number to clear the remaining bits 
11010
01000

1000 and check if result CONTAINS a 1, we don't care what the result is
BUT if it contains a 1 it's definitely not = 0
"""

def getIthBit(num, i):
    bool = (num & (1 << i)) != 0
    return bool

# print(getIthBit(26, 1))
print(2 & (1 << 0))
