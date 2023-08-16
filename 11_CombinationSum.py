candidates = [2,3,6,7]
target = 7

def dfs(sum, i, list):
    if sum < 0:
        return []
    elif sum == 0:
        return [list]
    else:
        if i == len(candidates):
            return []
        else:
            return dfs(sum-candidates[i], i, list+[candidates[i]]) + dfs(sum, i+1, list)

print(dfs(target, 0, []))