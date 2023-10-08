#2390. Removing Stars From a String
def removeStars(s: str) -> str:
    
    stack = []

    for letter in s:
        if stack and letter == '*':
            stack.pop()
        else:
            stack.append(letter)
    
    return "".join(stack)