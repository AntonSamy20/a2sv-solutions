class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        size = len(temperatures)
        ans = [0] * size

        for i in range(size):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans
        