s = "abcabcbb"
memo = set()

i = 0
j = 0
res = 0
while j < len(s):
    if s[j] not in memo:
        memo.add(s[j])
        j+=1
    else:
        res = max(res, j-i)
        while s[i]!=s[j]:
            memo.remove(s[i])
            i+=1
        i+=1
        j+=1
res = max(res, j-i)
print(res)
