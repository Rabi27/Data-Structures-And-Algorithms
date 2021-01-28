#Delete middle element
rev = [1,2,3,4,5]
def midElement(arr,i):
    if i == len(arr)//2:
        arr.remove(arr[i])
        return arr
    midElement(arr,i+1)
midElement(rev,0)
print(rev)