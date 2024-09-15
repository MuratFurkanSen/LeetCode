class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        nums1Index = 0
        nums2Index = 0
        num = 0
        if totalLen % 2 == 1:
            for i in range((totalLen//2)+1):
                if nums1Index == len(nums1):
                    num = nums2[nums2Index]
                    nums2Index += 1
                elif nums2Index == len(nums2):
                    num = nums1[nums1Index]
                    nums1Index += 1
                elif nums1[nums1Index] < nums2[nums2Index]:
                    num = nums1[nums1Index]
                    nums1Index += 1
                else:
                    num = nums2[nums2Index]
                    nums2Index += 1
            return num
        else:
            num = 0
            for i in range((totalLen // 2) + 1):
                if nums1Index == len(nums1):
                    if i >= (totalLen//2)-1: num += nums2[nums2Index]
                    nums2Index += 1
                elif nums2Index == len(nums2):
                    if i >= (totalLen//2)-1: num += nums1[nums1Index]
                    nums1Index += 1
                elif nums1[nums1Index] < nums2[nums2Index]:
                    if i >= (totalLen//2)-1: num += nums1[nums1Index]
                    nums1Index += 1
                else:
                    if i >= (totalLen//2)-1: num += nums2[nums2Index]
                    nums2Index += 1
            return num/2

s = Solution()
print(s.findMedianSortedArrays([1, 2], [3,4]))


