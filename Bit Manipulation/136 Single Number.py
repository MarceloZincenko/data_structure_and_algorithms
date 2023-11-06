#136. Single Number
def singleNumber(nums) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    
    return xor

singleNumber([4,1,2,1,2])