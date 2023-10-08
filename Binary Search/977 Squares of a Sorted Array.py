#977 Squares of a Sorted Array

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
def sortedSquares(nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            res[r - l] = left * left
            l += 1
        else:
            res[r - l] = right * right
            r -= 1
    return res