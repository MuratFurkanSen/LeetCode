class Solution:
    # Recursive
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = self.countAndSay(n - 1)
        new_result = ""
        last_int = result[0]
        count = 0
        for j in result:
            if j != last_int:
                new_result += str(count) + last_int
                count = 0
            last_int = j
            count += 1
        new_result += str(count) + last_int
        result = new_result
        return result

    # Iterative
    def countAndSayIterative(self, n: int) -> str:
        result = "1"
        for i in range(n - 1):
            new_result = ""
            count = 0
            last_int = result[0]
            for j in result:
                if j != last_int:
                    new_result += str(count) + last_int
                    count = 0
                last_int = j
                count += 1
            new_result += str(count) + last_int
            result = new_result
        return result
