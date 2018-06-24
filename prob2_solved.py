# AUTHOR: Caleb West Hoffman

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def kSum(kList, n, k, switch):
    
    for i in range(0, n):
        for x in range(i + 1, n):
            if kList[i] + kList[x] == k:
                print("The integers equal to k Value are " ,kList[i] ,"and", kList[x])
            else:
                switch = True
    return kList, n, k, switch

# test list
kList = [10, 15, 3, 7] # k = 17 = kList[0] + kList[3]

#constants
k = 17
n = len(kList)
switch = False

# executes main function
kSum(kList, n, k, switch)

# conditional alert
if switch:
    print("k Value was not found")
