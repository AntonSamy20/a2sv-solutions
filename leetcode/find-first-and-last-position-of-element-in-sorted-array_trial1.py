class Solution:
    def binarySearch(self, nums: List[int], target: int, direction: str):
        
        low = 0
        high = len(nums) - 1
        output = -1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target: 
                high = mid - 1
            else:
                output = mid
                if direction=="right":
                    low = mid + 1
                else :
                    high = mid - 1
            
        return output 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums, target, 'left')
        last = self.binarySearch(nums, target, 'right')

        return [first, last]