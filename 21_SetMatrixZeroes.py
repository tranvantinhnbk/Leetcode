matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zeros = 1

## Check top left element if it 0 then column zeros is zero
if matrix[0][0] == 0:
    zeros = 0

# top left responsible for first row
for j in range(1, len(matrix[0])):
    if matrix[0][j] == 0:
        matrix[0][0] = 0

#zeros responsible for first column
for i in range(1, len(matrix)):
    if matrix[i][0] == 0:
        zeros = 0

for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        if matrix[i][j] == 0:
            matrix[0][j] = 0
            matrix[i][0] = 0

for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0 or matrix[i][0] == 0:
            matrix[i][j] = 0

if matrix[0][0] == 0:
    for j in range(1, len(matrix[0])):
        matrix[0][j] = 0

if zeros == 0:
    for i in range(len(matrix)):
        matrix[i][0] = 0
print(matrix)

