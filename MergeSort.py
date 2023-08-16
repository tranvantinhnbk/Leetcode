arr  = [56,22,25,73,1,22]
def Merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i < len(left):
        res.append(left[i])
        i+=1
    while j < len(right):
        res.append(right[j])
        j+=1
    return res
def MergeSort(arr):
    if len(arr) <=1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    return Merge(MergeSort(left),MergeSort(right))
print(MergeSort(arr))