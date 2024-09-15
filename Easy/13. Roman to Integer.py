class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        num = 0
        while i < len(s):
            if i < len(s) -1 and nums[s[i]] < nums[s[i + 1]]:
                num -= nums[s[i]]
                num += nums[s[i + 1]]
                i += 2
            else:
                num += nums[s[i]]
                i += 1

        return num

