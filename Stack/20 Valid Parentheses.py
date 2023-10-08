#20. Valid Parentheses
def isValid(s: str) -> bool:
    
    stack = []

    pairs = {}
    pairs[')'] = '('
    pairs['}'] = '{'
    pairs[']'] = '[' 

    for l in s:
        if l not in pairs:
            stack.append(l)
            continue
        else:
            if stack:
                last = stack.pop()
                if last != pairs[l]:
                    return False
            else:
                return False

    return stack == []