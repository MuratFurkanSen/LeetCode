class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = self.binarySearch(nums, target, 0, len(nums))
        if mid == -1:
            return [-1, -1]
        start = mid
        end = mid
        while start > 0 and nums[start] == nums[start-1]:
            start -= 1
        while end < len(nums) - 1 and nums[end] == nums[end+1]:
            end += 1
        return [start, end]

    def binarySearch(self, nums: list[int], target: int,start:int ,end:int) -> int:
        middle_index = start + ((end-start) // 2)
        if end == start:
            return -1
        if nums[middle_index] > target:
            return self.binarySearch(nums, target,start,middle_index)
        elif nums[middle_index] < target:
            return self.binarySearch(nums, target,middle_index+1,end)
        else:
            return middle_index

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([1,2,3,4,5,6,7,8,9], 9))