class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        Min=float('inf')
        while low<=high:
            mid=(low+high)//2
            Min=min(Min,nums[mid])
            if nums[high]<=nums[mid]:
                low=mid+1
            else:
                high=mid
        return Min

        