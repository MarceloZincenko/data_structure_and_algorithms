#881. Boats to Save People
def numRescueBoats(people, limit):
    people.sort()
    l, r = 0, len(people) -1
    count = 0

    while l < r:
        if people[l] + people[r] > limit:
            count += 1
            r -= 1
        else:
            count += 1
            l += 1
            r -= 1
        
    if l == r:
        count += 1
    
    return count