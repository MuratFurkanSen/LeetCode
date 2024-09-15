class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0

        if divisor == 0:
            return None
        if dividend == 0:
            return 0
        resultSign = "+"
        if dividend > 0 > divisor or dividend < 0 < divisor:
            resultSign = "-"

        dividend = abs(dividend)
        divisor = abs(divisor)
        listDividend = list(str(dividend))
        quotient = list()
        currentLength = 0
        currSubStr = ""
        for i in listDividend:
            currSubStr += i
            currSubInt = int(currSubStr)
            if currSubInt >= divisor:
                currQuotient, remainder = self.subDivide(currSubInt, divisor)
                quotient.append(str(currQuotient))
                currSubStr = ""
                if remainder != 0: currSubStr += str(remainder)
            else:
                quotient.append("0")
        quotient = int("".join(quotient))
        quotient = -quotient if resultSign == "-" else quotient
        if quotient < -(2 ** 31): quotient = -(2 ** 31)
        if quotient > (2 ** 31) - 1: quotient = (2 ** 31) - 1
        return quotient

    def subDivide(self, dividend: int, divisor: int) -> (int, int):
        quotient = 0
        while dividend - divisor >= 0:
            quotient += 1
            dividend -= divisor
        return quotient, dividend

s = Solution()
print(s.divide(2147483647, 2))