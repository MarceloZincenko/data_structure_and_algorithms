#77. Combinations
'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''
def combine(n: int, k: int):
    res = []
    subset = []
    nums = range(1,n+1)

    def dfs(i):
        if i >= len(nums):
            if len(subset) == k:
                res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)        


    dfs(0)
    return res

def combine2(self, n: int, k: int):
    res = []
    def helper(start, comb):
        
        if len(comb) == k:
            res.append(comb.copy())
            return
        
        for i in range(start, n+1):
            comb.append(i)
            helper(i+1, comb)
            comb.pop()

    helper(1, [])
    return res