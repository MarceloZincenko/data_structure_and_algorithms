# 169. Majority Element
def majorityElement(nums):
    count = 0
    candidate = nums[0]

    for n in nums:
        if count == 0:
            candidate = n
        
        if n == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate