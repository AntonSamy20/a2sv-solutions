class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        n = len(word)
        ans = 0

        for left in range(n):
            seen = set()
            
            for right in range(left, n):
                if word[right] not in vowels:
                    break
               
                seen.add(word[right])
                
                if len(seen) == 5:
                    ans += 1
        return ans