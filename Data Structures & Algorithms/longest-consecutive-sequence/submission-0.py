class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=set(nums)
        maxcount=0
        count=0
        for i in nums:
            if i-1 not in nums:
                curr=i
                count=1
                while curr+1 in nums:
                    count+=1
                    curr+=1
                maxcount=max(maxcount,count)
        return maxcount