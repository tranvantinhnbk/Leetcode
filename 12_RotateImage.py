matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n = len(matrix)
k = n//2
for i in range(k):
    for j in range(i, n-i-1):
        temp1 = matrix[j][n-1-i]
        matrix[j][n-1-i] = matrix[i][j]
        temp2 = matrix[n-1-i][n-1-j]
        matrix[n-1-i][n-1-j] = temp1
        temp1 = matrix[n-1-j][i]
        matrix[n-1-j][i] = temp2
        matrix[i][j] = temp1
        
print(matrix)