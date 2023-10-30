def letterCasePermutation(s: str):
    ans = []
    S = s.lower()
    
    def dfs(i, res=''):
        if i >= len(s):
            ans.append(res)
            return
        
        dfs(i+1, res + S[i])
        if S[i].islower(): 
            dfs(i+1, res + S[i].upper())
    
    dfs(0)
    return ans