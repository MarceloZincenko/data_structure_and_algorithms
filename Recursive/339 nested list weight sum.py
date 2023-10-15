#339. Nested List Weight Sum
'''
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
'''

def weighted_sum(input, depth):

    suma = 0
    for element in input:
        if isinstance(element, int):
            suma += element * depth
        else:
            suma += weighted_sum(element, depth + 1)
    return suma    

# input = 1 -> 0
# input = [2] -> 2
# input = [1,[2]] -> 2

input = [1,[4,[6]]]
print(weighted_sum(input, 1))