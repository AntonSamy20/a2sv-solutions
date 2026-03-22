class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        nums.sort()

        c = 0
        while i<j:
            v = nums[i] + nums[j]
            if v < target:
                c += (j-i)
                i+=1
            else:
                j-=1
        return c