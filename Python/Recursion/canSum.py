#Can Sum with Recursion
#Given a target, check if the numbers of the array add up to the target
def canSum(target,nums):
    #If the target sum becomes 0, simply return 0
    if target == 0: return True
    
    #If the target sum becomes negative, return 0
    #i.e ... say remainder is 1, and the num = 2 , 1 - 2 = -1,
    #Hence return False
    if target < 0: return False
    
    for num in nums:
        remainder = target - num
        if canSum(remainder,nums):
            return True
    return False

#Above code works for the following examples
print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))

#But when the input is big, it becomes slow
#print(canSum(800,[7,14]))

#Optimized Solution with Memoization
memo = {}
def canSum_2(target,nums):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    
    for num in nums:
        remainder = target - num
        if canSum_2(remainder,nums):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

print(canSum_2(800,[7,14]))