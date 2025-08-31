class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            abs_num = abs(nums[i])
            index = abs_num -1
            if 0 <= index < n:
                if nums[index] == 0:
                    nums[index] = (n+1)*-1
                elif nums[index] > 0:
                    nums[index] *= -1
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1
