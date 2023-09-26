def encode(strs):
    # write your code here
    ans = []
    for s in strs:
        ans.append(f'{len(s)}#{s}')
    return ''.join(ans)

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    # write your code here
    ans = []

    if str:
        n = int(str[0])
    
    l = 1
    while l<len(str):

        if str[l] == "#":
            ans.append(str[(l + 1):(l+1+n)])
            l = l+1+n+1
        else:
            n = int(str[l])
            l += 1

    return ans

input = ["lint","code","love","you"]
print(encode(input))
print(decode(encode(input)))

