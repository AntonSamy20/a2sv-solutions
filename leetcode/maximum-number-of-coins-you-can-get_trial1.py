class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        tot = 0
        c = len(piles)//3
        i = 0
        for _ in range(c):
            i-=2
            tot+=piles[i]
            
        return tot
        