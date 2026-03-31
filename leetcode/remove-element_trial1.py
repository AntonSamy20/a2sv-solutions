class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i<=j:
            if nums[j]!=val:
                if nums[i]!=val:
                    i+=1
                else :
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                    j-=1
            else :
                j-=1
        return len(nums) - nums.count(val)
        