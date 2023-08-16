strs = ["eat","tea","tan","ate","nat","bat"]
res = {}
for s in strs:
    count=[0]*26
    for c in s:
        count[ord(c)-ord('a')]+=1
    if tuple(count) not in res:
        res[tuple(count)] = [s]
    else:
        res[tuple(count)] += [s]
result = []
for key in res:
    result.append(res[key])
print(result)