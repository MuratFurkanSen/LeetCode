class Solution:
    def intToRoman(self, num: int) -> str:
        nums = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        roman = ""
        i = 1000
        while i >= 1:
            roman += nums[i] * int(num // i)
            num %= i
            if num // (i - (i / 10)) > 0:
                roman += nums[i // 10] + nums[i]
                num %= (i - (i / 10))
            elif num // (i / 2) > 0:
                roman += nums[i // 2]
                num %= (i / 2)
            elif num // (i - (i / 2) - (i / 10)) > 0:
                roman += nums[i // 10] + nums[i//2]
                num %= (i - (i / 2) - (i / 10))
            i /= 10 
        return roman

