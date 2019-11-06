class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        strBuild = ''
        print('hi')
        for i in range(1, n + 1):
            print(i)
            if (i % 3 == 0):
                strBuild = 'Fizz'
                if (i % 5 == 0):
                    strBuild += 'Buzz'
            if (i % 5 == 0):
                strBuild = 'Buzz'

            if (strBuild != ''):
                result.append(strBuild)
            else:
                result.append(str(i))

        return result


obj = Solution()
# print(obj.fizzBuzz(15))


# variation
#  fizzBuzz logs numbers 1 - 50. anything divisible by 2 gets fizz, 4 gets buzz, 5 gets blazzo... multiples of both get both string
def fizzBuzzVar(arr, arrStr):
    strToDisplay = ''
    for count in range(1, 51):
        for ind in range(len(arrStr)):
            if (count % arr[ind] == 0):
                # create the string to print
                strToDisplay += arrStr[ind]
        # checks if there's something to show in string
        if (strToDisplay != ''):
            print(strToDisplay)
            # resets the string after print for next number
            strToDisplay=''
        else:
            # else print the actual number
            print(count)


fizzBuzzVar([2,4,5],['fizz','buzz','blazzo'])


