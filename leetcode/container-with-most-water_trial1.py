class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mx = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            mx = max(mx, h*w)

            if height[left] > height[right]:
                right -=1
            else :
                left +=1


        return mx

        
        