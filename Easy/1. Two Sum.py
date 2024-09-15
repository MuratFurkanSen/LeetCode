class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        searchList = nums.copy()
        if target > 0:
            searchList.sort()
        else:
            searchList.sort(reverse=True)
        for i in range(len(searchList)):
            if target > 0:
                if target > searchList[i] + searchList[-1]:
                    continue
                if target < searchList[i] + searchList[0]:
                    continue
            else:
                if target > searchList[i] + searchList[0]:
                    continue
                if target < searchList[i] + searchList[-1]:
                    continue
            for j in range(i + 1, len(searchList)):
                if searchList[i] + searchList[j] == target:
                    first = nums.index(searchList[i])
                    nums[first] = target+1 if target > 0 else target-1
                    second = nums.index(searchList[j])
                    result = [first, second]
                    result.sort()
                    return result