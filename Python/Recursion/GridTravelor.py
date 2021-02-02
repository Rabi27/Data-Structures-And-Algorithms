#Left substree involves decreasing a row
#Right substree involves decreasing a column
#Everytime rows and columns are same, that constitutes to a single 
#way of traversing through m*n grid
#we would return 1 whenver m and n are equal to 1
#and adding their sum

def gridTravelor(m,n):
    if m == 1 and n== 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTravelor(m-1,n) + gridTravelor(m,n-1) 

print(gridTravelor(1,1))
print(gridTravelor(2,1))
print(gridTravelor(3,3))
print(gridTravelor(8,8))
#18 * 18 GRID is too much for this solution
#print(gridTravelor(18,18))
#Now we optimize the above solution

#Optimized Solution
memo = {}
def gridTravelor_2(m,n):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 and n== 1:
        return 1
    if m == 0 or n == 0:
        return 0
    value =  gridTravelor_2(m-1,n) + gridTravelor_2(m,n-1) 
    memo[(m,n)] = value
    return value

print(gridTravelor_2(18,18))
