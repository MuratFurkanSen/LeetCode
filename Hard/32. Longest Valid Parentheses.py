class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                if len(stack) != 0:
                    stack.pop()
                    res = max(res, index - stack[-1])
        return res


sol = Solution()
print(sol.longestValidParentheses("(()(())"))
