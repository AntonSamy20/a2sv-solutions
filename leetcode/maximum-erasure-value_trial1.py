class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        seen = set()
        left = 0
        total = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left+=1
                
            seen.add(nums[right])
            total += nums[right]

            score = max(total, score)

        return score            
                
        

                


        