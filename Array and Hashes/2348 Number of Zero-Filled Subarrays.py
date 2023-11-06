def zeroFilledSubarray(nums):
    i, res = 0, 0

    while i < len(nums):
        if nums[i] == 0:
            count = 0
            while i < len(nums) and nums[i] == 0:
                count += 1
                i += 1
                res += count
        i += 1
    
    return res
