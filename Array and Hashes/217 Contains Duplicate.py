#217. Contains Duplicate
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


def containsDuplicate2(nums):
    visited = set()

    for n in nums:
        if n in visited:
            return True
        visited.add(n)
    
    return False