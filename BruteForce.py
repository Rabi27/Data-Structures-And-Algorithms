lis = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
max_sum = 0
#Defining size of subarray
k = 4
#Using the brute force approach to compute sum of each subarray of size 3 in the list
print("Brute Force Approach")
for i in range(len(lis)-k+1):

    curr_sum = 0
    for j in range(k):
        curr_sum = curr_sum + lis[i+j]
    max_sum = max(max_sum,curr_sum)
        
   
print("Maximum Sum:",max_sum)
