# 268. Missing Number
def missingNumber(nums):
    
    aux = [0] * (len(nums) + 1)

    for n in nums:
        aux[n] = 1
    
    for i in range(len(aux)):
        if aux[i] == 0:
            return i
