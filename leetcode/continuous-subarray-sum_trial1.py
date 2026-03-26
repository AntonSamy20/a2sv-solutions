class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        x = y = 0
        tot = sum(nums[:2])
        

        for i in range(n):
            x += nums[i]
            prefix[i] = x
            if i!=0 and prefix[i]%k==0:
                return True
        for i in range(n-1,-1,-1):
            y += nums[i]
            if i!=0 and suffix[i]%k==0:
                return True
        return False

        # for i in range(1,n):
        #     left = i+1
        #     right = n-1

        #     while left<right:
        #         if tot%6==0:
        #             return true 
        #         else:
        #             tot+=nums[left]
        #             left+=1
            

        