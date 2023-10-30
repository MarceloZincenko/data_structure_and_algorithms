#Maximum Holidays
# input = ['H', 'W', 'W', 'H', 'W', 'H', 'H']
# take off = 2

def holidays(calendar, k):

    res = 0
    count = 0
    l = 0

    for r in range(len(calendar)):

        if calendar[r] == "W":
            count += 1
        
        res = max(res, r - l)

        while count > k:
            if calendar[l] == "W":
                count -= 1
            l += 1

    return res + 1 if calendar[-1] == "H" else res

print(holidays(['H', 'W', 'W', 'H', 'W', 'H', 'W'], 2))
