class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = ""
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1):
                if s[j:i+j] == s[j:i+j][::-1] and len(max) < len(s[j:i+j]):
                    max = s[j:i+j]
        return max


sol = Solution()
A = sol.longestPalindrome("abaa")
print(A)