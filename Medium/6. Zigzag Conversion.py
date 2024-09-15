class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = numRows + (numRows - 2)
        if numRows == 1:
            return s
        Top = s[::step]
        Bottom = s[numRows - 1::step]
        middle = list()
        for i in range(1, numRows - 1):
            B = s[i::step]
            C = s[numRows * 2 - 2 - i::step]
            E = [i + j for i, j in zip(B, C)]
            if len(B) > len(C):
                E += B[-1]
            middle.append("".join(E))
        result = Top + "".join(middle) + Bottom
        return result


s = Solution()
print(s.convert("PAYPALISHIRING", 4))

"""
P   A   H   N
A P L S I I G
Y   I   R

P     I    N
A   L S  I G
Y A   H R
P     I
"""
