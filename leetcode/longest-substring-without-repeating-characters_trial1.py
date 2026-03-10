class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        ans = 0

        for r, c in enumerate(s):
            while c in chars:
                chars.remove(s[l])
                l += 1

            chars.add(c)
            ans = max(ans, r - l + 1)

        return ans