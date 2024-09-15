class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        changeIndex = len(nums) - 1
        while changeIndex > 1 and nums[changeIndex] <= nums[changeIndex - 1]:
            changeIndex -= 1
        changeIndex -= 1
        target = len(nums) - 1
        while target > changeIndex and nums[target] <= nums[changeIndex]:
            target -= 1

        if target == 0:
            nums[:] = nums[::-1]
        else:
            nums[changeIndex], nums[target] = nums[target], nums[changeIndex]
            nums[changeIndex + 1:] = nums[changeIndex + 1:][::-1]
