class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        wndw=[]
        count=0
        maxcount=0
        for i in range(len(s)):
            while s[i] in wndw:
                wndw.pop(0)
                left+=1
                count-=1

            wndw.append(s[i])
            count+=1
            maxcount=max(maxcount,count)
        return maxcount
        
        