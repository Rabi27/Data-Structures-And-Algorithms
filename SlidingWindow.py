lis = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
subarr = []
dic = {}
sumarr = []
k = 4 #Defining size of subarray
#Using the brute force approach to compute sum of each subarray of size 3 in the list
print("Brute Force Approach")
for i in range(len(lis)-k+1):
    
  
    sum = 0
    for j in range(i,k):
        sum = sum + lis[j]
        subarr.append(lis[j])
   
        
    sumarr.append(sum)
    dic[sum] = subarr
    subarr = []
   

print(dic)
print("Maximum Sum:",max(sumarr))

'''
Brute Force Approach
1+2+3 = 6
2+3+4 = 9 (redoing 2+3)
3+4+5 = 12 (redoing 3+4)
4+5+6 = 15 (redoing 4+5)
5+6+7 = 18 (redoing 5+6)

Optimized Solution
1+2+3 = 6
7-prev+next = 7-1+4 = 9
9-prev+next = 9-2+5 = 12
...
In this solution we're not re-computing as in the Brute Force Approach





Sliding Window questions are of two types:
1-Fixed Size Window
2-Variable Size Window

1-In fixed size window, when the size of the Window is reached, some calculations are to be performed.
In our case, these calculations are to calculate the sum.

2-In variable size Window questions, the size of the window is to be computed by us. Example of these
questions is to finding maximum subarray of characters with no repeating characters.

 
'''


print("Sliding Window Approach")

l = [1, 4, 2, 10, 2, 3, 1, 0, 20] 

#defining the size of the window
window_size = 4
#Initializing the sum variable for the sum of 1st Window elements
res = 0
#computing the sum for the elements of the first window
for i in range(window_size):
    res = res + l[i]

#Initialzing sum variable for finding sum for each window
curr_sum = 0

#Determining the max_sum subarray value
for i in range(window_size,len(l)):

    curr_sum = max(res+l[i]-l[i-window_size],sum)
    res = max(res,curr_sum)

print("Maximum Sum:",res)