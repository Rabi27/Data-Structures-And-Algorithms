#Reverse an arr
rev = [1,2,3,4,5]
def reverseArray(arr):
    if len(arr) == 0:
        return
    temp = arr[0]
    arr.remove(temp)
    reverseArray(arr)
    arr.append(temp)
    return arr

reverseArray(rev)
print(rev)

    