#39. Combination Sum
'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
'''   
def combinationSum(candidates, target):
    res = []
    subset = []

    def dfs(i):
        if i >= len(candidates):
            if sum(subset) == target:
                res.append(subset.copy())
            return
        
        # consider the candidate
        subset.append(candidates[i])
        dfs(i+1)

        # not consider the candidate
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res

combinationSum([2,3,6,7], 7)

'''
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.
'''
def combinationSum2(candidates, target):
        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            dfs(i, total + candidates[i])
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res

combinationSum2([2,3,6,7], 7)
