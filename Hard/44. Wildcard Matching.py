class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '*':
            return True

        memo = [[False] * (len(p) + 1)]*(len(s) + 1)
        memo[0][0] = True
        for i in range(0, len(s)):
            for j in range(len(p)):
                if p[j] == "?":
                    memo[i+1][j+1] = memo[i][j]
                elif p[j] == "*":
                    memo[i + 1][j + 1] = memo[i+1][j] or memo[i][j+1]
                elif p[j] == s[i]:
                    memo[i+1][j+1] = memo[i][j]
                else:
                    memo[i+1][j+1] = False
        return memo[-1][-1]
if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("adceb", "*a*b"))