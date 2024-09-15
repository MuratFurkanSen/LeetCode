class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letterMap = {"1": "", "2": "abc", "3": "def",
                     "4": "ghi", "5": "jkl", "6": "mno",
                     "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = list()
        if len(digits) == 0:
            return result
        count = 1
        for digit in digits[1:]:
            count *= len(letterMap[digit])
        firstDigit = digits[0]
        for i in letterMap[firstDigit]:
            for __ in range(count):
                result.append(i)

        for i in range(1, len(digits)):
            letters = letterMap[digits[i]]
            letterCount = len(letters)
            stepSize = 1
            for digit in digits[i+1:]:
                stepSize *= len(letterMap[digit])
            indexStart = 0
            for letter in letters:
                currentIndex = indexStart
                for __ in range((len(result)//letterCount) // stepSize):
                    for j in range(stepSize):
                        result[currentIndex] += letter
                        currentIndex += 1
                    currentIndex += stepSize*(letterCount-1)
                indexStart += stepSize
        return result

s = Solution()
print(s.letterCombinations("999"))