#49. Group Anagrams
import collections

def create_id(string):
    count = [0] * 26

    for s in string:
        count[ord(s) - ord("a")] += 1
    
    return tuple(count)

def groupAnagrams(strs):

    id_strs = collections.defaultdict(list)
    
    for string in strs:
        id_strs[create_id(string)].append(string)
    
    return id_strs.values()