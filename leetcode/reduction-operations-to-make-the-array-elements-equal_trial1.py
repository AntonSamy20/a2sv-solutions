class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = 0
        operation = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                c+=1
            operation+=c
        return operation
            
        