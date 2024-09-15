class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums = list(enumerate(nums))
        last = None
        while len(nums) > 0:
            last = nums[0] if nums[0][1] > target else nums[-1]
            middle = len(nums) // 2
            index, val = nums[middle][0], nums[middle][1]
            if val > target:
                nums = nums[:middle]
            elif val < target:
                nums = nums[middle + 1:]
            else:
                return index

        if last[1] > target:
            return last[0]
        else:
            return last[0] + 1


sol = Solution()
print(sol.searchInsert(nums=[1, 2, 4, 6, 7], target=3))
