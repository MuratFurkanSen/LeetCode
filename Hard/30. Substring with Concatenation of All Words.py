class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if len(words) == 0:
            return []
        length = len(words[0])
        checkLength = length
        if length != 1:
            for word in words:
                for i in word:
                    if word.count(i) == checkLength:
                        checkLength -= word.count(i)-1
        concatStrLength = len(words) * length
        result = list()
        firstWordLastMatch = ""
        i = 0
        lengthSinceLastMatch = 0
        while i <= len(s) - concatStrLength:
            sub = s[i:i + concatStrLength]
            foundList = list()
            isSubMatch = True
            lastWordSub = sub[concatStrLength - length:concatStrLength]
            if lengthSinceLastMatch == length and firstWordLastMatch == lastWordSub:
                lengthSinceLastMatch = 0
                firstWordLastMatch = sub[:length]
                result.append(i)
                i += checkLength
                lengthSinceLastMatch += checkLength
                continue
            for j in range(0, len(sub), length):
                isWordMatch = False
                for word in words:
                    if sub[j:j + length] == word and foundList.count(word) < words.count(word):
                        foundList.append(word)
                        isWordMatch = True
                        break
                if not isWordMatch:
                    isSubMatch = False
                    break
            if isSubMatch:
                lengthSinceLastMatch = 0
                firstWordLastMatch = sub[:length]
                result.append(i)
                i += checkLength
                lengthSinceLastMatch += checkLength
            else:
                firstWordLastMatch = ""
                i += 1
                lengthSinceLastMatch += 1
        return result


sol = Solution()
s = "abaababbaba"
words = ["ba", "ab", "ab"]

print(sol.findSubstring(s, words))  #
