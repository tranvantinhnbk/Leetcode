m = 3
n = 7

## Method 1:
memo = [[None for i in range(n)] for j in range(m)]
def NumOfWay(m, n):
    if m == 0 or n == 0:
        if memo[m][n] == None:
            memo[m][n] = 1
        return memo[m][n]
    else:
        if memo[m][n] != None:
            return memo[m][n]
        else:
            return NumOfWay(m-1,n)+ NumOfWay(m, n-1)
print(NumOfWay(2,6))
 ## Method 2
# memo = [[None for i in range(n)] for j in range(m)]
# def NumOfWay(m, n):
#     for i in range(m):
#         for j in range(n):
#             if i == 0 or j == 0:
#                 memo[i][j] = 1
#             else:
#                 memo[i][j] = memo[i-1][j]+memo[i][j-1]
    

# print(NumOfWay(m,n))
# print(memo[m-1][n-1])