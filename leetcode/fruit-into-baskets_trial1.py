class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        for i in range(len(fruits)):
            baskets[fruits[i]] = baskets.get(fruits[i],0) + 1
        
        target = sorted(baskets.values())

        return sum(target[-2:])

        