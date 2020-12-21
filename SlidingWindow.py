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
k = 4
#computing the sum for the elements of the first window
res = sum(l[:k])
max_sum = res

#Determining the max_sum subarray value
for i in range(len(l)-k):
    res = res-l[i]+l[i+k]
    max_sum = max(res,max_sum)
    

print("Maximum Sum:",max_sum)