#680. Valid Palindrome II

def validPalindrome(s: str) -> bool:
    mistakes = 0

    def isPalindrome(s):
        nonlocal mistakes
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l] != s[r]:
                if mistakes == 0:
                    mistakes = 1
                    return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
                else:
                    return False
            
            l += 1
            r -= 1

        return True
    
    return isPalindrome(s)    
validPalindrome("abc")