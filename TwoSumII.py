j = len(numbers) - 1
for i in range(len(numbers)):
    if i >= j:
        break
    if numbers[i] + numbers[j] > target:
        j-=1
    if numbers[i] + numbers[j] == target:
        return [i+1, j+1]
return []
            