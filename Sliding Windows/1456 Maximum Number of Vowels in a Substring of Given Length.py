# 1456. Maximum Number of Vowels in a Substring of Given Length
def maxVowels(s: str, k: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    l = 0
    res = 0
    numVowels = 0

    for r in range(len(s)):
        
        if s[r] in vowels:
            numVowels += 1

        if r - l + 1 == k:
            res = max(res, numVowels)
            if s[l] in vowels:
                numVowels -= 1
            l += 1
                    
    return res