class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for i in s:
            if i in parMap.values():
                stack.append(i)
            if i in parMap.keys():
                if len(stack) == 0:
                    return False
                if parMap[i] != stack.pop():
                    return False
        return len(stack) == 0
