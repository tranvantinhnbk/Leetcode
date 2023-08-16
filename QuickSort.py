arr = [56,22,25,73,1,22]
def QuickSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr 
    pivot = arr[-1]
    left = []
    right = []
    for idx in range(len(arr)-1):
        if arr[idx] < pivot:
            left.append(arr[idx])
        else:
            right.append(arr[idx])
    return QuickSort(left)+[pivot]+QuickSort(right)
print(QuickSort(arr))
    