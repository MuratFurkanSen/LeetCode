class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = -100000000
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                if abs(Sum - target) < abs(result - target):
                    result = Sum
                if Sum < target:
                    left += 1
                elif Sum > target:
                    right -= 1
                else:
                    return target
        return result

