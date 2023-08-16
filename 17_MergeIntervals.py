intervals = [[1,4],[0,4]]
sorted_intervals = sorted(intervals, key = lambda x: (x[0], x[1]))

output = [sorted_intervals[0]]
for val in sorted_intervals:
    last_interval = output[-1]
    if last_interval[1] >= val[0]:
        output[-1][1] = max(last_interval[1], val[1])
    else:
        output.append(val)
print(output)

