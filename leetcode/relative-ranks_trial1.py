class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        d = {}

        for i,k in enumerate(s):
            if i == 0 :
                d[k] = "Gold Medal"
            elif i == 1 :
                d[k] = "Silver Medal"
            elif i == 2 :
                d[k] = "Bronze Medal"
            else :
                d[k] = str(i+1)
        
        return [d[x] for x in score]

        


        