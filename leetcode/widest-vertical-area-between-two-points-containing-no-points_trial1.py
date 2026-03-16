class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = []
        for p in points:
            width.append(p[0])
        width.sort()
        mx = 0
        for i in range(len(width)-1):
            if width[i+1] - width[i] >mx:
                mx = width[i+1] - width[i]
        return mx


        