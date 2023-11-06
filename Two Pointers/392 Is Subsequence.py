#392. Is Subsequence
def isSubsequence(s: str, t: str) -> bool:
    
    ls, lt = 0, 0

    while ls < len(s) and lt < len(t):

        if t[lt] == s[ls]:
            ls += 1
        lt += 1
    
    return ls == len(s)