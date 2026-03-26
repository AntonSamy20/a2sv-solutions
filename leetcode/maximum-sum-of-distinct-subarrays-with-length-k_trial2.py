class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = sum(nums[:k])
        mx = window if len(set(nums[:k])) == k else 0

        for i in range(k,len(nums)):
            window += nums[i]
            window -= nums[i-k]
            
            if len(set(nums[i-k+1:i+1])) == k:
                mx = max(mx, window)

        return mx 