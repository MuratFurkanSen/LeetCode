class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = len(nums)
        i = 1
        index = 1
        while index < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                k -= 1
                i += 1
            if i < len(nums):
                nums[index] = nums[i]
            else:
                break
            index += 1
            i += 1
        return k


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
