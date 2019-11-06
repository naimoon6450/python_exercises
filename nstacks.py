# N stacks

class NStacks:
    def __init__(self, num, size):
        # number of stacks to build
        self.num_stack = num
        # array giving pointer to the top of the stacks
        self.top_stack = [-1] * num
        # the actual stack with data
        self.stack = [0] * size
        
        # if there's an element set at index 
        # when it's not set it points the the next avail item 
        self.nextPrevInd = []
        for i in range(size):
            self.nextPrevInd.append(i + 1)
        # change the last index to -1 because there's nothing after last elem
        self.nextPrevInd[size - 1] = -1

        # will be a pointer to the next available index
        self.nextAvail = 0

    def push(self, stackNum, val):
        # check for any out of bounds measures of if there's no more room left
        if stackNum < 0 or stackNum >= len(self.top_stack): return 'Out of bounds'
        if self.nextAvail < 0: return 'Stacks are all full'

        # first add to the stack
        self.stack[self.nextAvail] = val
        # set var for the current index, which is at nextAvail
        currInd = self.nextAvail
        
        # capture the previous of top of stack index
        oldTop = self.top_stack[stackNum]
        # change top of stack of stackNum to wherever the val will be placed in stack, which is given by currInd
        self.top_stack[stackNum] = currInd
        
        # next change the nextAvailable to the according index in the nextPrevInd array
        self.nextAvail = self.nextPrevInd[self.nextAvail]

        # change the nextPrevInd to oldTop
        self.nextPrevInd[currInd] = oldTop

    def pop(self, stackNum):
        # exceptions
        if stackNum < 0 or stackNum >= len(self.top_stack): return 'Out of bounds'
        # get current index from top of stack
        currInd = self.top_stack[stackNum]
        # return the popped value
        result = self.stack[currInd]

        # get the prev ind value to set topStack
        prevInd = self.nextPrevInd[currInd]

        # next avail needs to change to the currInd
        self.nextPrevInd[currInd] = self.nextAvail
        # next avail index needs to change
        self.nextAvail = currInd
        # top stack needs to change
        self.top_stack[stackNum] = prevInd 
        
        return result

        


three_stacks = NStacks(3, 10)
three_stacks.push(0, 5)
three_stacks.push(0, 6)
three_stacks.push(1, 8)
three_stacks.pop(0)
three_stacks.push(1, 8)

print(three_stacks.stack)
print(three_stacks.nextPrevInd)
        



        
        
