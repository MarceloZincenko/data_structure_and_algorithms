# 953. Verifying an Alien Dictionary

def isAlienSorted(words, order):
    orderInd = { c : i for i, c in enumerate(order)} #letter:order
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1] #compare two word per time
        
        for j in range(len(w1)):
            if j == len(w2):
                return False
            
            if w1[j] != w2[j]:
                if orderInd[w2[j]] < orderInd[w1[j]]:
                    return False
                break # the order it is ok
    return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))