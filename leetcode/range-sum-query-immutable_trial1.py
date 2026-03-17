class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]* len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            self.prefix[i] = s
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right] 
        return (self.prefix[right] - self.prefix[left-1])

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
