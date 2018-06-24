# AUTHOR: Caleb West Hoffman

# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array
# except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
# [2, 3, 6].

# Follow-up: what if you can't use division? """

arr = [1, 2, 3, 4, 5] # [120, 60, 40, 30, 24]
n = len(arr)

def arrIndex():

    product = 1
    for i in range(n):
        product *= arr[i]
    newArr = [product//i for i in arr]

    return newArr

newArr = arrIndex()
print(newArr)
            
