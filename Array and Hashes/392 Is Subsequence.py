#392. Is Subsequence
def isSubsequence(s: str, t: str) :
    ls = 0
    lt = 0

    while ls < len(s) and lt < len(t):
        if s[ls] == t[lt]:
            ls += 1
        lt += 1
        
    return ls == len(s)