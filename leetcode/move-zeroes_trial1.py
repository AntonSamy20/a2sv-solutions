class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        digit = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[digit] = nums[digit],nums[i]
                digit +=1
            
            
        