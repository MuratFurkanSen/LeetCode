class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        opening = "("
        closing = ")"
        result = ["("]
        while len(result[-1]) < n*2:
            length = len(result)
            for i in range(length):
                openingCount = result[i].count(opening)
                closingCount = result[i].count(closing)
                if openingCount > closingCount:
                    if openingCount < n:
                        result[i] += opening
                        result.append(result[i][:-1]+closing)
                    else:
                        result[i] += closing
                if openingCount == closingCount and openingCount < n:
                    result[i] += opening
        return result
s = Solution()
print(s.generateParenthesis(3))