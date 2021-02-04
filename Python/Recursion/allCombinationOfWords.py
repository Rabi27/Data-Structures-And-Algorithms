#All combinations to construct a word
def allCombinations(target,words):
    if target == "": return [[]]
    res = []
    for word in words:
        
        if target.find(word) == 0:
            suffix = target[len(word):]
            combinations = allCombinations(suffix,words)
            for c in combinations:
                c.insert(0,word)
                res.append(c)
        
    return res
    
#All combinations to construct a word with memoization
memo = {}
def allCombinations_2(target,words):
    if target in memo: return memo[target]
    if target == "": return [[]]
    res = []
    for word in words:
        
        if target.find(word) == 0:
            suffix = target[len(word):]
            combinations = allCombinations_2(suffix,words)
            for c in combinations:
                c.insert(0,word)
                res.append(c)
    
    memo[target] = res
    return res
    
print(allCombinations_2('abcdef',['ab','abc','cd','def','abcd','ef','c']))
print(allCombinations_2('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(allCombinations_2('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(allCombinations_2('rabi',['a','ra','i']))
print(allCombinations_2('rabi',['a','ra','i','b']))
print(allCombinations_2('purple',['purp','p','ur','le','purpl']))
            