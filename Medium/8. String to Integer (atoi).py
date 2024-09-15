class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        if len(s) == 0: return 0
        sign = s[0]
        startIndex = 0
        try:
            int(sign)
            sign = 1
        except ValueError:
            startIndex = 1 if sign == "+" or sign == "-" else 0
            sign = 1 if sign == "+" else -1
        for i in range(startIndex, len(s)):
            try:
                int(s[i])
            except ValueError:
                if i == startIndex:
                    return 0
                num = int(int(s[startIndex:i]) * sign)
                return num if abs(num) <= 2 ** 31 - 1 else (-(2 ** 31) if sign == -1 else (2 ** 31-1))
        try:
            int(s)
        except ValueError:
            return 0
        num = int(int(s[startIndex:]) * sign)
        return num if abs(num) <= 2 ** 31 - 1 else (-(2 ** 31) if sign == -1 else (2 ** 31-1))


s = Solution()
print(s.myAtoi("   -042"))
