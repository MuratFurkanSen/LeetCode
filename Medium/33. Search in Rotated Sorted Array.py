class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nums = list(enumerate(nums))
        while len(nums) > 0:
            middle = len(nums) // 2
            index, val = nums[middle]
            if val == target:
                return index
            if len(nums) == 1:
                nums = []
            elif nums[0][1] < nums[middle][1]:
                if nums[0][1] <= target <= nums[middle][1]:
                    nums = nums[:middle]
                else:
                    nums = nums[middle + 1:]
            else:
                if nums[middle][1] <= target <= nums[-1][1]:
                    nums = nums[middle + 1:]
                else:
                    nums = nums[:middle]
            print(nums, middle)
        return -1

s = Solution()
print(s.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))