class Solution:
    def func(self, nums, k ):
        left = 0
        odd = 0
        res = 0
        for right in range(len(nums)):
            odd += nums[right]
            while odd > k: 
                odd -= nums[left]
                left +=1
            res += right - left + 1
        return res

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        return self.func(nums, k) - self.func(nums, k - 1)

