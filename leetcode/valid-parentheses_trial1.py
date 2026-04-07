class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(',
                    '}':'{',
                    ']':'['}

        opened = {'(', '{', '['}
        stack = []

        for i in range(len(s)):
            if s[i] in opened:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1] != bracket[s[i]]:
                    return False
                else :
                    stack.pop()

        return len(stack)==0


        