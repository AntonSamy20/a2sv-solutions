class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefix[i] = s
        return prefix
        