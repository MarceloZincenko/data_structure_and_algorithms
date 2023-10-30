#977. Squares of a Sorted Array
def sortedSquares(nums):
    res = [0] * len(nums)
    l = 0
    r = len(nums) - 1
    pos = len(nums) - 1

    while l <= r:
        if nums[l]**2 < nums[r]**2:
            res[pos] = nums[r]**2
            r -= 1
        else:
            res[pos] = nums[l]**2
            l += 1
        
        pos -= 1
    
    return res