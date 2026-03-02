class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        freq = [0] * 3
        for i in nums:
            freq[i]+=1
        
        index = 0
        for color in range(3):
            for _ in range(freq[color]):
                nums[index] = color
                index+=1
        
        