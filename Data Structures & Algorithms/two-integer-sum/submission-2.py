class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums[:]   # copy original list

        nums.sort()

        low = 0
        high = len(nums) - 1

        while low < high:
            s = nums[low] + nums[high]

            if s > target:
                high -= 1

            elif s < target:
                low += 1

            else:
                a = nums[low]
                b = nums[high]
                break

        if a == b:
            first = temp.index(a)
            second = temp.index(b, first + 1)
            return [first, second]

        idx1 = temp.index(a)
        idx2 = temp.index(b)
        return sorted([idx1, idx2])