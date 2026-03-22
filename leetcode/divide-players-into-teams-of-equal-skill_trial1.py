class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        teams = n//2
        total = sum(skill)

        if total % teams != 0:
            return -1

        target = total // teams
        skill.sort()

        i = 0
        j = n - 1
        chemistry = 0

        while i<j:
            if skill[i] + skill[j] != target:
                return -1
            chemistry += skill[i] * skill[j]
            i+=1
            j-=1
        return chemistry



        