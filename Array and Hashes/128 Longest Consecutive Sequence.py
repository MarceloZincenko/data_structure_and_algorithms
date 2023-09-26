#128. Longest Consecutive Sequence
def longestConsecutive(nums) -> int:
    
    snums = set(nums)
    ans = 0

    for n in snums:
        if n - 1 in snums:
            continue
        
        k = 1
        while n + k in snums:
            k += 1
            
        ans = max(ans, k)

    return ans