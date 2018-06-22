# _CalebWest_
# This function takes a list of integers, and returns the maximum sum
# of non-adjacent elements.

# import dis

# main
def maxSum():
    
    # test lists
    intList = [5, 1, 1, 5] # output = 10
    intList2 = [2, 4, 6, 2, 5] # output = 13

    # previous max value, current max sum
    previous, current = 0, 0

    # loop controlled tuple sub-problem solver
    for i in intList:
       previous, current = current, max(current, previous + i)
    return current

maxNum = maxSum()
print(maxNum)

# prints opcodes for visualization
#dis.dis(maxSum)

