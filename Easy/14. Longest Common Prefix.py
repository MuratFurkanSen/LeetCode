class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        first = strs[0]
        index = 0
        while index < len(first):
            for s in strs[1:]:
                if not (index < len(s) and s[index] == first[index]):
                    return prefix
            prefix += first[index]
            index += 1
        return prefix
