#1. Two Sum
def twoSum(nums, target):
    
    diff_pos = {} 

    for i, n in enumerate(nums):
        if n in diff_pos:
            return [diff_pos[n], i]
        diff_pos[target - n] = i