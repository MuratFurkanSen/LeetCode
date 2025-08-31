class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(i) for i in num1]
        num2 = [int(i) for i in num2]
        carry = 0
        result = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num2)):
            curr_num2 = num2[len(num2) - i - 1]
            for j in range(len(num1)):
                curr_num1 = num1[len(num1) - j - 1]
                num = result[i + j] + (curr_num1 * curr_num2) + carry
                result[i + j] = num % 10
                carry = num // 10
            result[i + len(num1)] += carry
            carry = 0
        result = result[::-1]
        for i in range(len(result)):
            if result[i] != 0:
                result = result[i:]
                break
        else:
            result = [0]
        result = map(str, result)
        return "".join(result)

if __name__ == '__main__':
    s = Solution()
    print(s.multiply("123","456"))
