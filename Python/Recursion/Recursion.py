#Printing Numbers recursively ==> 10-1
def p(n):
    if n != 0:
        print(n)
        p(n-1)
        
p(10)

#Printing Numbers recursively ==> 1-10
def p2(n):
    if n != 0:
        p2(n-1)
        print(n)
        
p2(10)

#Factorial Using Recursion
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
                 
print(fact(9))

#first greatest element
def largest(arr,i):
    if arr[i] > arr[i+1]:
        print(arr[i])
    else:
        i += 1
        print(i)
        largest(arr,i)

arr = [-1,2,4,3]

largest(arr,0)

arr = [3,4,1,2,6]

#Array splitting recursively
def divide(arr):
    
    if len(arr) == 1:
        return arr
    print('Before',arr)
    arr = arr[:len(arr)-1]
    divide(arr)
    print('After',arr)
divide(arr)

#Sorting Array recursively
# Using functions of sort and insert for this purpose       
def sort(arr):
    if len(arr) == 0:
        return 
    temp = arr[-1]
    arr.remove(temp)
    sort(arr)
    insert(arr,temp)

def insert(arr,temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    val = arr[-1]
    arr.remove(val)
    insert(arr,temp)
    arr.append(val)
    
arr = [5,6,2,1,9,-1,-2,99,12,1]

sort(arr)
print(arr)