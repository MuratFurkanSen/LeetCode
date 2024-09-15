class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = (j-i)*min(height[i], height[j])
            if area > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea