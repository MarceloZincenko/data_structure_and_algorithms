#242 Valid Anagram

def convert_to_hashmap(string):

    res = {}

    for s in string:
        if s in res:
            res[s] += 1
        else:
            res[s] = 1
    
    return res
    
def isAnagram(s: str, t: str) -> bool:
   return convert_to_hashmap(s) == convert_to_hashmap(t)