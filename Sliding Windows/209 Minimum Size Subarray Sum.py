#209. Minimum Size Subarray Sum

def minSubArrayLen(target, nums):
    
    res = float('inf')
    cumSum = 0
    l = 0 
    
    for r in range(len(nums)):
        
        cumSum += nums[r]
        
        while cumSum >= target:
            res = min(res, r - l + 1)
            cumSum -= nums[l]
            l += 1
                
    return 0 if res == float('inf') else res

nums = [1,2,3,4,5]
target = 11
minSubArrayLen(target, nums)
