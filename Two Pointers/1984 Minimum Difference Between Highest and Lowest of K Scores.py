#1984. Minimum Difference Between Highest and Lowest of K Scores

def minimumDifference(nums, k):
    nums.sort()
    l, r = 0, k-1
    ans = float('inf')

    while r < len(nums):
        ans = min(ans, nums[r] - nums[l])
        l += 1
        r += 1
    
    return ans if len(nums) > 1 and ans != float('inf') else 0