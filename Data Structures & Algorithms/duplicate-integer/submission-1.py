class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr={}
        for i in nums:
            if i not in arr:
                arr[i]=1
            else:
                return True
        return False