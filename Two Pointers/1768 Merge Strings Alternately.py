#1768. Merge Strings Alternately
def mergeAlternately(word1: str, word2: str) -> str:
    l1, l2 = 0, 0
    ans = []

    while l1 < len(word1) and l2 < len(word2):
        ans.append(word1[l1])
        ans.append(word2[l2])
        l1 += 1
        l2 += 1

    while l1 < len(word1):
        ans.append(word1[l1])
        l1 += 1
    
    while l2 < len(word2):
        ans.append(word2[l2])
        l2 += 1
    
    return "".join(ans)
