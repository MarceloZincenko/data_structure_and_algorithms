# 448. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    aux = [0] * (len(nums) + 1)

    for n in nums:
        aux[n] = 1
    
    res = []
    i = 1
    while i < len(aux):
        if aux[i] == 0:
            res.append(i)
        i += 1

    return res