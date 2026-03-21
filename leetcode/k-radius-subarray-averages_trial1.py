class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        
        size = 2 * k + 1
        if size > n:
            return avgs

        total = sum(nums[:size])
        avgs[k] = total//size

        for i in range(size,n):
            total -= nums[i-size]
            total += nums[i]
            c = i -k
            avgs[c] = total//size
        return avgs




        