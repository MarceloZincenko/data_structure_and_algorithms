#844. Backspace String Compare
def backspaceCompare(s: str, t: str) -> bool:
    rs, rt = len(s) - 1, len(t) - 1
    count_s = 0
    count_t = 0

    while rs >= 0 and rt >= 0:
        
        if s[rs] == '#':
            count_s += 1
            rs -= 1
            continue

        if count_s > 0:
            count_s -= 1
            rs -= 1
            continue
        
        if t[rt] == '#':
            count_t += 1
            rt -= 1
            continue

        if count_t > 0:
            count_t -= 1
            rt -= 1
            continue
        
        if s[rs] != t[rt]:
            return False
        
        rs -= 1
        rt -= 1

    if rt >= 0:
        while rt >= 0:    
            if t[rt] == '#':
                count_t += 1
                rt -= 1
                continue

            if count_t > 0:
                count_t -= 1
                rt -= 1
                continue
            
            return False

    if rs >= 0:
        while rs >= 0:    
            if s[rs] == '#':
                count_s += 1
                rs -= 1
                continue

            if count_s > 0:
                count_s -= 1
                rs -= 1
                continue
            
            return False
    return True