class Solution:
    def isValid(self, s: str) -> bool:
        pair={']':'[','}':'{',')':'('}
        s=list(s)
        stack=[]
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1]!=pair[s[i]]:
                    return False
                stack.pop()
        if stack:
            return False
        else:
            return True
        
        