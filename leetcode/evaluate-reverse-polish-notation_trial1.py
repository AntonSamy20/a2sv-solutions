class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = { '+', '-', '*' , '/'}
        for i in tokens:
            if i not in operators:
                stack.append(i)
            elif stack:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))

        return int(stack[0])