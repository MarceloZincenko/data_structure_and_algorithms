'''
Remove ocurrences
nested_list = [1, [2, 3, 2], [4, [5, 2, 6]], 2]
target = 2
[1, [3], [4, [5, 6]]]
'''

'''
target = 2
[] -> []
[1 ,2 ,3] -> [1,3]
[1 ,[2 ,3]] -> [1,[3]]

'''

def remove_ocurrences(nums, target):
    res = []

    for element in nums:
        if isinstance(element, int):
            if element != target:
                res.append(element)
        else:
            res.append(remove_ocurrences(element, target))  

    return res

target = 2
# [] -> []
# [1 ,2 ,3] -> [1,3]
# [1 ,[2 ,3]] -> [1,[3]]
nums = [1 ,[2 ,3], [2]]
print(remove_ocurrences(nums, target))