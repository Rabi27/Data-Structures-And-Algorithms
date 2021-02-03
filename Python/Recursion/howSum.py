#Given a target, find number array that adds up to the target

def howSum(target,nums):
    if target == 0: return []
    if target < 0: return None
    
    for num in nums:
        remainder = target - num
        result = howSum(remainder,nums)
        if result != None:
            return result+[num]
    
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
#When the output gets bigger, as always, the recursive function struggles in terms of speed.
#print(howSum(800,[7,14]))

#Memoized Version
memo = {}
def howSum_2(target,nums):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for num in nums:
        remainder = target - num
        result = howSum_2(remainder,nums)
        if result != None:
            return result+[num]
    
    memo[target] = None
    return None

print(howSum_2(800,[7,14]))