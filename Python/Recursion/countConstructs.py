#count the number of construct a given word from a given array of strings
def countConstruct(target,words):
    
    if target == "":
        return 1
    
    count = 0
    
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            temp = countConstruct(suffix,words)
            count += temp
    
    return count

print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct('enterpotentpot',['a','p','ent','enter','ot','o','t']))
print(countConstruct('rabi',['a','ra','i']))
print(countConstruct('rabi',['a','ra','i','b']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))

#Memoied Version
memo = {}
def countConstruct_2(target,words):
    if target in memo: return memo[target]
    if target == "":
        return 1
    
    count = 0
    
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            temp = countConstruct_2(suffix,words) 
            count += temp
    memo[target] = count
    return count

print(countConstruct_2('purple',['purp','p','ur','le','purpl']))