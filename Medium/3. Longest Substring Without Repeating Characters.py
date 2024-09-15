class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLength = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if substring.count(s[j]) != 0:
                    if len(substring) > maxLength:
                        maxLength = len(substring)
                    substring = ""
                    break
                substring += s[j]
        if maxLength == -1:
            maxLength = len(substring)
        return maxLength


solution = Solution()
A = solution.lengthOfLongestSubstring(" ")
print(A)