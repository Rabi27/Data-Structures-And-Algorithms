#Can Construct a given word from a given array of strings

#find method vs index method
#If substring exists inside the string, both methods return the lowest index in the string where substring is found.
#The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.

def canConstruct(target,words):
    
    if target == "":
        return True
    
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix,words) == True:
                return True
    
    return False

print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct('enterpotentpot',['a','p','ent','enter','ot','o','t']))
print(canConstruct('rabi',['a','ra','i']))
print(canConstruct('rabi',['a','ra','i','b']))
#When the size of input increases the below, example does not run
#print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))

#Memoized Version
memo = {}
def canConstruct_2(target,words):
    
    if target in memo: return memo[target]
    if target == "":return True
    
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct_2(suffix,words) == True:
                return True
    memo[target] = False
    return False

print(canConstruct_2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))