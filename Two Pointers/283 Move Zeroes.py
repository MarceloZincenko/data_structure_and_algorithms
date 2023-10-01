def moveZeroes(nums):
    l, r = 0, 0
    while r < len (nums):
        
        if  nums[l] == 0 and nums[r] != 0:
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp

        if nums[l] != 0:
            l += 1
        
        r += 1