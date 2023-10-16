#90. Subsets II
'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

'''
def subsetsWithDup(nums):
    nums.sort()
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        # All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i+1)


    dfs(0)
    return res