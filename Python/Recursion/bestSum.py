#best sum using Memoization
memo = {}
def howSum_2(target,nums):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    bestSum = None

    for num in nums:
        remainder = target - num
        result = howSum_2(remainder,nums)
        if result != None:
             combination = result + [num]
             if bestSum == None or len(combination) < len(bestSum):
                bestSum = combination
            
   
    memo[target] = bestSum
    return bestSum

print(howSum_2(7,[2,3,4,5]))

print(howSum_2(2009,[2,3,4,5]))