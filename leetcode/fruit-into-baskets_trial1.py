class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mx = 0
        left = 0

        seen = {}
        for i in range(n): 
            seen[fruits[i]] = seen.get(fruits[i], 0) + 1

            while len(seen) > 2:
                seen[fruits[left]]-=1
                if seen[fruits[left]]==0:
                    del seen[fruits[left]]
                left+=1
            mx = max(mx, i-left+1)

        return mx    