#41. First Missing Positive
def firstMissingPositive(nums):
    aux = set(nums)

    for i in range(1,len(nums)+10):
        if i not in aux:
            return i