def hasAllCodes(s: str, k: int) -> bool:
    
    combinations = set()
    for i in range(k, len(s)+1):
        print(f"{i-k}{i}")
        current =  s[i-k:i]
        if current not in combinations:
            combinations.add(current)
    
    return len(combinations) == 2 ** k

print(hasAllCodes("00110",2))