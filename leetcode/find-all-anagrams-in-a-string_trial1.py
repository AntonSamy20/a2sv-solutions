class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p = sorted(p)
        lst = []
        for i in range(len(s)-n+1):
            if sorted(s[i:i+n])==p:
                lst.append(i)
        return lst


        