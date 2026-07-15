class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        best={}
        for i in range(len(nums)):
            if nums[i] not in best:
                best[nums[i]]=1
            else:
                best[nums[i]]+=1
        result=[]
        sorted_keys = sorted(best, key=best.get, reverse=True)
        count=0
        for i in sorted_keys:
            result.append(i)
            count+=1
            if count==k:
                break
        return result