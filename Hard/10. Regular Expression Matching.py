class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        if "**" in p:
            p  = p.replace("**", "")
        match = re.match(p, s)
        if match:
            return match.group(0) == s
        else:
            return False


sol = Solution()
print(sol.isMatch("abc", "a***abc"))
