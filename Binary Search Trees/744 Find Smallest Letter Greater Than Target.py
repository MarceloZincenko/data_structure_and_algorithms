#744. Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, target):
    if target < letters[0] or target == "z":
        return letters[0]

    l = 0
    r = len(letters) - 1
    index = -1

    while l <= r:

        mid = l + (r - l) // 2

        if letters[mid] > target:
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return letters[index] if index > -1 else letters[0]


nextGreatestLetter(["c","f","j"],"d")