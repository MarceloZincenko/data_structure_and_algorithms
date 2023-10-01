def removeDuplicates(nums):
        l, r = 1, 1
        
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

removeDuplicates([1,1,2])