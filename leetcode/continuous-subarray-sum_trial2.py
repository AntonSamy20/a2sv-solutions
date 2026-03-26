class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0

        reminder = {0:-1}
        for i in range(len(nums)):
            prefix += nums[i]

            r = prefix % k
            if r in reminder:
                if i - reminder[r] >=2:
                    return True
            else :
                reminder[r] = i
        return False
