class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sing = abs(x)/x
        num = int(str(abs(x))[::-1])
        if num > 2**31-1:
            return 0
        return int(num*sing)
