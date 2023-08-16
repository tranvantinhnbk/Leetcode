height = [1,8,6,2,5,4,8,3,7]

i = 0
j = len(height) - 1
m = 0
while i<j:
    if m < (j-i)*min(height[i], height[j]):
        m = (j-i)*min(height[i], height[j])
    if height[i] < height[j]:
        i+=1
    else:
        j-=1
print(m)


