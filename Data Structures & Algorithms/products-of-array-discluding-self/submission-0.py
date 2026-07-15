class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k=nums.count(0)
        if k>1:
            return [0]*(len(nums))
        elif k==1:
            product=1
            for i in range(len(nums)):
                if nums[i]!=0:
                    product*=nums[i]
            index=nums.index(0)
            nums=[0]*len(nums)
            nums[index]=product
            return nums
        product=1
        for i in range(len(nums)):
            product*=nums[i]
        for i in range(len(nums)):
            nums[i]=product//nums[i]
        return nums


        