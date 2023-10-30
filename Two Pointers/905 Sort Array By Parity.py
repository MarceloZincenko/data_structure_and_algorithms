#905. Sort Array By Parity
def sortArrayByParity(nums):
    l = 0
    while l < len(nums) and nums[l] % 2 == 0:
        l += 1

    r = l + 1    

    while r < len(nums):

        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]

        if nums[l] % 2 == 0:
            l += 1
            
        r += 1
        
    return nums
