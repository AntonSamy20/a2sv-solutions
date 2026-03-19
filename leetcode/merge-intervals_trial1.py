class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lst = [intervals[0]]

        for i in range(1,len(intervals)):
            curr = intervals[i]
            last = lst[-1]
            if last[1] >= curr[0]:
                last[1] = max(last[1], curr[1])
            else :
                lst.append(curr)
    
        return lst
                    
        