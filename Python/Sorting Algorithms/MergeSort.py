def mergeSort(arr):

    if len(arr) > 1:

        mid = (len(arr))//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        l = 0
        r = 0
        k = 0

        while l < len(L) and r < len(R):

            if L[l] < R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1
        

        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1
        

        while r < len(R) :
            arr[k] = R[r]
            r += 1
            k += 1

        return arr


nums = [3,4,1,2,5,6,1]

a = mergeSort(nums)
print(a)
    

