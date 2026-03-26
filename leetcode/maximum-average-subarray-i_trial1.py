class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        mx = window
        for i in range(k, len(nums)):
            window -= nums[i-k]
            window += nums[i]
            mx = max(window,mx)
        return mx/k
        