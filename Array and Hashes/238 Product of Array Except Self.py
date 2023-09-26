#238. Product of Array Except Self
def productExceptSelf(nums):
    l, r = 1, 1
    len_n = len(nums)

    if len_n == 0 or nums is None:
        return nums

    ans = [1] * len_n
    
    for i in range(0, len_n):
        ans[i] *= l
        l *= nums[i]
        ans[len_n - i - 1] *= r
        r *= nums[len_n - i - 1]
    
    return ans
