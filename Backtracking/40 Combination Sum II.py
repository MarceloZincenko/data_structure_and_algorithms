#40. Combination Sum II

def combinationSum2(candidates, target):
    res = []
    subset = []
    candidates.sort()
    def dfs(i, total):
        if total == target:
            res.append(subset.copy())
            return
        if i >= len(candidates) or total > target:
            return

        subset.append(candidates[i])
        dfs(i+1,  total + candidates[i])
        subset.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        dfs(i+1, total)

    dfs(0, 0)
    return res

target = 27
input = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
print(combinationSum2(input, target))
