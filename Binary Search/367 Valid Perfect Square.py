# 367. Valid Perfect Square
'''
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
'''
def isPerfectSquare(num: int) -> bool:
    for i in range(1, num+1):
        if i * i == num:
            return True
        if i* i > num:
            return False
    
    
    
def isPerfectSquare_2(num: int) -> bool:
    l ,r = 1, num
    while l <= r:
        mid = (l +r) // 2
        if mid * mid > num:
            r = mid - 1
        elif mid * mid < num:
            l = mid + 1
        else:
            return True
    return False