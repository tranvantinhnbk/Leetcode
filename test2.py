A = [1,2,3,4,5]
occ = {}
for num in A:
    if num not in occ: 
        occ[num] = 1 
    else:
        occ[num] += 1
occ_list = list(occ.values())
occ_list = sorted(occ_list, reverse=True)
unique = set()
print(occ_list)
res = 0
for i in range(len(occ_list)):
    while occ_list[i] in unique:
        occ_list[i] -=1 
        res+=1
        if occ_list[i] == 0:
            break
    if occ_list[i] != 0:
        unique.add(occ_list[i])
print(res)

