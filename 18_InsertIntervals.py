intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
res = []

for (i, interval) in enumerate(intervals):
    if newInterval[1] < interval[0]:
        res += ([newInterval] + intervals[i:])
        break
    elif newInterval[0] > interval[1]:
        res.append(interval)
    else:
        newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
print(res)





    



        
    



