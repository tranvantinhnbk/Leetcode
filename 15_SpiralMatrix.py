matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m = len(matrix)
n = len(matrix[0])
res = [0]*m*n

index = 0
i = 0 
while True:
    for j in range(i, n-i):
        res[index] = matrix[i][j]
        index+=1
    if index==n*m:
        return res
    for j in range(i+1, m-i):
        res[index]=matrix[j][n-1-i]
        index+=1
    if index==n*m:
        return res
    for j in reversed(range(i,n-1-i)):
        res[index] = matrix[m-1-i][j]
        index+=1
    if index==n*m:
        return res
    for j in reversed(range(i+1, m-1-i)):
        res[index] = matrix[j][i]
        index+=1
    if index==n*m:
        return res
    i+=1
    print(res)
