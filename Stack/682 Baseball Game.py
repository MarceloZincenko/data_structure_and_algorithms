# 682. Baseball Game
def calPoints(operations):
    
    stack = []

    for e in operations:
        if e == '+':
            tmp = stack[-2:]
            stack.append(sum(tmp))
        elif e == 'D':
            tmp = stack[-1]
            stack.append(tmp * 2)
        elif e == 'C':
            stack.pop()
        else:
            stack.append(int(e))
        
    return sum(stack)