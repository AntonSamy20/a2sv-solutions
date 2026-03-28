class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = { 'a', 'e', 'i', 'o', 'u'}
        count = 0
        mx = 0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        mx = count
        for i in range(k, len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k] in vowel:
                count-=1

            mx = max(count, mx)


        return mx

        