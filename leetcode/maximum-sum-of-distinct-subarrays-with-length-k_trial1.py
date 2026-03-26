class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = sum(nums[:k])
        mx = window if len(set(nums[:k])) == k else 0

        for i in range(k,len(nums)):
            if len(set(nums[i:i+k])) == k:
                mx = max(mx, window)
            window += nums[i]
            window -= nums[i-k]

        return mx 